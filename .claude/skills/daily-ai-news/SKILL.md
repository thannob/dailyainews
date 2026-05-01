---
name: daily-ai-news
description: Generate a daily Thai-language AI news brief covering up to 5 stories from the last 24 hours (rolling window, Asia/Bangkok), with URLs deduplicated against yesterday's brief so the same story is never covered twice in a row, enrich it with three expert perspectives (professor / AI specialist / professional programmer), commit it to this repository via the GitHub connector, and push a TL;DR to LINE. Use this when the user asks for a "daily AI news brief", a "สรุปข่าว AI วันนี้", triggers this skill by name, or when it runs on schedule via Claude Web Routine.
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

## Step 1 — Research (last 24h, deduplicated against yesterday)

Open `reference/trusted-sources.md` and treat it as the allow-list. Prefer sources from that list; do **not** invent outlets.

### 1a. Load yesterday's URLs (so we don't repeat ourselves)

Compute `YESTERDAY = TODAY − 1 day` in Asia/Bangkok.

Use the GitHub connector's `get_file_contents` to read `articles/{YESTERDAY}-brief.md` on `GITHUB_BRANCH`. Three outcomes:

- **File found.** Extract every URL from the body using a regex over inline-link syntax, i.e. all matches of `\[[^\]]+\]\((https?://[^)]+)\)` plus any plain URLs. Build a set `YESTERDAYS_URLS`. Lowercase host for the comparison; preserve the full URL otherwise (don't strip query strings or fragments — different paths are genuinely different stories).
- **File not found** (first-ever run, or yesterday's run was skipped). Set `YESTERDAYS_URLS = {}` (empty).
- **Connector error other than 404.** Surface the error and continue with `YESTERDAYS_URLS = {}`. Don't block the run on a stale-dedup-set worry.

Print the size: `Yesterday's URL count: N`.

### 1b. Gather candidates with `WebSearch`

Use `WebSearch` with rolling-24h queries:
- `AI news` (and Thai: `ข่าว AI`, `ปัญญาประดิษฐ์`). Add a date hint when supported (e.g. `qdr:d` on Google).
- Targeted per trusted source: `site:techcrunch.com AI`, `site:blognone.com AI`, etc.

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

### 1b-bis. Two filters — last 24h AND not in yesterday's brief

Apply both filters **before** selection. Drop on either failure.

**Filter A — Rolling 24h freshness.** A candidate passes only if its publish timestamp falls within `[now − 24h, now]` in Asia/Bangkok.

| What the snippet shows | Pass? |
|---|---|
| `วันนี้`, `Today`, `N hours ago` (any N ≤ 24) | ✅ pass |
| `เมื่อวาน` / `Yesterday` / `1 day ago` | ✅ pass (still inside the rolling 24h window — Filter B catches the dedup case below) |
| Explicit date within last 24h | ✅ pass |
| Anything older than 24h (`2 days ago`, `last week`, explicit older date) | ❌ drop |
| URL slug embeds a date older than 24h | ❌ drop, even if the snippet looks recent — slugs lie less than snippets |
| Date ambiguous / not surfaced | ❌ drop (do not guess) |

**Filter B — Not in yesterday's brief.** If the candidate's URL is in `YESTERDAYS_URLS` (loaded in Step 1a), drop it — even if it's still trending. We're publishing today's reporting, not re-running yesterday's coverage.

This is **URL-level dedup**, not topic-level. Different reporting on the same evolving story (e.g. a follow-up on the Google–Anthropic deal at a different URL) is fair game — that's genuinely new content. Same URL = same article = drop.

Edge case: if a story's snippet body references an event from yesterday but the URL itself is fresh-today reporting on it, the URL passes Filter B (URL not in yesterday's set) and Filter A (24h timestamp). Include it. The dedup is precise: the **specific article** wasn't in yesterday's brief, even if the topic was.

### 1b-tris. Hard rule — DO NOT bend the 24h filter

Filter A is a **hard gate**, not a guideline. Forbidden patterns observed in past runs that this rule explicitly prohibits:

- ❌ "I couldn't find 5 stories from today, so I included items from the past several days." → **NO.** Ship fewer; never older.
- ❌ "Most-recent indexed stories on trusted-sources.md happen to be from 3-5 days ago, so I'll use them." → **NO.** "Most recent on the index" ≠ "within 24h." If indexers haven't crawled today's news yet, that's a search-recency issue — try other queries, other domains, broader Thai sources. If still empty, ship the empty stub.
- ❌ "The 24-hour window could not be guaranteed via search snippets alone, so older items were included." → **NO.** That note is the sound of the contract breaking. If you can't guarantee freshness, you can't include the item. Period.
- ❌ Including an item with `Published: per search snippet (อ้างอิงข้อมูล [last quarter / last month])`. The dated content is what's being aggregated, not what's being reported today. Drop.

Before writing `sources.md`, **re-check every selected story's timestamp** against `now − 24h Asia/Bangkok` one more time. Any item that fails this check at the second pass is dropped silently — no apology note, no inclusion-with-caveat. If this leaves you with 0 stories, write the stub and commit.

The empty-day signal is correct output. A padded brief is broken output that erodes trust in every future run.

### 1c. Select up to 5

Select **up to 5** stories that passed both filters (24h fresh AND not in `YESTERDAYS_URLS`). Mix: aim for ≥1 Thai-language source and ≥3 international sources when supply allows. Prefer Tier 1 over Tier 2 when both are available for the same candidate. Prefer primary announcements over commentary.

If fewer than 5 candidates pass, ship what you have — even 1, even 0. Do **not** loosen either filter to fill the count.

If **0 stories** pass → write a one-line stub article (per Step 5a NO-OP rules) explaining whether the shortfall came from (a) the 24h freshness filter, (b) the dedup filter, or (c) both, and commit. The empty-day signal is itself information.

### 1d. Write `reference/sources.md`

Overwrite the file with this template — `Verification`, `FreshnessCheck`, and `DedupCheck` lines are all required:

```markdown
# Sources — {TODAY}

Generated: {TODAY} (Asia/Bangkok)
Runtime: {WEBFETCH_OK | WEBFETCH_BLOCKED}
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/{YESTERDAY}-brief.md ({N} URLs loaded)

1. **{Headline}**
   - Publisher: {Publisher}
   - URL: {final URL}
   - Published: {explicit timestamp or relative phrase as it appeared}
   - FreshnessCheck: ✅ within last 24h via {evidence — e.g. "snippet '3 hours ago'", "URL slug 2026-04-27", "publishedTime 2026-04-27T08:14"}
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS ({reason — e.g. "domain matches yesterday but path differs", "host not in yesterday at all")
   - Verification: {Tier 1 — WebFetch | Tier 2 — WebSearch snippet}
   - Summary: {1–2 sentences, strictly from fetched body or snippet}

2. ...
```

If you saw promising candidates but they failed either filter, list them in a "Dropped" block for traceability:
```
## Dropped
- {URL} — Filter A (>24h): "URL slug /2026/04/24/... is 3 days old"
- {URL} — Filter B (dedup): "appeared in articles/{YESTERDAY}-brief.md"
```

If you found <5 items, end with:
```
> Note: {N} items passed both filters this run. Of {M} candidates, {X} failed Filter A, {Y} failed Filter B.
```

If **0 stories** passed both filters → skip Step 2–4, write a minimal article (Step 5 still commits) explaining whether the shortfall came from (a) Filter A (no fresh news), (b) Filter B (everything available was already covered yesterday), or (c) both. The empty-day signal is itself information.

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
- **Do NOT mention verification mode anywhere in the article body.** No top banner, no italic tags, no footer line about Tier 2 / WEBFETCH_BLOCKED / search-snippet. The reader doesn't need any of that — they want news, not metadata about how it was sourced. Verification mode lives **only** in two places, both invisible to the reader: the commit message `[verify=search|webfetch]` tag, and `reference/sources.md`'s `Runtime:` + per-story `Verification:` lines. That's plenty for an operator to audit; nothing belongs in `articles/{TODAY}-brief.md` itself.

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
_Generated by the `daily-ai-news` skill on {TODAY} (Asia/Bangkok)._
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
| Story published > 24h ago | DROP (Filter A). List in "Dropped" of sources.md. |
| Story URL is in YESTERDAYS_URLS | DROP (Filter B) — already covered yesterday. |
| Story timestamp ambiguous / unparseable | DROP — never guess. |
| Yesterday's brief file unreadable (404 or other) | Continue with empty dedup set. Log the reason. |
| <5 stories pass both filters | Ship fewer (1–4 is fine). Note the breakdown (A vs B). |
| 0 stories pass both filters | Skip Step 2–4. Write a one-line stub explaining whether A, B, or both blocked everything. |
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
