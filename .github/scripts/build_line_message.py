#!/usr/bin/env python3
"""Build the LINE push body from a daily-ai-news brief markdown file.

Usage:
    build_line_message.py <article_path> <permalink>

Prints the message text to stdout. The caller wraps it in the LINE
push JSON payload.

Sizing strategy:
    1. First pass: render with each story's full body paragraph.
    2. If the total fits within LINE's 5000-char text-message limit,
       emit it verbatim.
    3. Otherwise, split each body into sentences and keep only the
       leading whole sentences that fit a per-story budget — never
       mid-sentence cuts, never "...".
    4. If even the first-sentence-each version exceeds the budget,
       drop trailing stories until it fits.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# --- knobs ----------------------------------------------------------------

# Hard ceiling for the LINE Messaging API text-message body.
LINE_TEXT_MAX = 5000

# How many TL;DR bullets to surface (skill writes 3 by contract).
TLDR_MAX = 3

# How many stories to surface (skill writes 5 by contract).
STORIES_MAX = 5

# Minimum sentences to keep per story when budget is tight.
MIN_SENTENCES_PER_STORY = 1


# --- parsing --------------------------------------------------------------

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
TLDR_BULLET_RE = re.compile(r"^>\s*-\s+(.+?)\s*$")
STORY_HEAD_RE = re.compile(
    r"^###\s+(\d+)\.\s+(.+?)\s+—\s+\[([^\]]+)\]\(([^)]+)\)\s*$"
)
H2_RE = re.compile(r"^##\s+")
ITALIC_TAG_RE = re.compile(r"^_\(.*\)_\s*$")

# Sentence-ending markers we trust. Thai prose often uses spaces rather
# than periods, so we also fall back to splitting on " — " (em dash with
# spaces) which the skill uses as a discourse-shift marker.
SENTENCE_END_RE = re.compile(r"(?<=[\.\?\!…])\s+")
EM_DASH_SPLIT_RE = re.compile(r"\s+—\s+")


def parse_article(text: str):
    """Return (title, tldr_bullets, stories).

    `stories` is a list of dicts with keys: n, title, pub, url, body.
    """
    lines = text.split("\n")

    title = ""
    for line in lines:
        m = H1_RE.match(line)
        if m:
            title = m.group(1)
            break

    tldr: list[str] = []
    in_tldr = False
    for line in lines:
        if line.startswith("> TL;DR"):
            in_tldr = True
            continue
        if not in_tldr:
            continue
        m = TLDR_BULLET_RE.match(line)
        if m:
            tldr.append(m.group(1))
            continue
        if not line.startswith(">"):
            break

    stories: list[dict] = []
    current: dict | None = None
    for line in lines:
        m = STORY_HEAD_RE.match(line)
        if m:
            if current is not None:
                stories.append(current)
            current = {
                "n": int(m.group(1)),
                "title": m.group(2).strip(),
                "pub": m.group(3).strip(),
                "url": m.group(4).strip(),
                "body": "",
            }
            continue
        if H2_RE.match(line):
            if current is not None:
                stories.append(current)
                current = None
            continue
        if current is None:
            continue
        if current["body"]:
            continue
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or stripped.startswith(">"):
            continue
        if ITALIC_TAG_RE.match(stripped):
            continue
        current["body"] = stripped

    if current is not None:
        stories.append(current)

    return title, tldr, stories


# --- sentence splitting / fitting -----------------------------------------

def split_sentences(text: str) -> list[str]:
    """Split a paragraph into sentences without losing trailing
    punctuation. Falls back to em-dash splitting for Thai prose that
    doesn't terminate sentences with periods."""
    if not text:
        return []
    parts = SENTENCE_END_RE.split(text)
    sentences = [p.strip() for p in parts if p.strip()]
    # If we ended up with one very long "sentence", probably no
    # punctuation — try the soft em-dash fallback.
    if len(sentences) == 1 and len(sentences[0]) > 240:
        parts = EM_DASH_SPLIT_RE.split(sentences[0])
        if len(parts) > 1:
            # Re-attach em dashes to the start of each follow-up part
            # so the prose still reads naturally.
            head, *tail = [p.strip() for p in parts if p.strip()]
            sentences = [head] + [f"— {t}" for t in tail]
    return sentences


def fit_sentences(sentences: list[str], max_chars: int) -> str:
    """Return as many leading whole sentences as fit within max_chars.

    Guarantees:
        - Never returns mid-sentence text — only complete sentences.
        - Never appends '...'; the natural sentence-ending punctuation
          provides the stop signal.
        - Always returns at least the first sentence if any exists,
          even if it exceeds the budget — better one full thought than
          a truncated one.
    """
    if not sentences:
        return ""
    out = sentences[0]
    for s in sentences[1:]:
        candidate = out + " " + s
        if len(candidate) > max_chars:
            break
        out = candidate
    return out


# --- formatting -----------------------------------------------------------

def render(title: str, tldr: list[str], stories: list[dict],
           permalink: str, body_func) -> str:
    """Render the full message. `body_func(i, story) -> str` decides
    how much of each story body to include — full body, sentence-fitted,
    or empty."""
    parts: list[str] = []
    parts.append(f"📰 {title}" if title else "📰 สรุปข่าว AI")
    parts.append("")

    if tldr:
        parts.append("TL;DR")
        for b in tldr[:TLDR_MAX]:
            parts.append(f"• {b}")
        parts.append("")

    if stories:
        parts.append("━━━━━━━━━━")
        parts.append("")
        for i, s in enumerate(stories):
            parts.append(f"🔸 {s['n']}. {s['title']}")
            body = body_func(i, s)
            if body:
                parts.append(f"   {body}")
            if s.get("pub") and s.get("url"):
                parts.append(f"   📎 {s['pub']}: {s['url']}")
            parts.append("")

    parts.append(f"อ่านฉบับเต็ม: {permalink}")
    return "\n".join(parts)


def build_message(title: str, tldr: list[str], stories: list[dict],
                  permalink: str, max_chars: int = LINE_TEXT_MAX) -> str:
    """Render the message, sentence-fitting bodies if the full version
    overflows the LINE 5000-char limit."""
    stories = stories[:STORIES_MAX]

    # Pass 1: full bodies. Common case — message is well under 5000.
    msg = render(title, tldr, stories, permalink,
                 body_func=lambda i, s: s.get("body", ""))
    if len(msg) <= max_chars:
        return msg

    # Pass 2: per-story budget at sentence granularity.
    sents_per_story = [split_sentences(s.get("body", "")) for s in stories]

    def fit_to_budget(stories_in: list[dict],
                      sents_in: list[list[str]]) -> str:
        if not stories_in:
            return render(title, tldr, [], permalink, body_func=lambda i, s: "")
        skeleton = render(title, tldr, stories_in, permalink,
                          body_func=lambda i, s: "")
        # +4 per body line accounts for "   " indent and a newline.
        body_overhead = 4 * len(stories_in)
        available = max_chars - len(skeleton) - body_overhead
        if available <= 0:
            per = 0
        else:
            per = available // len(stories_in)
        return render(title, tldr, stories_in, permalink,
                      body_func=lambda i, s: fit_sentences(sents_in[i], per))

    msg = fit_to_budget(stories, sents_per_story)
    if len(msg) <= max_chars:
        return msg

    # Pass 3: drop stories from the end until it fits.
    while len(stories) > 1:
        stories = stories[:-1]
        sents_per_story = sents_per_story[:-1]
        msg = fit_to_budget(stories, sents_per_story)
        if len(msg) <= max_chars:
            return msg

    # Last resort: return whatever pass 3 produced (may be slightly
    # over budget if even one story's first sentence is huge — but at
    # least it's a complete sentence, not a "...").
    return msg


# --- entrypoint -----------------------------------------------------------

def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(
            f"usage: {argv[0]} <article_path> <permalink>",
            file=sys.stderr,
        )
        return 2
    article_path = Path(argv[1])
    permalink = argv[2]
    text = article_path.read_text(encoding="utf-8")
    title, tldr, stories = parse_article(text)
    msg = build_message(title, tldr, stories, permalink)
    sys.stdout.write(msg)
    if not msg.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
