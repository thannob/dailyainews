---
name: line-test
description: Send a single test message to LINE via the Messaging API push endpoint. Use this to verify end-to-end that `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_TO` in the `ClaudeBot_Line` Cloud Environment actually reach the runtime and that LINE accepts the push. Invoke when the user says "test LINE", "ทดสอบส่ง LINE", "verify LINE integration", or when daily-ai-news reports `LINE: skipped` and you need to isolate whether it's an env issue or a LINE API issue.
---

# line-test

**One purpose:** prove that this Routine can send a LINE push. Nothing else. No GitHub, no research, no articles.

Use this as the **first diagnostic** when LINE isn't working in `daily-ai-news`. If `line-test` fails, `daily-ai-news` Step 6 will fail the same way — fix it here first.

## Runtime contract

- **Tools allowed:** `WebFetch`, `Read`.
- **Forbidden:** `Bash`, shell, `git` CLI, any network tool other than `WebFetch`.
- **Cloud Environment expected:** `ClaudeBot_Line` (see [`../daily-ai-news/SKILL.md`](../daily-ai-news/SKILL.md) for env table).

## Step 1 — Resolve env

Walk the same 3-tier resolution as `daily-ai-news` for these two vars only:

- `LINE_CHANNEL_ACCESS_TOKEN`
- `LINE_TO`

Resolution order:
1. Cloud Environment (`ClaudeBot_Line` — injected context, substituted placeholders, or env-reading MCP tool).
2. Inline in the skill invocation prompt.
3. (There is no `defaults.json` fallback for these — they are secrets.)

Reject literal placeholder strings like `{{LINE_TO}}`, `<from Routine env>`, `$LINE_TO`, or `PASTE_REAL_TOKEN_HERE`.

Print a masked resolution table:

```
line-test env resolution (Cloud Environment: ClaudeBot_Line expected):
  LINE_CHANNEL_ACCESS_TOKEN = ***set*** (length=N, source: cloud-env / ClaudeBot_Line)
  LINE_TO                   = U******xxxx (first 2 + last 4 chars, source: cloud-env / ClaudeBot_Line)
```

If either is `***missing***` → print:
```
ABORT: <VAR_NAME> not resolvable. Confirm the Routine has the "ClaudeBot_Line" Cloud Environment attached and that the key name is spelled exactly as shown (case-sensitive).
```
and stop. Do not call LINE.

## Step 2 — Compose the test message

```
TODAY = <YYYY-MM-DD HH:mm in Asia/Bangkok>

text =
📡 line-test from daily-ai-news
Time: {TODAY}
If you can read this, LINE_CHANNEL_ACCESS_TOKEN and LINE_TO are wired correctly in the ClaudeBot_Line Cloud Environment. No commit was made by this run.
```

Keep it under 500 chars — LINE text messages cap at 5000 but the short version is cheaper for push quota.

## Step 3 — Call the LINE API

Use `WebFetch` with:

- **Method:** `POST`
- **URL:** `https://api.line.me/v2/bot/message/push`
- **Headers:**
  - `Authorization: Bearer {LINE_CHANNEL_ACCESS_TOKEN}`
  - `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "to": "{LINE_TO}",
    "messages": [
      { "type": "text", "text": "{text}" }
    ]
  }
  ```

If `WebFetch` in the current runtime does **not** support POST with custom headers, say so explicitly and stop — **do not fall back to GET**, that will not send a message.

## Step 4 — Report verbatim

Print exactly:

```
LINE test result:
  status = <HTTP status code>
  body   = <response body, verbatim, or "(empty)">
  x-line-request-id = <header value if present>
```

Then classify:

| Condition | Interpretation | Next step |
|---|---|---|
| `status = 200` | Message delivered to LINE platform | Check your LINE client — the message should arrive within a few seconds. |
| `status = 401` | Token rejected | Re-issue token in [LINE Developers Console](https://developers.line.biz/console/) → Channel → Messaging API tab → reissue; update `ClaudeBot_Line`. |
| `status = 400` with `Invalid reply token` / `Invalid user ID` | `LINE_TO` wrong | Must be a userId (`U...`), groupId (`C...`), or roomId (`R...`) that has sent a message to the bot. |
| `status = 400` with `The property, 'to'` | `LINE_TO` empty or mis-typed | Check the key name in `ClaudeBot_Line`. |
| `status = 403` | Token scope / channel mismatch | Confirm the token belongs to the Messaging API channel, not a LINE Login channel. |
| `status = 429` | Rate limit / monthly quota | Check the bot's quota in LINE console. Do NOT retry. |
| `status = 5xx` | LINE platform issue | Do NOT retry in this run. Try again manually later. |
| Non-200, anything else | Unclassified | Print the full body and stop. |

**Do not retry on any status.** The whole point of this skill is to surface the first response verbatim.

## What "verified" looks like

The skill succeeds only when **all three** are true:

1. Env resolution table shows both LINE vars resolved from `cloud-env / ClaudeBot_Line` (not `***missing***`, not `defaults.json`).
2. LINE API returned `status = 200`.
3. The user reports that the message actually arrived in their LINE client.

If #1 and #2 are true but #3 is not, the most likely cause is that `LINE_TO` points to a user/group the bot hasn't been added to — add the bot and retry.
