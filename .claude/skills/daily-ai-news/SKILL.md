---
name: daily-ai-news
description: Generate a daily Thai-language AI news brief from the last 24 hours of trusted sources, enrich it with three expert perspectives (professor / AI specialist / professional programmer), commit it to this repository via the GitHub connector, and push a TL;DR to LINE. Use this when the user asks for a "daily AI news brief", a "สรุปข่าว AI วันนี้", triggers this skill by name, or when it runs on schedule via Claude Web Routine.
---

# Daily AI News Brief

End-to-end routine that produces **one Markdown article per day** at `articles/YYYY-MM-DD-brief.md`, commits it via the GitHub connector, then notifies LINE. Runs entirely inside Claude (Web / Routine) — **no shell, no git CLI, no Bash**.

## Runtime contract

- **Timezone:** Asia/Bangkok. Compute `YYYY-MM-DD` from this TZ.
- **Tools allowed:** `WebSearch`, `WebFetch`, `Read`, `Write`, `Edit`, and the configured GitHub MCP connector.
- **Tools FORBIDDEN:** `Bash`, any shell, any `git` CLI. If you catch yourself reaching for `Bash`, stop — this skill must run on Claude Remote Routine where shell is unavailable.
- **No fabrication:** every news item MUST have a real, fetched URL from the trusted-source list in `reference/trusted-sources.md`. If you cannot verify a URL via `WebFetch`, drop the item.

## Required environment (read from the Routine env)

| Var | Purpose | Required |
|---|---|---|
| `GITHUB_OWNER` | GitHub account / org owning the target repo | yes |
| `GITHUB_REPO` | Target repo name | yes |
| `GITHUB_BRANCH` | Branch to commit on (default `main`) | no |
| `LINE_CHANNEL_ACCESS_TOKEN` | Messaging API channel token | no (skip LINE if absent) |
| `LINE_TO` | Target userId / groupId / roomId | no (skip LINE if absent) |

If env is not directly exposed, ask the caller to paste the values at the top of the run, then proceed.

---

## Step 0 — Preflight (fail fast, log loudly)

1. **GitHub connector check.** Confirm the GitHub MCP connector is connected (look for tools whose names start with `mcp__github` / `mcp__Github` / similar — e.g. `create_or_update_file`, `push_files`, `get_file_contents`). If **none** are available:
   - Print: `ABORT: GitHub connector is not connected. Enable the GitHub MCP connector in Claude settings and re-run.`
   - **Stop immediately.** Do not research, do not write any files.
2. **LINE env check.** Read `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_TO`.
   - If either is missing → set `LINE_ENABLED=false`, print `LINE: skipped (env missing)`, but continue — the commit step must still run.
3. **Date.** Compute `TODAY = YYYY-MM-DD` in `Asia/Bangkok`. Use this string for the filename, commit message, and article body.

---

## Step 1 — Research (last 24h, 5 stories)

Open `reference/trusted-sources.md` and treat it as the allow-list. Prefer sources from that list; do **not** invent outlets.

1. Use `WebSearch` with queries like:
   - `AI news` with a date filter for the last 24h (include Thai queries: `ข่าว AI`, `ปัญญาประดิษฐ์ วันนี้`).
   - Targeted queries per trusted source (e.g. `site:techcrunch.com AI`, `site:blognone.com AI`).
2. For each candidate, use `WebFetch` to open the URL and extract:
   - Final canonical URL (follow redirects; reject paywall-only or login-walled pages).
   - Headline, publisher, publish timestamp (must be within the last 24h in the source's own timezone; be generous at the edges).
   - A 1–2 sentence factual summary, in your own words.
3. Select **exactly 5** stories. Mix: aim for ≥1 Thai-language source and ≥3 international sources. Prefer primary announcements over commentary.
4. Write the verified list to `reference/sources.md` using this exact template — overwrite the file:

```markdown
# Sources — {TODAY}

Generated: {TODAY} (Asia/Bangkok)

1. **{Headline}**
   - Publisher: {Publisher}
   - URL: {final URL}
   - Published: {ISO timestamp as shown on page}
   - Summary: {1–2 factual sentences, your words}

2. ...
```

If you cannot find 5 verifiable items, write however many you found and add a line `> Note: only N verified items found within 24h window.` — do not pad with fiction.

---

## Step 2 — Draft the article

Create the first draft in memory (don't commit yet). Structure:

```markdown
# สรุปข่าว AI ประจำวันที่ {TODAY}

> TL;DR
> - {bullet 1 — one sentence}
> - {bullet 2}
> - {bullet 3}

## ข่าวเด่น 24 ชั่วโมงที่ผ่านมา

### 1. {Headline}
{2–4 sentences. Link inline: [{Publisher}]({URL}). Every factual claim must trace to that URL.}

### 2. ...
```

Rules:
- Every story references its source URL at least once via inline markdown link.
- Do **not** invent quotes, numbers, dates, or names. If the source didn't say it, don't write it.
- Thai-first prose; technical terms can stay in English.

---

## Step 3 — Three perspectives

For each of the 5 stories, produce a short reaction from **three personas**. Write them to `reference/perspectives.md` (overwrite) using this layout:

```markdown
# Perspectives — {TODAY}

## 1. {Headline}

**อาจารย์ (มหาวิทยาลัย):** {1–2 sentences — pedagogical framing, what students/readers should understand}
**ผู้เชี่ยวชาญด้าน AI:** {1–2 sentences — technical substance, caveats, what's genuinely new}
**โปรแกรมเมอร์มืออาชีพ:** {1–2 sentences — practical impact on day-to-day engineering work, tooling, cost}

## 2. ...
```

Keep each persona's voice distinct. No filler. No platitudes.

---

## Step 4 — Rewrite (integrated)

Produce the **final article body** by weaving the three perspectives into each story rather than listing them as separate blocks. Append an **Action items** section at the end.

Target structure for the final file `articles/{TODAY}-brief.md`:

```markdown
# สรุปข่าว AI ประจำวันที่ {TODAY}

> TL;DR
> - {bullet 1}
> - {bullet 2}
> - {bullet 3}

## ข่าวเด่น 24 ชั่วโมงที่ผ่านมา

### 1. {Headline} — [{Publisher}]({URL})
{2–4 sentences of reporting, then a paragraph that integrates the professor / AI-expert / programmer angles naturally. No "persona:" labels in the body.}

### 2. ...

## Action items

- **สำหรับอาจารย์/นักเรียน:** {1 concrete action}
- **สำหรับผู้เชี่ยวชาญ AI:** {1 concrete action}
- **สำหรับโปรแกรมเมอร์:** {1 concrete action}

---
_Generated by the `daily-ai-news` skill on {TODAY} (Asia/Bangkok). Sources verified via WebFetch._
```

Save the final markdown as a string in memory — call it `ARTICLE_BODY` — for the commit step.

---

## Step 5 — Commit via GitHub connector

**Never use git CLI.** Use the connector tool. The exact tool name depends on the connector build; common shapes:

- `create_or_update_file` with params: `owner`, `repo`, `path`, `branch`, `message`, `content` (plain UTF-8 string; connector handles base64 if needed), optional `sha` for updates.
- `push_files` with a `files` array.

Do:

1. Set:
   - `path = articles/{TODAY}-brief.md`
   - `branch = GITHUB_BRANCH or "main"`
   - `message = "brief: {TOPIC} {TODAY}"` where `{TOPIC}` is a ≤40-char summary of the day's dominant theme (e.g. `OpenAI ships new agent API`).
   - `content = ARTICLE_BODY`
2. Call the connector's create-or-update tool.
3. If the response includes a commit SHA (typical field: `commit.sha` or `sha`), capture it as `COMMIT_SHA`. Otherwise attempt to read it back by calling the connector's `get_file_contents` / commit-list tool for the branch.
4. Form `PERMALINK = https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{COMMIT_SHA}/articles/{TODAY}-brief.md`. Pin to the SHA — do **not** use `/blob/main/...` (that link drifts).
5. If the commit call fails: print the full connector error, do not retry silently, do not proceed to LINE.

---

## Step 6 — LINE push (optional)

Skip this step entirely if `LINE_ENABLED=false`.

Build the message text:

```
📰 สรุปข่าว AI {TODAY}

TL;DR
• {bullet 1}
• {bullet 2}
• {bullet 3}

อ่านฉบับเต็ม: {PERMALINK}
```

Send via **`WebFetch` with method POST** (no curl, no shell):

- URL: `https://api.line.me/v2/bot/message/push`
- Headers:
  - `Authorization: Bearer {LINE_CHANNEL_ACCESS_TOKEN}`
  - `Content-Type: application/json`
- Body (JSON):
  ```json
  {
    "to": "{LINE_TO}",
    "messages": [{ "type": "text", "text": "<msg>" }]
  }
  ```

On response:
- **HTTP 200:** print `LINE: ok`.
- **Non-200:** print `LINE ERROR: status={code} body={responseBody}`. **Do not retry.** The commit already landed — a failed notification is surfaced, not swallowed.

If `WebFetch` in the current environment doesn't allow POST with custom headers, say so explicitly and stop rather than falling back to a GET — never silently degrade.

---

## Step 7 — Final report

Print a compact summary to the user / routine log:

```
✅ Committed: articles/{TODAY}-brief.md @ {COMMIT_SHA_short}
   {PERMALINK}
{LINE status line}
```

---

## Error-handling summary

| Condition | Action |
|---|---|
| GitHub connector missing | Abort before any work. Log clearly. |
| <5 verifiable stories | Proceed with what you have; note the shortfall in sources.md. |
| URL unreachable / paywalled | Drop that item, find another. Never invent. |
| GitHub commit fails | Surface the error. Do not continue to LINE. |
| LINE env missing | Skip step 6. Commit is still the success criterion. |
| LINE API non-200 | Log status + body. No retry. |

## Files this skill touches

- `reference/sources.md` — overwritten each run (working artifact)
- `reference/perspectives.md` — overwritten each run (working artifact)
- `articles/{TODAY}-brief.md` — the single committed output

`reference/trusted-sources.md` is **read-only** for this skill.
