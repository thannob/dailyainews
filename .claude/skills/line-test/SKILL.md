---
name: line-test
description: Diagnostic pointer for LINE push testing. Tells the caller that LINE delivery is handled by the GitHub Actions workflow `.github/workflows/line-notify.yml`, not by any Claude skill — because `WebFetch` in Claude Web Routine cannot issue POST requests with Bearer auth. Use when the user asks "test LINE", "ทดสอบส่ง LINE", or why LINE isn't being sent from the skill.
---

# line-test (redirect)

**This skill does not send anything.** An earlier iteration tried to POST to `api.line.me/v2/bot/message/push` via `WebFetch`, but the `WebFetch` tool in Claude Web Routine accepts only `(url, prompt)` — no method, no headers, no body — so POST with `Authorization: Bearer ...` is impossible from any Claude skill in that runtime.

LINE delivery was moved to GitHub Actions: [`.github/workflows/line-notify.yml`](../../../.github/workflows/line-notify.yml).

## How to test LINE end-to-end

Pick whichever path is cheaper right now:

### A. Manually trigger the workflow

```bash
gh workflow run line-notify.yml -f file=articles/<some-existing-brief>.md
gh run watch
```

The run log will show the masked payload, the HTTP status, the body, and the `x-line-request-id`. If it returns `200`, LINE accepted the push — check your LINE client.

### B. Force a real push

Commit any change to an `articles/*-brief.md` file on `main` (the daily Routine run does this naturally). The `on.push` trigger fires immediately; watch it in the Actions tab.

### C. Read the workflow output for the last run

```bash
gh run list --workflow=line-notify.yml --limit 1
gh run view <run-id> --log
```

## What each status means

| Status | Meaning | Fix |
|---|---|---|
| `200` + message arrives | Working | — |
| `200` + no message | Bot not added to the user / group that `LINE_TO` points at | Add the bot as a friend (1:1) or invite it to the group |
| `401 Invalid channel access token` | Token expired / wrong channel | Reissue in LINE Developers Console; update `LINE_CHANNEL_ACCESS_TOKEN` in repo secrets |
| `400 The property, 'to'` | `LINE_TO` wrong or empty | Set it to a real userId (`U...`), groupId (`C...`), or roomId (`R...`) |
| `403` | Channel type mismatch | The token belongs to a LINE Login channel, not a Messaging API channel |
| `429` | Rate limited / monthly quota hit | Don't retry — wait it out or upgrade the plan |
| `5xx` | LINE platform issue | Don't retry in this run — try later |

## Where the secrets live

- `LINE_CHANNEL_ACCESS_TOKEN` — GitHub repo **Settings → Secrets and variables → Actions → New repository secret**
- `LINE_TO` — same place

Not in `.env.example`, not in `reference/defaults.json`, not in any skill — they only exist on the GitHub secret store and reach the workflow runner as env vars at run time.
