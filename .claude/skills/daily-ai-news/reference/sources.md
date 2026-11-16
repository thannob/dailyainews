# Sources — 2026-11-16

Generated: 2026-11-16 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-11-15-brief.md (5 URLs loaded)

**No stories qualified for inclusion this run.**

## Diagnosis

- **Filter A (24h fresh):** blocks everything. Every URL from `reference/trusted-sources.md` that WebSearch surfaced today is ≥4 days old (TechCrunch Nov 10/12, The Information briefings Nov 5–10, DeepMind Nov 10, siliconangle Nov 11, nvidianews from 2025, etc.). Fresh Nov 15/16 items were visible only in aggregators outside the allow-list (Yahoo Finance, CNBC, Fox Business, FourWeekMBA, 404kresearch, aiweekly.co, cryptobriefing, etc.).
- **Filter B (dedup):** not reached — nothing survived Filter A to be dedup-checked.

## Candidates reviewed and dropped

- `techcrunch.com/2026/11/12/jensen-huang-is-out-at-nvidia-who-is-colette-kress-his-interim-replacement/` — Filter A (>24h): URL slug 2026/11/12 is 4 days old
- `techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/` — Filter A: 6 days old
- `techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/` — Filter B: in YESTERDAYS_URLS
- `techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/` — Filter B: in YESTERDAYS_URLS
- `techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/` — Filter B: in YESTERDAYS_URLS
- `bloomberg.com/news/articles/2026-11-14/ai-tools-huang-championed-now-star-in-memes-of-his-downfall` — Filter B: in YESTERDAYS_URLS
- `blognone.com/node/152177` — Filter B: in YESTERDAYS_URLS
- `deepmind.google/blog/formal-verification-signal-protocol` — Filter A: Nov 10, 2026, 6 days old
- `theinformation.com/briefings/report-nvidia-board-reportedly-preparing-oust-nvidia-ceo` — Filter A: Nov 10, 6 days old
- `cnbc.com/2026/11/13/nvidia-huang-ceo-replacement-search.html` — cnbc.com not in trusted-sources.md + Filter A (3 days)
- `finance.yahoo.com/.../jensen-huang-discusses-comeback-nvidia-192628314.html` — yahoo.com not in trusted-sources.md (snippet dated Nov 15)
- `fourweekmba.com/ai-daily-roundup-15-nov-2026-bessent-nvidia-board-10-days` — not in trusted-sources.md (snippet Nov 15 — Bessent remarks)
- `aiweekly.co/ai-news-today` — not in trusted-sources.md (snippet Nov 15 roundup)
- `siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/` — not in trusted-sources.md + Filter A (5 days)
- FT report on Huang discussing comeback as Nvidia CEO (Nov 15, Asia/Bangkok) — **no ft.com URL surfaced in WebSearch results**, only aggregator citations
- Reuters coverage of Nvidia/OpenAI Ohio data-center guarantee revision (Nov 15) — **no reuters.com URL in results**

## Runtime notes

- WebFetch probe (`example.com`, `techcrunch.com`) returned `ENOTFOUND` across all attempts → whole runtime is `WEBFETCH_BLOCKED`. Only Tier 2 was available.
- Tier 2 strictly requires the URL on a trusted-sources.md domain **appearing in a WebSearch result** together with a timestamp resolvable to TODAY. Search snippets today mentioned trusted-source outlets (FT, Reuters, Bloomberg) as citations, but the actual result URLs returned were aggregator domains, not the primary site. Under the skill's hard anti-bending rule, the FT/Reuters/Bloomberg Nov 15 stories therefore cannot be cited.

> Note: 0 items passed both filters this run. Of ~20 candidates reviewed, all failed Filter A (timestamp >24h for trusted-source URLs, or Nov 15 content only reachable via non-trusted aggregator URLs). Filter B blocked 5 duplicates from yesterday's brief but those also failed Filter A.
