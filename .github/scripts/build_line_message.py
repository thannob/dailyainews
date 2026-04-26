#!/usr/bin/env python3
"""Build the LINE push body from a daily-ai-news brief markdown file.

Usage:
    build_line_message.py <article_path> <permalink>

Prints the message text to stdout. The caller wraps it in the LINE
push JSON payload.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# --- knobs ----------------------------------------------------------------

# Per-story body truncation. Thai text is counted by Unicode codepoints,
# which is what LINE charges against the 5000-char text-message limit.
BODY_MAX_CHARS = 180

# How many TL;DR bullets to surface (skill writes 3 by contract).
TLDR_MAX = 3

# How many stories to surface (skill writes 5 by contract; if ever
# fewer, we just show what's there).
STORIES_MAX = 5


# --- parsing --------------------------------------------------------------

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
TLDR_BULLET_RE = re.compile(r"^>\s*-\s+(.+?)\s*$")
STORY_HEAD_RE = re.compile(
    r"^###\s+(\d+)\.\s+(.+?)\s+—\s+\[([^\]]+)\]\(([^)]+)\)\s*$"
)
H2_RE = re.compile(r"^##\s+")
ITALIC_TAG_RE = re.compile(r"^_\(.*\)_\s*$")


def parse_article(text: str):
    """Return (title, tldr_bullets, stories).

    `stories` is a list of dicts with keys: n, title, pub, url, body.
    """
    lines = text.split("\n")

    # Title — first H1.
    title = ""
    for line in lines:
        m = H1_RE.match(line)
        if m:
            title = m.group(1)
            break

    # TL;DR — bullets inside the `> TL;DR` blockquote.
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
        # Stay in the TL;DR block on other `> ...` lines (e.g. blank
        # quote lines), but break on the first non-quote line.
        if not line.startswith(">"):
            break

    # Stories — H3 headings of the form
    #   ### N. Headline — [Publisher](URL)
    # followed by a body paragraph. Stop at the next H2 (e.g. "## Action items").
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


# --- formatting -----------------------------------------------------------

def truncate(s: str, n: int) -> str:
    """Codepoint-aware truncation with an ellipsis."""
    if len(s) <= n:
        return s
    # Trim trailing whitespace before adding the ellipsis so we don't
    # produce odd "word …" gaps.
    return s[: max(0, n - 1)].rstrip() + "…"


def build_message(title: str, tldr: list[str], stories: list[dict], permalink: str) -> str:
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
        for s in stories[:STORIES_MAX]:
            parts.append(f"🔸 {s['n']}. {s['title']}")
            if s["body"]:
                parts.append(f"   {truncate(s['body'], BODY_MAX_CHARS)}")
            if s.get("pub") and s.get("url"):
                parts.append(f"   📎 {s['pub']}: {s['url']}")
            parts.append("")

    parts.append(f"อ่านฉบับเต็ม: {permalink}")
    return "\n".join(parts)


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
