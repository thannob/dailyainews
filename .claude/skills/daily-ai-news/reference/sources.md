# Sources — 2026-05-12

Generated: 2026-05-12 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED (probe to https://example.com returned HTTP 403)
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-05-11-brief.md (2 URLs loaded)

YESTERDAYS_URLS:
- https://techcrunch.com/2026/05/10/were-feeling-cynical-about-xais-big-deal-with-anthropic/
- https://techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/

---

1. **OpenAI launches the OpenAI Deployment Company (US$4B, TPG-led, 19 partners)**
   - Publisher: OpenAI
   - URL: https://openai.com/index/openai-launches-the-deployment-company/
   - Published: 2026-05-11 (cross-corroborated by Axios URL `axios.com/2026/05/11/openai-deployco-private-equity` and search synthesis "3 hours ago")
   - FreshnessCheck: ✅ within last 24h via "search snippet '3 hours ago' + Axios URL slug 2026/05/11"
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS (openai.com host not in yesterday's brief)
   - Verification: Tier 2 — WebSearch snippet (openai.com is on trusted-sources.md "International — primary / research")
   - Summary: OpenAI launched the OpenAI Deployment Company with US$4B initial funding from 19 partners (TPG-led; Advent, Bain Capital, Brookfield as co-leads). The new entity will help enterprises build and deploy AI systems and acquires applied-AI consultancy Tomoro, bringing ~150 Forward Deployed Engineers and Deployment Specialists.

2. **OpenAI for Healthcare — HIPAA-compliant ChatGPT for hospitals**
   - Publisher: OpenAI
   - URL: https://openai.com/index/openai-for-healthcare/
   - Published: 2026-05-11 ("starting today" in OpenAI's announcement, same-day batch as the Deployment Company launch)
   - FreshnessCheck: ✅ within last 24h via "snippet 'available starting today' + same OpenAI batch as Deployment Company (2026-05-11)"
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS
   - Verification: Tier 2 — WebSearch snippet (openai.com is trusted)
   - Summary: ChatGPT for Healthcare is now rolling out to AdventHealth, Baylor Scott & White Health, Boston Children's Hospital, Cedars-Sinai, HCA Healthcare, Memorial Sloan Kettering, Stanford Medicine Children's Health, and UCSF. It supports HIPAA-compliant deployment with data residency, audit logs, customer-managed encryption keys, and a BAA with OpenAI; content shared with ChatGPT for Healthcare is not used to train models.

3. **OpenAI brings ChatGPT Go (US$8/month) to the US plus ads in Free / Go tiers**
   - Publisher: OpenAI
   - URL: https://openai.com/index/our-approach-to-advertising-and-expanding-access/
   - Published: 2026-05-11 (same batch as Deployment Company / Healthcare; corroborated by PYMNTS 2026 article "OpenAI Brings Subscription Tier and Ads to US" and Geeky Gadgets "ChatGPT Go at $8 per Month in US, Now in 171 Countries")
   - FreshnessCheck: ✅ within last 24h via "same-day OpenAI batch as items #1 and #2 (2026-05-11) + multiple mirror sites with matching launch substance"
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS
   - Verification: Tier 2 — WebSearch snippet (openai.com is trusted)
   - Summary: ChatGPT Go is now in 171 countries including the US at US$8/month, adding GPT-5.2 Instant and 10× the messages of the Free tier. To sustain the lower-cost tier, OpenAI introduced advertisements in the Free and Go tiers and laid out its approach to ad integration and access expansion.

4. **Digg returns as an AI-driven news aggregator powered by X engagement signals**
   - Publisher: TechCrunch
   - URL: https://techcrunch.com/2026/05/11/digg-tries-again-this-time-as-an-ai-news-aggregator/
   - Published: 2026-05-11 (URL slug; mirrored by Slashdot story id `26/05/11/2040256`)
   - FreshnessCheck: ✅ within last 24h via "URL slug 2026/05/11 + Slashdot mirror 26/05/11"
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS
   - Verification: Tier 2 — WebSearch snippet (techcrunch.com is trusted)
   - Summary: Kevin Rose previewed a new Digg positioned as an AI-driven news aggregator instead of a Reddit-style community, after the previous reboot folded in March under bot-traffic problems. The site ingests X content in real time and applies sentiment analysis, clustering, and signal detection; the homepage surfaces "most viewed", "rising discussion", "fastest-climbing", and "in case you missed it" — starting with the AI vertical and (if it works) expanding to other topics.

---

## Dropped

- https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html — Filter A pass (~13h ago), but Filter S (source) fails: cnbc.com is not on trusted-sources.md.
- https://www.businesstoday.in/amp/technology/story/openai-anthropic-turn-to-hindu-sikh-christian-leaders-to-teach-ai-morality-530806-2026-05-11 — Filter A pass, but businesstoday.in is not on trusted-sources.md.
- TechCrunch follow-up on the Anthropic blackmail / Claude alignment research (URL `techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/`) — Filter B (dedup): already covered in articles/2026-05-11-brief.md.
- TechCrunch xAI–Anthropic Colossus deal (URL `techcrunch.com/2026/05/10/were-feeling-cynical-about-xais-big-deal-with-anthropic/`) — Filter B (dedup): already covered in articles/2026-05-11-brief.md.
- OpenAI voice-intelligence API models (https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) — Filter A ambiguous: TechCrunch coverage is dated 2026/05/07 (>24h), but a gHacks mirror URL slug is 2026/05/11. Cannot resolve which date the openai.com canonical post bears without WebFetch. Drop per "ambiguous timestamp → drop".
- TechCrunch Helsing defense funding (https://techcrunch.com/2026/05/11/daniel-ek-backed-defense-tech-helsing-to-raise-1-2b-at-18b-valuation/) — Within 24h and on a trusted domain, but the snippet does not establish AI as the primary angle (defense-tech funding round, AI is incidental); skipped to keep the brief AI-focused.

> Note: 4 items passed both filters this run. Of ~10 candidates seriously considered, 2 failed source-trust (cnbc, businesstoday.in), 2 failed Filter B (already in 2026-05-11 brief), 1 was AI-tangential, and 1 had ambiguous timestamps.
