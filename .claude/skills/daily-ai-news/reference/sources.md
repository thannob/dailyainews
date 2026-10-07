# Sources — 2026-10-07

Generated: 2026-10-07 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-10-06-brief.md (3 URLs loaded)

## Selected (0)

_No story cleared both Filter A (within 24h) and Filter B (not in YESTERDAYS_URLS) with Tier 2 confidence._

## Dropped

- https://techcrunch.com/?p=3106990 ("The public opposition to AI infrastructure is heating up" — Lucas Ropek) — Filter A ambiguous: search snippet labeled "4 hours ago" / "within the last 24 hours", but cross-referencing the article's described content ("boiling point in early 2026", 70% opposition stat) against other coverage shows the storyline predates the 24h window. In this runtime WebFetch is blocked, so an authoritative publishedTime cannot be read. Timestamp signal insufficient.
- https://techcrunch.com/?p=3096961 ("The White House wants AI companies to cover rate hikes" — Tim Fernholz) — Filter A fail: a follow-up search surfaced "appears to have been published in February 2026" alongside the Rate Payer Protection Pledge (signed March 6, 2026). Snippet freshness cue proven unreliable for this cluster.
- https://techcrunch.com/?p=3091795 ("OpenAI policy exec who opposed chatbot's 'adult mode' reportedly fired on discrimination claim") — Filter A fail: WSJ-sourced reporting and multiple confirming outlets (TechSpot, Storyboard18, Newsweek) place the firing in January 2026; snippet "7 hours ago" is clearly stale metadata.
- Boston Dynamics CEO Robert Playter steps down — Filter A fail: robotics247 and The Robot Report confirm the step-down was announced for February 27, 2026.
- xAI $20B Series E / $230B valuation — Filter A fail: TheWeek, Techzine, SeekingAlpha date this round to January 2026.
- Apple Siri AI French/Japanese/Korean/Portuguese/Spanish rollout — Filter A ambiguous: snippets say "October 2026" and "expected to arrive before October ends" — no confirmed launch within the 24h window.
- Marvell Investor Day (October 6, 2026, NYC) — Scheduled date lands in the window, but no trusted-sources.md domain (TechCrunch, Reuters, Bloomberg, The Verge, FT, Wired, Ars Technica, MIT Tech Review, The Information, Thai outlets) surfaced same-day reporting on the actual presentation; businesswire/01net coverage is on the pre-event announcement, which is not a 24h-fresh news event.
- Anthropic withholding model from UK testers / Anthropic IPO mid-November shift — Filter A fail: dated Oct 1–2, 2026 (5–6 days ago), outside the 24h rolling window.

> Note: 0 items passed both filters this run. Of ~8 candidates surfaced, all failed Filter A (freshness). Filter B (dedup against YESTERDAYS_URLS) was not the binding constraint — none of the dropped URLs overlapped yesterday's set, but none could satisfy the 24h gate under WEBFETCH_BLOCKED tier-2-only verification either.
