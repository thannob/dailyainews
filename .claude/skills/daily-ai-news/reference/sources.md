# Sources — 2026-10-28

Generated: 2026-10-28 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-10-27-brief.md (0 URLs loaded — yesterday was an empty stub)

## Selected (passed both filters)

วันนี้ไม่มีผู้สมัครที่ผ่านทั้ง Filter A (24 ชั่วโมงล่าสุด Asia/Bangkok) และข้อกำหนด Tier 2 (URL จากโดเมนใน `reference/trusted-sources.md` ปรากฏใน WebSearch snippet ของ skill รอบนี้) พร้อมกัน

## Dropped — candidates found but did not clear both gates

- **OpenAI "Three AI-assisted discoveries in math, CS, physics" (ETH false; local-smoothing conjecture; 4D QFT existence)**
  - Announced Mon 2026-10-26 (US time) → within 24h window (Filter A: ✅)
  - URL seen in search: only non-trusted aggregators — `aljazeera.com/economy/2026/10/27/...openai-says` (Al Jazeera, not on allow-list), `qz.com/openai-ai-discoveries-math-computer-science-physics-102726` (Quartz, not on allow-list), `unite.ai/.../three-proofs-in-math-cs-and-physics/` (not on allow-list), Techmeme listing mentions an `openai.com` post but the URL itself was not surfaced in search results on the trusted-sources domains.
  - Reason: Tier 2 requires the URL to appear in search snippets for a trusted-sources domain. The specific story URL on openai.com was not visible in my results — only generic index pages (`openai.com/news/`, `openai.com/news/research/`, `openai.com/research/index/release/`).
  - **DROP (Tier 2 — no trusted-domain story URL seen in search snippet).**

- **OpenAI "Introducing GPT-6.1 Terra" (Oct 26, 2026 — pricing $1/$5 per 1M tokens, "fast and capable computer use at scale")**
  - Date per Techmeme excerpt → within 24h window (Filter A: ✅ if confirmed)
  - URL seen in search: only Techmeme excerpt + third-party aggregators (datalearner.com, orcarouter.ai, pricepertoken.com, cloudprice.net). A direct `GPT-6.1 Terra OpenAI` search returned pages describing Terra as "尚未发布" (not yet released) with "placeholder" release dates.
  - **DROP (conflicting signals; no direct `openai.com` story URL in snippets).**

- **OpenAI "GPT-6.1 Sol helps CodeRabbit strengthen security"**
  - Techmeme excerpt lists an openai.com page dated Oct 26, 2026, but the specific URL did not appear in search results — only `openai.com/news/` category pages.
  - **DROP (Tier 2 — no story URL in search snippet).**

- **OpenAI "An in-depth look at how workers use ChatGPT"**
  - Same situation as above — Techmeme excerpt mentions it but no direct openai.com URL surfaced.
  - **DROP (Tier 2 — no story URL in search snippet).**

- **Anthropic — "Confidential draft S-1 to SEC" (`anthropic.com/news/confidential-draft-s1-sec`)**
  - Trusted-domain URL visible in search snippets ✅
  - Date: **2026-06-01** → ~5 months old (Filter A: ❌)
  - **DROP (Filter A — >24h old).**

- **OpenAI "Sharing AI progress in mathematics" / 722 math papers release (`openai.com/index/sharing-ai-progress-in-mathematics/`)**
  - Trusted-domain URL visible in search snippets ✅
  - Date: **2026-10-06 / 2026-10-07** → ~21 days old (Filter A: ❌)
  - Washington Post coverage dated 2026-10-07 (and WaPo is not on the allow-list anyway)
  - **DROP (Filter A — >24h old).**

- **Al Jazeera: "AI makes discoveries in mathematics, computer science, physics, OpenAI says" (`aljazeera.com/economy/2026/10/27/...`)**
  - URL slug dates it Oct 27 (within 24h window — Filter A: ✅)
  - Publisher is NOT on `reference/trusted-sources.md`
  - **DROP (trusted-sources allow-list — Al Jazeera not listed).**

- **Fox News: "Anthropic IPO filing reveals AI security breaches, training halt" (10-27-26 live-news URL)**
  - Not on `reference/trusted-sources.md`
  - **DROP (trusted-sources allow-list — Fox News not listed).**

- **Reuters-attributed story: China's Star 50 AI/chip index down ~40%**
  - Reuters IS on the allow-list, but `site:reuters.com` searches did not surface the specific story URL — only third-party coverage (Bloomberg Línea, newsbytesapp, The Edge Malaysia, Protos).
  - **DROP (Tier 2 — no `reuters.com` URL seen in search snippet).**

- **"Google DeepMind Genie 4 interactive world model" (per one aggregator live-feed snippet)**
  - `site:deepmind.google Genie 4` returned no results — only Genie 3 pages. A broader search also found only Genie 3 / Project Genie coverage.
  - **DROP (Tier 2 — not confirmed on deepmind.google; aggregator-only mention appears to conflate with the earlier Genie 3 lineage).**

- **Thai sources (Blognone, Beartai, Thairath, Matichon, Prachachat, The Standard)**
  - No AI stories dated within the last 24 hours surfaced in search for any of these domains. Most results are from July–October 2026 but older than the 24h window, or are non-dated tag/landing pages.
  - **DROP (Filter A — no fresh content).**

## Breakdown

- Candidates evaluated: ~11
- Failed Filter A (>24h old): 2 explicit (Anthropic S-1, OpenAI 722 papers) + the Thai-sources sweep
- Failed Tier 2 (trusted-domain URL not seen in WebSearch snippet, or publisher off the allow-list): the Oct 26/27 OpenAI announcements, Al Jazeera, Fox News, Reuters-China-Star-50, DeepMind Genie 4
- Failed Filter B (dedup): **0** — yesterday's brief was itself empty, so `YESTERDAYS_URLS = {}`

> Note: 0 items passed both gates this run. The dominant blocker is Tier 2 verification: the fresh (within-24h) stories that genuinely exist today — OpenAI's three-discoveries announcement, GPT-6.1 Terra, and related items — originate on `openai.com`, but their specific story URLs are not yet surfacing in search snippets for the trusted-sources allow-list. The skill's hard rule prohibits citing URLs that have not appeared in WebSearch results for a trusted domain, so these are dropped rather than guessed at.
