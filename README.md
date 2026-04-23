# dailyainews

A Claude Code skill that produces **one Thai-language AI news brief per day**, commits it to this repo, and pings a LINE chat with the TL;DR.

The entire flow is executable from inside Claude — **no shell, no git CLI, no cron on your laptop**. The intended host is [Claude Web Routine](https://claude.ai), so it survives your machine being asleep.

```
06:30 Asia/Bangkok  ──▶  Claude Routine fires  ──▶  WebSearch + WebFetch (5 stories)
                                                        │
                                                        ▼
                                               draft → 3 perspectives → rewrite
                                                        │
                                                        ▼
                                          GitHub MCP connector commits
                                          articles/YYYY-MM-DD-brief.md
                                                        │
                                                        ▼
                                     WebFetch POST https://api.line.me/v2/bot/message/push
```

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
- **LINE API non-200 → loud failure.** Status and response body are printed; the skill does **not** retry silently.
- **No fabricated URLs.** Every cited link is fetched and verified before it lands in the article.
- **Timezone is `Asia/Bangkok`** everywhere the date is computed.

## Running in Claude Web Routine

### 1. Push this repo to GitHub

You are reading the finished repo. If you're setting up your own fork, make sure `articles/` exists and `.claude/skills/daily-ai-news/` is committed to the default branch — that's where Claude will look for skills when it opens the repo.

### 2. Connect the GitHub MCP connector

In Claude (web): **Settings → Connectors → GitHub → Connect**, then authorize access to the repo you want the brief committed into. The connector exposes tools like `create_or_update_file` that the skill calls in Step 5.

Without this connector, Step 0 of the skill aborts on purpose.

### 3. Set environment variables on the Routine

The skill resolves each variable through a **3-tier order** (Step 0 in [`SKILL.md`](./.claude/skills/daily-ai-news/SKILL.md)):

1. **Cloud Environment** on the Routine — injected system context, template substitution like `{{LINE_TO}}`, or an env-reading MCP tool.
2. **Inline in the invocation prompt** — e.g. the prompt says `LINE_CHANNEL_ACCESS_TOKEN = xxx` directly.
3. **`reference/defaults.json`** — committed, **non-secret only** (`GITHUB_OWNER`, `GITHUB_REPO`, `GITHUB_BRANCH`). Secrets MUST NOT go here.

| Var | Example | Required | Best tier |
|---|---|---|---|
| `GITHUB_OWNER` | `thannob` | yes | Cloud Env or defaults.json |
| `GITHUB_REPO` | `dailyainews` | yes | Cloud Env or defaults.json |
| `GITHUB_BRANCH` | `main` | no (default `main`) | Cloud Env or defaults.json |
| `LINE_CHANNEL_ACCESS_TOKEN` | `xxxx...` from [LINE Developers Console](https://developers.line.biz/console/) | no | **Cloud Env** (fallback: prompt) |
| `LINE_TO` | `Uxxxxxxxxxxxxxxxxxxxxxxx` (userId from the bot's webhook) | no | **Cloud Env** (fallback: prompt) |

**Setting Cloud Env for a Routine:** in the Routine editor, open the **Cloud Environment** panel and add each key/value. Save before running. Key names are case-sensitive (`LINE_CHANNEL_ACCESS_TOKEN`, not `line_channel_access_token`).

**Gotcha:** Cloud Env values reach the model differently across Routine platforms — sometimes as injected system context, sometimes via template substitution, sometimes only via shell (which we don't have). Step 0 prints a resolution table showing the actual source each var was resolved from, so you can tell at a glance whether Cloud Env worked or it fell through to defaults.

If either LINE var is absent from all tiers, the skill commits but skips the notification — intentional so you can roll out the GitHub half first.

See [`.env.example`](./.env.example) and [`defaults.json`](./.claude/skills/daily-ai-news/reference/defaults.json) for inline notes.

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

## Diagnosing LINE issues with `line-test`

There's a companion skill at [`.claude/skills/line-test/SKILL.md`](./.claude/skills/line-test/SKILL.md) that does **only** the LINE push — no research, no GitHub. Use it when `daily-ai-news` reports `LINE: skipped` or a non-200 and you need to isolate whether the problem is the env wiring, the token, or the target id.

To run it:

1. In any Claude session with the `ClaudeBot_Line` Cloud Environment attached, say:
   > run the line-test skill
2. Watch the output. Success is **all three**:
   - Env resolution table shows both LINE vars `(source: cloud-env / ClaudeBot_Line)`.
   - `status = 200` from `api.line.me`.
   - The test message actually arrives in your LINE client.
3. If any of those three fails, the skill prints a classification table that maps the failure to the most likely cause (wrong token, wrong `LINE_TO`, bot not added to the group, etc).

If `line-test` passes and `daily-ai-news` still skips LINE, that's a `daily-ai-news` Step 0 bug — file it, don't keep running the full news flow blindly.

## Troubleshooting

- **"GitHub connector is not connected" on every run.** The connector authorization expired or was scoped to a different repo. Reconnect in **Settings → Connectors** and re-authorize for this repo.
- **Commit lands but no LINE message.** Check the Routine log — the skill prints `LINE: skipped (env missing)` or `LINE ERROR: status=... body=...` verbatim. No retries happen by design.
- **The brief repeats yesterday's stories.** The 24h freshness check is against the publisher's own timestamp; stories republished on a new URL may re-surface. Tighten [`reference/trusted-sources.md`](./.claude/skills/daily-ai-news/reference/trusted-sources.md) or add a "recently seen URLs" note at the top of the skill run.
- **"No verifiable stories" in sources.md.** The skill refuses to fabricate — expected behavior when the news day is genuinely quiet or when `WebFetch` is being blocked by a source. Re-run in a few hours or allow-list another publisher.

## License

No license chosen yet. Treat as all-rights-reserved until a `LICENSE` file lands.
