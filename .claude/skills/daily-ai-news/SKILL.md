---
name: daily-ai-news
description: Generate a daily Thai-language AI news brief covering ONLY stories published today in Asia/Bangkok timezone (no rolling 24h window, no yesterday's news), enrich it with three expert perspectives (professor / AI specialist / professional programmer), commit it to this repository via the GitHub connector, and push a TL;DR to LINE. Use this when the user asks for a "daily AI news brief", a "สรุปข่าว AI วันนี้", triggers this skill by name, or when it runs on schedule via Claude Web Routine.
---

# Daily AI News Brief

End-to-end routine that produces **one Markdown article per day** at `articles/YYYY-MM-DD-brief.md`, commits it via the GitHub connector, then notifies LINE. Runs entirely inside Claude (Web / Routine) — **no shell, no git CLI, no Bash**.

## Runtime contract

- **Timezone:** Asia/Bangkok. Compute `YYYY-MM-DD` from this TZ.
- **Tools allowed:** `WebSearch`, `WebFetch`, `Read`, `Write`, `Edit`, and the configured GitHub MCP connector.
- **Tools FORBIDDEN:** `Bash`, any shell, any `git` CLI. If you catch yourself reaching for `Bash`, stop — this skill must run on Claude Remote Routine where shell is unavailable.
- **No fabrication:** every news item MUST have a real, fetched URL from the trusted-source list in `reference/trusted-sources.md`. If you cannot verify a URL via `WebFetch`, drop the item.

## Required environment

The Routine itself needs very little env now — LINE moved out to GitHub Actions (see Step 6). The skill reads only:

| Var | Purpose | Required | Source |
|---|---|---|---|
| `GITHUB_OWNER` | GitHub account / org owning the target repo | yes | inline prompt, or `reference/defaults.json` fallback |
| `GITHUB_REPO` | Target repo name | yes | inline prompt, or `reference/defaults.json` fallback |
| `GITHUB_BRANCH` | Branch to commit on (default `main`) | no | inline prompt, or `reference/defaults.json` fallback |

`LINE_CHANNEL_ACCESS_TOKEN` / `LINE_TO` are **no longer read by the skill** — they live in GitHub repo secrets and are consumed by `.github/workflows/line-notify.yml`. If you still see them in an older prompt, ignore them; the Routine doesn't need them.

Claude Web Routine's Cloud Environment feature does not reliably inject values into the model's prompt context (observed empirically in this deployment). That's fine — GitHub vars have a committed defaults fallback, and LINE secrets now live on a surface (GH secrets) that actually works.

### Env resolution order (apply per variable, first hit wins)

1. **Inline in the skill invocation prompt.** The caller may have written `GITHUB_OWNER = thannob` directly in the run prompt. Use that.
2. **`reference/defaults.json`** — read with the `Read` tool. This is the canonical fallback for the three `GITHUB_*` vars.
3. **Missing** → hard abort.

Do **not** invent values. Do **not** treat literal placeholder strings like `{{GITHUB_OWNER}}` or `$GITHUB_OWNER` as real values — those are signs substitution failed and the caller needs to either paste real values or let the defaults take over.

---

## Step 0 — Preflight (fail fast, log loudly)

1. **GitHub connector check.** Confirm the GitHub MCP connector is connected (look for tools whose names start with `mcp__github` / `mcp__Github` / similar — e.g. `create_or_update_file`, `push_files`, `get_file_contents`). If **none** are available:
   - Print: `ABORT: GitHub connector is not connected. Enable the GitHub MCP connector in Claude settings and re-run.`
   - **Stop immediately.** Do not research, do not write any files.
2. **Resolve env.** For each variable in the table above, walk the resolution order. `Read` `reference/defaults.json` exactly once and cache it.
3. **Print a resolution table** so failures are obvious:
   ```
   Env resolution:
     GITHUB_OWNER   = thannob       (source: defaults.json)
     GITHUB_REPO    = dailyainews   (source: defaults.json)
     GITHUB_BRANCH  = main          (source: defaults.json)
   ```
4. **GitHub gate.** If `GITHUB_OWNER` or `GITHUB_REPO` is `***missing***` → abort with a clear log.
5. **Date.** Compute `TODAY = YYYY-MM-DD` in `Asia/Bangkok`. Use this string for the filename, commit message, and article body.

---

## Step 1 — Research (today only, up to 5 stories)

Open `reference/trusted-sources.md` and treat it as the allow-list. Prefer sources from that list; do **not** invent outlets.

### 1a. Gather candidates with `WebSearch`

Use `WebSearch` with **today-only** queries:
- `AI news today` (and Thai: `ข่าว AI วันนี้`, `ปัญญาประดิษฐ์ วันนี้`).
- Targeted per trusted source: `site:techcrunch.com AI {YYYY-MM-DD}`, `site:blognone.com AI วันนี้`, etc.

Capture for each candidate: URL, title, publisher (inferred from domain vs trusted-sources list), and the **search-result snippet** verbatim — including any timestamp string the search engine surfaces (e.g. "2 hours ago", "April 27, 2026", "วันนี้").

### 1b. Verification — tiered (handles egress-blocked runtimes)

Each story is assigned a verification tier. Do a quick `WebFetch` probe on one trusted URL (e.g. `https://example.com`) at the start of this step to detect whether WebFetch works at all in this runtime. Label the runtime:

- **`WEBFETCH_OK`** — probe returned 2xx.
- **`WEBFETCH_BLOCKED`** — probe returned 403 / network error (typical in Claude Web Routine today).

Then for each candidate:

| Tier | Requirements | Allowed when |
|---|---|---|
| **Tier 1 — Full fetch** | `WebFetch` returns 2xx for the URL; body contains the headline and an explicit timestamp on `TODAY` (Asia/Bangkok) | `WEBFETCH_OK` |
| **Tier 2 — Search snippet** | URL's domain is on `reference/trusted-sources.md`; `WebSearch` result includes a substantive snippet AND a timestamp resolvable to `TODAY` (Asia/Bangkok); **summary must paraphrase only what's in the snippet** | always — but only the sole option when `WEBFETCH_BLOCKED` |
| **Drop** | Can't satisfy Tier 1 or Tier 2 | — |

**Never** cite a URL that you could not at least see in a `WebSearch` result for a trusted-source domain. Search engines don't invent URLs, so a URL present in search results is real. The risk is **staleness of the snippet**, not fabrication — mitigate by never asserting more than the snippet says.

### 1b-bis. Today-only freshness check (HARD GATE)

Apply this filter **before** moving to selection. A candidate passes only if its publish timestamp resolves to the same calendar date as `TODAY` in Asia/Bangkok. **Yesterday is not "today" — drop it.** No rolling 24h window, no "close enough", no padding.

Resolving snippet timestamps:

| What the snippet shows | Pass? |
|---|---|
| `วันนี้`, `Today`, `HH:MM today` | ✅ pass |
| Explicit date `YYYY-MM-DD` or `เม.ย. DD, 2026` matching `TODAY` | ✅ pass |
| `N hours ago` where `now − N hours ≥ TODAY 00:00 Asia/Bangkok` | ✅ pass |
| `N hours ago` where the computed time is before `TODAY 00:00 Bangkok` | ❌ drop (it's yesterday-Bangkok even if same UTC date) |
| `เมื่อวาน`, `Yesterday`, `1 day ago` | ❌ drop |
| Any explicit date < `TODAY` | ❌ drop |
| URL slug embeds a date < `TODAY` (e.g. `/2026/04/24/...` when TODAY=`2026-04-25`) | ❌ drop, even if the snippet says otherwise — the slug is a strong signal |
| Date ambiguous / not surfaced | ❌ drop (do not guess) |

When in doubt, **drop**. A short brief that's actually about today beats a five-story brief padded with yesterday's news.

If a story's body in the snippet references a launch/event from a previous day (e.g. "GPT-5.5 launched on April 23" while TODAY is `2026-04-25`), that's a **follow-up commentary** — drop it. We want the day's primary announcements, not retrospectives.

### 1c. Select up to 5

Select **up to 5** stories that passed the today-only gate. Mix: aim for ≥1 Thai-language source and ≥3 international sources when supply allows. Prefer Tier 1 over Tier 2 when both are available for the same candidate. Prefer primary announcements over commentary.

If fewer than 5 candidates pass the gate, ship what you have — even 1, even 0. Do **not** reach back to yesterday or earlier to fill the count. The brief is "today's news"; on slow days it's short.

If **0 stories** pass the gate → write a one-line stub article (per Step 5a NO-OP rules) explaining "no qualifying stories on TODAY" and commit. The empty-day signal is itself information.

### 1d. Write `reference/sources.md`

Overwrite the file with this template — the `Verification` and `TodayCheck` lines are required:

```markdown
# Sources — {TODAY}

Generated: {TODAY} (Asia/Bangkok)
Runtime: {WEBFETCH_OK | WEBFETCH_BLOCKED}
Freshness gate: today-only (Asia/Bangkok)

1. **{Headline}**
   - Publisher: {Publisher}
   - URL: {final URL}
   - Published: {explicit timestamp or relative phrase as it appeared}
   - TodayCheck: ✅ resolves to {TODAY} via {evidence — e.g. "URL slug 2026-04-27", "snippet says 'today'", "'2 hours ago' at 09:00 Bangkok = same calendar day"}
   - Verification: {Tier 1 — WebFetch | Tier 2 — WebSearch snippet}
   - Summary: {1–2 sentences, strictly from fetched body or snippet}

2. ...
```

If you saw promising candidates but they failed the today-only gate, list them in a separate block at the bottom for traceability:
```
## Dropped (not today)
- {URL} — {why} — e.g. "URL slug /2026/04/26/... yesterday-Bangkok"
```

If you found <5 items, end with:
```
> Note: only N items passed the today-only gate ({WEBFETCH_OK|WEBFETCH_BLOCKED}).
```

If **0 stories** passed the today-only gate → skip Step 2–4, write a minimal article (Step 5 still commits) explaining "no qualifying stories on TODAY". This is intentional: an empty day is itself a signal — not a reason to relax the gate.

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
- Do **not** invent quotes, numbers, dates, or names. If the source didn't say it (Tier 1 body) or if the snippet didn't say it (Tier 2), don't write it.
- Thai-first prose; technical terms can stay in English.
- **Do NOT add per-story italic tags** for Tier 2 sourcing — no `_(อ้างอิงจาก search snippet …)_` blurb at the end of any paragraph. The reader doesn't need it inline.
- **Do NOT add a top-of-article banner** when the runtime is `WEBFETCH_BLOCKED`. The verification mode is already surfaced in three other places (commit message `[verify=search]`, `reference/sources.md` `Runtime:` line, and the footer `Verification mode:` line) — that's plenty for traceability. Keep the article body clean for the reader.

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
_Generated by the `daily-ai-news` skill on {TODAY} (Asia/Bangkok). Verification mode: {WEBFETCH_OK | WEBFETCH_BLOCKED → WebSearch-snippet}._
```

Save the final markdown as a string in memory — call it `ARTICLE_BODY` — for the commit step.

---

## Step 5 — Commit via GitHub connector

**Never use git CLI.** Use the connector tool. The exact tool name depends on the connector build; common shapes:

- `create_or_update_file` with params: `owner`, `repo`, `path`, `branch`, `message`, `content` (plain UTF-8 string; connector handles base64 if needed), optional `sha` for updates.
- `push_files` with a `files` array.

### 5a. Idempotency check

Before writing, call the connector's `get_file_contents` (or equivalent) for `articles/{TODAY}-brief.md` on `branch`. Three outcomes:

- **Not found.** Create it. Proceed.
- **Found, content byte-for-byte identical to `ARTICLE_BODY`.** Skip the commit. Log: `Run status: NO-OP (idempotent) — today's brief already committed at <existing SHA>`. Capture that SHA as `COMMIT_SHA` and **still proceed to Step 6** (LINE may have been skipped last time).
- **Found, content differs.** Update with the returned `sha` — this is a meaningful re-run (e.g. the earlier run was `WEBFETCH_BLOCKED` and this one has fresh data).

### 5b. Commit

1. Set:
   - `path = articles/{TODAY}-brief.md`
   - `branch = GITHUB_BRANCH or "main"`
   - `message = "brief: {TOPIC} {TODAY} [verify={webfetch|search}]"` where `{TOPIC}` is a ≤40-char summary of the day's dominant theme (e.g. `OpenAI ships new agent API`), and `verify=` reflects the runtime label from Step 1b.
   - `content = ARTICLE_BODY`
2. Call the connector's create-or-update tool.
3. If the response includes a commit SHA (typical field: `commit.sha` or `sha`), capture it as `COMMIT_SHA`. Otherwise attempt to read it back by calling the connector's `get_file_contents` / commit-list tool for the branch.
4. Form `PERMALINK = https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{COMMIT_SHA}/articles/{TODAY}-brief.md`. Pin to the SHA — do **not** use `/blob/main/...` (that link drifts).
5. If the commit call fails: print the full connector error, do not retry silently, do not proceed to LINE.

---

## Step 6 — LINE push (handled externally)

**This skill does NOT send to LINE.** The `WebFetch` tool in Claude Web Routine accepts only `(url, prompt)` — no method, no headers, no body — so it cannot POST to `api.line.me/v2/bot/message/push` with a Bearer token. That's a tool-schema limit, not an egress or env issue.

LINE dispatch is instead handled by a GitHub Actions workflow at [`.github/workflows/line-notify.yml`](../../../.github/workflows/line-notify.yml) that triggers on every push to `main` affecting `articles/*-brief.md`. The workflow:

- Reads repo secrets `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_TO`.
- Extracts the title + TL;DR bullets from the newly committed brief.
- Builds a permalink pinned to the commit SHA.
- POSTs to `api.line.me` with `curl` (full HTTP capability).
- Fails loudly in the Actions UI on non-200.

What the skill does here:

1. Do nothing that talks to LINE directly — no `WebFetch`, no markers, no retries.
2. Print one line for the operator: `LINE: dispatched by .github/workflows/line-notify.yml (see Actions tab for delivery status)`.
3. If the commit in Step 5 was a NO-OP (idempotent), the workflow will NOT fire — because no push happened. This is correct: no new content means no new notification.

If the maintainer wants to force a re-notify for an already-committed brief, they can run the workflow manually via `gh workflow run line-notify.yml -f file=articles/{TODAY}-brief.md` or the GitHub UI.

---

## Step 7 — Final report

Print a compact summary to the user / routine log:

```
✅ Committed: articles/{TODAY}-brief.md @ {COMMIT_SHA_short}
   {PERMALINK}
LINE: dispatched by .github/workflows/line-notify.yml (see Actions tab for delivery status)
```

If Step 5a decided NO-OP (identical content already on main), say so instead:
```
Run status: NO-OP (idempotent) — today's brief already at {COMMIT_SHA_short}
   {PERMALINK}
LINE: not re-notified (no new commit → workflow does not fire)
```

---

## Error-handling summary

| Condition | Action |
|---|---|
| GitHub connector missing | Abort before any work. Log clearly. |
| `WEBFETCH_BLOCKED` (whole runtime) | Switch to Tier 2 (WebSearch snippet) for every story; commit with `[verify=search]`. |
| Story published before TODAY in Asia/Bangkok | DROP — no rolling 24h window, no padding. List in "Dropped (not today)" of sources.md for traceability. |
| Story timestamp ambiguous / unparseable | DROP — never guess that yesterday's news is today's. |
| <5 stories pass the today-only gate | Ship fewer (1–4 is fine). Note the shortfall in sources.md. |
| 0 stories pass the today-only gate | Skip Step 2–4. Write a one-line stub article. Commit. The empty-day signal is intentional. |
| URL unreachable / paywalled (single story, `WEBFETCH_OK` runtime) | Drop that item; try Tier 2 for it; if both fail, skip it. |
| GitHub commit fails | Surface the error. Stop. |
| Today's article already committed, content identical | NO-OP. LINE workflow does not fire (intentional). |
| Today's article already committed, content differs | Update via the returned SHA. LINE workflow will fire on the new push. |
| LINE issues | Not this skill's concern — see `.github/workflows/line-notify.yml` and the Actions tab. |

## Files this skill touches

- `reference/sources.md` — overwritten each run (working artifact)
- `reference/perspectives.md` — overwritten each run (working artifact)
- `articles/{TODAY}-brief.md` — the single committed output

`reference/trusted-sources.md` and `reference/defaults.json` are **read-only** for this skill.
