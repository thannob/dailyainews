# Sources — 2026-09-06

Generated: 2026-09-06 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-09-05-brief.md (4 URLs loaded)

Yesterday's URL set (`YESTERDAYS_URLS`):
- https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/
- https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/
- https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/
- https://www.blognone.com/node/151543

## Selected

_None._ Zero candidates passed BOTH Filter A (rolling-24h freshness) AND Filter B (URL not in yesterday's brief). The empty-day signal is preserved intentionally — see Step 1b-tris of the skill (never bend Filter A).

## Dropped

- https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/ — Filter A (>24h): URL slug `/2026/09/03/…` = ~3 days old
- https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/ — Filter A (>24h): search snippet dated announcement Sept 2–3, 2026 (~3 days old)
- https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/ — Filter A (>24h): URL slug `/2026/09/03/…` = ~3 days old
- https://openai.com/index/gpt-6-astra/ — Filter A (>24h): search snippets confirm Sept 3, 2026 release (~3 days old)
- https://deepmind.google/science/weathernext/ — Filter A (>24h): TechCrunch launch article `/2026/09/03/…` = ~3 days old
- https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/ — Filter A (>24h): URL slug `/2026/09/04/…` — outside the strict rolling-24h window from Asia/Bangkok now
- https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/ — Filter A (>24h): URL slug `/2026/09/04/…` — outside rolling-24h
- https://techcrunch.com/2026/09/03/abliteration-ai-is-making-a-business-out-of-removing-ai-guardrails/ — Filter A (>24h): URL slug `/2026/09/03/…`
- https://www.anthropic.com/research/formalizing-fermats-last-theorem — Filter A (>24h): search snippet ("The announcement was published September 4, 2026 and updated September 5, 2026") — original publish is >24h; the Sept 5 update alone does not reset the publish timestamp per the strict rule
- https://www.blognone.com/node/151533 — Filter A (>24h): node number precedes yesterday's already-covered node 151543 — published before Sept 4
- https://www.blognone.com/node/151552 — Filter A (ambiguous): no explicit publish timestamp surfaced in search snippet; node-number heuristic ("later than yesterday's 151543") is not proof of within-24h publication → drop per "Date ambiguous / not surfaced ❌ drop (do not guess)"
- Reuters "Exclusive-Anthropic IPO launch shifts toward mid-October" (Sept 5) — Not selectable: **no reuters.com URL appeared in any WebSearch result** (only aggregators: CNBC, The Star, Japan Times, Investing.com, Seeking Alpha). Skill rule: "Never cite a URL that you could not at least see in a WebSearch result for a trusted-source domain."
- CNBC / The Motley Fool / Bloomberg-hosted URLs for Anthropic-IPO-shift and AMD-Anthropic-$5B stories — publishers not on `reference/trusted-sources.md` allow-list

## Breakdown

- Candidates evaluated (trusted-source URLs seen in WebSearch results): ~12
- Failed Filter A (>24h publish): ~10
- Failed URL-not-in-search-results rule (trusted source but URL not surfaced): 1 (Reuters IPO story)
- Failed "date ambiguous → drop": 1 (Blognone node 151552)
- Passed both Filter A and Filter B: **0**

> Note: 0 items passed both filters this run. Of ~12 candidates, ~11 failed Filter A (freshness), 0 failed Filter B (dedup) — Filter A alone blocked the day. Runtime was `WEBFETCH_BLOCKED`, so all verification was Tier-2 (WebSearch snippet only); no candidate could be uplifted to Tier 1.
