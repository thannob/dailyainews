# dailyainews

A Claude Code skill that produces **one Thai-language AI news brief per day**, commits it to this repo, and pings a LINE chat with the TL;DR.

The entire flow is executable from inside Claude — **no shell, no git CLI, no cron on your laptop**. The intended host is [Claude Web Routine](https://claude.ai), so it survives your machine being asleep.

```
07:00 Asia/Bangkok  ──▶  Claude Routine fires  ──▶  WebSearch + WebFetch (5 stories)
                                                        │
                                                        ▼
                                               draft → 3 perspectives → rewrite
                                                        │
                                                        ▼
                                          GitHub MCP connector commits
                                          articles/YYYY-MM-DD-brief.md
                                                        │                     push to main
                                                        ▼
                                        GitHub Actions (.github/workflows/line-notify.yml)
                                                        │
                                                        ▼
                                         curl POST https://api.line.me/v2/bot/message/push
                                         (using repo secrets LINE_CHANNEL_ACCESS_TOKEN + LINE_TO)
```

**Why LINE dispatch lives in GitHub Actions, not the skill:** Claude Web Routine's `WebFetch` tool accepts only `(url, prompt)` — it cannot issue a POST with `Authorization: Bearer`, which LINE requires. Rather than fight a tool-schema limit, we moved LINE to Actions, which has real `curl` and real secrets.

## Repo layout

```
.
├── .claude/
│   └── skills/
│       └── daily-ai-news/
│           ├── SKILL.md                # the skill — Claude reads this
│           └── reference/
│               ├── trusted-sources.md  # allow-list of publishers (read-only)
│               ├── sources.md          # overwritten each run
│               └── perspectives.md     # overwritten each run
├── articles/                           # committed output lives here
│   └── YYYY-MM-DD-brief.md
├── .env.example
├── .gitignore
└── README.md
```

## What the skill does, in short

1. **Preflight.** Verifies the GitHub MCP connector is connected. Aborts otherwise. Checks LINE env — optional.
2. **Research.** `WebSearch` + `WebFetch` for 5 AI stories in the last 24h, drawn only from [`reference/trusted-sources.md`](./.claude/skills/daily-ai-news/reference/trusted-sources.md). Writes [`reference/sources.md`](./.claude/skills/daily-ai-news/reference/sources.md).
3. **Three perspectives.** Each story gets a short reaction from a university professor, an AI specialist, and a professional programmer. Written to [`reference/perspectives.md`](./.claude/skills/daily-ai-news/reference/perspectives.md).
4. **Rewrite.** Weaves the three angles into each story as prose, appends an **Action items** section.
5. **Commit.** Uses the GitHub connector (no git CLI) to create `articles/YYYY-MM-DD-brief.md` on `main`. Commit message: `brief: {TOPIC} YYYY-MM-DD`.
6. **LINE.** Sends a TL;DR via `WebFetch` POST to `api.line.me/v2/bot/message/push`. Link in the message is pinned to the commit SHA, not a branch.

Full contract: [`.claude/skills/daily-ai-news/SKILL.md`](./.claude/skills/daily-ai-news/SKILL.md).

## Guardrails (enforced in SKILL.md)

- **Routine-compatible only.** No `Bash`, no shell, no `git` CLI, ever. If the tool isn't on the allow-list in the skill, don't use it.
- **GitHub connector missing → abort.** The skill refuses to run without commit capability and logs why.
- **LINE env missing → skip cleanly.** Commit still happens; LINE step is no-op.
- **LINE API non-200 or egress-blocked → loud failure.** Status/reason is printed; a `🔕 LINE not delivered` marker is appended to the committed article; no retry.
- **No fabricated URLs.** Every cited URL is either fetched (Tier 1) or present in a live `WebSearch` result for a trusted-source domain (Tier 2). A URL never appears unless a search engine also returned it.
- **Verification mode is visible.** Commit messages include `[verify=webfetch]` or `[verify=search]`; when the whole runtime is egress-blocked (`WEBFETCH_BLOCKED`), the article itself carries a banner.
- **Idempotent.** Re-runs on the same day don't duplicate: identical content is a NO-OP, different content updates via SHA.
- **Timezone is `Asia/Bangkok`** everywhere the date is computed.

## Running in Claude Web Routine

### 1. Push this repo to GitHub

You are reading the finished repo. If you're setting up your own fork, make sure `articles/` exists and `.claude/skills/daily-ai-news/` is committed to the default branch — that's where Claude will look for skills when it opens the repo.

### 2. Connect the GitHub MCP connector

In Claude (web): **Settings → Connectors → GitHub → Connect**, then authorize access to the repo you want the brief committed into. The connector exposes tools like `create_or_update_file` that the skill calls in Step 5.

Without this connector, Step 0 of the skill aborts on purpose.

### 3. Set environment — two surfaces, two purposes

**A. Routine config (for the skill that writes the brief):**

The skill only needs three GitHub-identity vars. It reads them in this order:

1. Inline in the invocation prompt (e.g. `GITHUB_OWNER = thannob`).
2. [`defaults.json`](./.claude/skills/daily-ai-news/reference/defaults.json) — committed fallback.

| Var | Example | Required | Where |
|---|---|---|---|
| `GITHUB_OWNER` | `thannob` | yes | prompt or `defaults.json` |
| `GITHUB_REPO` | `dailyainews` | yes | prompt or `defaults.json` |
| `GITHUB_BRANCH` | `main` | no (default `main`) | prompt or `defaults.json` |

Cloud Environment on the Routine is **not required** — `defaults.json` covers the fallback. In this deployment we observed Cloud Environment does not inject values into the model's prompt context, so we don't depend on it.

**B. GitHub repo secrets (for the Actions workflow that sends LINE):**

| Secret | Example | Where to set |
|---|---|---|
| `LINE_CHANNEL_ACCESS_TOKEN` | long-lived channel token from [LINE Developers Console](https://developers.line.biz/console/) | **Repo → Settings → Secrets and variables → Actions → New repository secret** |
| `LINE_TO` | `Uxxxxxxxxxxxxxxxxxxxxxxx` (userId/groupId/roomId) | same place |

The workflow at [`.github/workflows/line-notify.yml`](./.github/workflows/line-notify.yml) reads these directly. If either secret is missing, the workflow emits a warning and exits cleanly — commits still land, just no LINE push.

See [`.env.example`](./.env.example) for inline notes on each var.

### 4. Create the Routine

1. In Claude web, go to **Routines → New Routine**.
2. Attach this repo (the GitHub connector must already be authorized for it).
3. Set the schedule — suggested: **every day at 06:30 Asia/Bangkok**.
4. Paste the prompt:
   > Run the `daily-ai-news` skill. Today is the scheduled daily brief.
5. Save. The first run is the best sanity check.

### 5. What you get

Each run produces:

- A new commit on `main` in this repo: `articles/YYYY-MM-DD-brief.md`, message `brief: {TOPIC} YYYY-MM-DD`.
- Regenerated working artifacts at `reference/sources.md` and `reference/perspectives.md` (also committed, via the same or a separate commit depending on the connector).
- If LINE is configured: a push message containing headline + 3 TL;DR bullets + a permalink pinned to that commit's SHA (so the link never drifts if history is rewritten).

## Running it interactively in Claude Code

You can also invoke the skill from a local Claude Code session — same flow, same guardrails. The same GitHub connector and env vars are required. Open this repo in Claude Code and ask:

> run the daily-ai-news skill

Claude will load [`SKILL.md`](./.claude/skills/daily-ai-news/SKILL.md) and execute the seven steps.

## Diagnosing LINE issues

LINE delivery happens in GitHub Actions, not in Claude, so diagnose it there:

```bash
# Manually fire the workflow against any existing brief
gh workflow run line-notify.yml -f file=articles/<YYYY-MM-DD>-brief.md

# Watch / inspect
gh run list --workflow=line-notify.yml --limit 5
gh run view <run-id> --log
```

The workflow log shows the masked payload, the HTTP status, and the response body. The status-code mapping (`401` = token bad, `400 The property, 'to'` = `LINE_TO` bad, `200` + no message = bot not added to target, etc) is documented in [`.claude/skills/line-test/SKILL.md`](./.claude/skills/line-test/SKILL.md).

## Troubleshooting

- **"GitHub connector is not connected" on every run.** The connector authorization expired or was scoped to a different repo. Reconnect in **Settings → Connectors** and re-authorize for this repo.
- **Commit lands but no LINE message.** LINE is dispatched by `.github/workflows/line-notify.yml` — check the Actions tab of the repo, not the Routine log. If the workflow didn't even fire, the push may have been a NO-OP (skill detected identical content and skipped the commit — intentional).
- **Workflow ran but returned non-200.** Look at the run log — it prints the masked payload, status code, body, and `x-line-request-id`. Status-code mapping is in [`.claude/skills/line-test/SKILL.md`](./.claude/skills/line-test/SKILL.md).
- **Every WebFetch returns 403 from a single Routine run.** May be a transient tool issue; the skill auto-falls-back to `WEBFETCH_BLOCKED` (Tier 2 — WebSearch snippets), commits with `[verify=search]`, and the article carries a banner saying so. If it's persistent across many runs, the fix is at the Routine platform level (egress policy / `WebFetch` schema), not the skill.
- **`WebFetch` tool signature is `(url, prompt)` only — can't POST.** Not a bug. That's the tool shape in Claude Web Routine. Anything requiring POST with custom headers (like LINE) must live outside the Routine — see the GH Actions workflow.
- **"No verifiable stories" in sources.md.** Means `WebSearch` returned zero usable snippets from trusted-source domains too. Genuinely quiet news day or search quota issue. Re-run later; don't loosen [`reference/trusted-sources.md`](./.claude/skills/daily-ai-news/reference/trusted-sources.md) just to fill the quota.
- **The brief repeats yesterday's stories.** Check `Published:` in [`reference/sources.md`](./.claude/skills/daily-ai-news/reference/sources.md). Tier-2 stories derive the date from the search snippet, which can be stale on slow news days.

## License

No license chosen yet. Treat as all-rights-reserved until a `LICENSE` file lands.
