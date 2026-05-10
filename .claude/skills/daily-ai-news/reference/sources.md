# Sources — 2026-05-10

Generated: 2026-05-10 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (probe to https://example.com returned HTTP 403)
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-05-09-brief.md (4 URLs loaded)

1. **Nvidia has already committed $40B to equity AI deals this year**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/05/09/nvidia-has-already-committed-40b-to-equity-ai-deals-this-year/
   - Published: 2026-05-09 (URL slug); search snippet "TechCrunch on May 9, 2026 (9 hours ago from the search result timestamp)"
   - FreshnessCheck: ✅ within last 24h via URL slug `/2026/05/09/` AND snippet "9 hours ago"
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS (yesterday's TechCrunch URLs were /2026/05/08/airbnb..., /2026/05/08/cloudflare..., /2026/05/08/the-biggest-u-s-power-grid... — different paths)
   - Verification: Tier 2 — WebSearch snippet (WEBFETCH_BLOCKED)
   - Summary: Per CNBC reporting referenced by TechCrunch, Nvidia has committed more than $40B to equity investments in AI companies in the early months of 2026. Major commitments include up to $100B in OpenAI staged per gigawatt of deployment, $2.1B in data-center developer IREN announced May 7, and $2B each in optics firms Lumentum and Coherent announced March. Nvidia participated in ~67 venture deals in 2025, surpassing 54 in all of 2024.

2. **บลูมเบิร์กเผย สหรัฐฯ สงสัยไทยเป็นทางผ่านลักลอบส่งชิป Nvidia ให้ Alibaba ในจีน**
   - Publisher: Thairath (ไทยรัฐออนไลน์)
   - URL: https://www.thairath.co.th/news/foreign/2931581
   - Published: 2026-05-09 (search snippet: "สำนักข่าวบลูมเบิร์ก รายงานเมื่อวันที่ 9 พฤษภาคม 2569"); ranked #1 for query "ข่าว AI วันนี้ 9 พฤษภาคม 2026"
   - FreshnessCheck: ✅ within last 24h via snippet "รายงานเมื่อวันที่ 9 พฤษภาคม 2569" (= 2026-05-09)
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS (yesterday had no Thai-source URLs and no OBON/chip-smuggling story)
   - Verification: Tier 2 — WebSearch snippet (WEBFETCH_BLOCKED)
   - Summary: Bloomberg-sourced reporting that the U.S. suspects a Thai company tied to Thailand's national AI initiative helped ship Super Micro servers containing advanced Nvidia chips to China, with Alibaba as one of multiple end customers. The intermediary, called "Company-1" by U.S. prosecutors, has been identified by Bloomberg as Bangkok-based OBON Corp; total value of servers forwarded to Alibaba reportedly ~$2.5B (~80,000 ล้านบาท). Super Micro's co-founder and a contractor have been indicted for conspiring to divert servers containing Nvidia chips to China. Alibaba denies any business relationship with Super Micro, OBON, or any third-party brokers in the indictment, and says it has never used banned Nvidia chips in its data centers. OBON is the supplier of servers to Siam AI Cloud, Thailand's first NVIDIA Cloud Partner.

## Dropped

- https://www.bloomberg.com/news/articles/2026-05-08/us-said-to-suspect-nvidia-chips-smuggled-to-alibaba-via-thailand — Filter A (URL slug 2026-05-08 = ~36–48h, beyond 24h). Same story is covered via Thairath (item 2 above) which has a 2026-05-09 timestamp.
- https://www.bloomberg.com/news/articles/2026-05-08/anthropic-inks-1-8-billion-computing-deal-with-akamai — Filter B (this exact URL was in articles/2026-05-09-brief.md as Story #4)
- https://www.bloomberg.com/news/newsletters/2026-05-08/ai-power-use-risks-blowing-up-for-governments — Filter A (slug 2026-05-08 + topical overlap with yesterday's PJM grid story)
- https://www.bloomberg.com/news/articles/2026-05-07/nvidia-to-invest-up-to-2-1-billion-in-data-center-firm-iren — Filter A (slug 2026-05-07 = ~3 days)
- https://www.bloomberg.com/news/articles/2026-05-07/anthropic-is-making-claude-chatbot-more-appealing-to-consumers — Filter A (slug 2026-05-07)
- https://www.bloomberg.com/news/articles/2026-05-06/anthropic-inks-computing-deal-with-spacex-to-meet-ai-demand — Filter A (slug 2026-05-06)
- https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/ — Filter A (slug 2026-05-05)
- https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/ — Filter A (slug 2026-05-04)
- https://www.bloomberg.com/news/videos/2026-05-08/bloomberg-tech-5-8-2026-video — Filter A (slug 2026-05-08)
- https://www.blognone.com/node/150485 (Thai OBON coverage) — date not surfaced in any snippet (numeric node ID, no slug date); to avoid guessing, used Thairath instead which has explicit "9 พฤษภาคม 2569" in the snippet.
- https://www.prachachat.net/ict/news-2004475 (อิสริยะ ตั้ง 6 คำถามถึง OBON) — date not surfaced in snippet; same reason as above.

> Note: 2 items passed both filters this run. Of ~12 candidates evaluated, 9 failed Filter A (publish date > 24h, mostly slugs 2026-05-04 to 2026-05-08), 1 failed Filter B (Akamai-Anthropic URL was already in yesterday's brief), and 2 were dropped due to ambiguous timestamps in the snippets even though the underlying story was timely.
