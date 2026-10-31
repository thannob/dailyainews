# Sources — 2026-10-31

Generated: 2026-10-31 (Asia/Bangkok)
Runtime: WEBFETCH_OK (partial — only anthropic.com และ microsoft.com เท่านั้นที่ resolvable; โดเมนอื่น ๆ ในรายการ allow-list ถูกบล็อกชั้น DNS/egress ใน Routine รอบนี้)
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-10-30-brief.md (0 URLs loaded — yesterday was an empty-day stub)

1. **From synthetic enterprise data evaluations to real Microsoft Copilot AI confidence**
   - Publisher: Microsoft Research
   - URL: https://www.microsoft.com/en-us/research/blog/from-synthetic-enterprise-data-evaluations-to-real-microsoft-copilot-ai-confidence/
   - Published: October 30, 2026
   - FreshnessCheck: ✅ within last 24h via explicit "October 30, 2026" byline on both the listing page และตัวโพสต์โดยตรง (WebFetch 2xx, body contains headline + date)
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS (yesterday's brief was a stub with 0 URLs)
   - Verification: Tier 1 — WebFetch (2xx on both the index page https://www.microsoft.com/en-us/research/blog/ และหน้าโพสต์เต็ม)
   - Summary: Microsoft Research แนะนำ "Industry Evaluation Data Generation Platform" ที่สร้างสภาพแวดล้อม enterprise สังเคราะห์ล้วน ๆ จากข้อมูลสาธารณะ (O*NET occupational data, job postings, SEC filings) เพื่อประเมิน Copilot โดยไม่ต้องแตะข้อมูลลูกค้า มี automated pipeline สร้าง industry-specific queries สำหรับ pharmaceutical / capital markets / IT & software พร้อม quality checks ครอบคลุม structure, relevance, behavioral realism, และ content safety ทีมผู้เขียนรายงานการเพิ่มคุณภาพข้อมูลสังเคราะห์ 39% และวางกรอบนี้ไว้เป็นฐานของ "trust" สำหรับ Copilot ขณะที่ขยับเข้าสู่ multi-step agentic workflows ผู้เขียน: Somya Chatterjee, Harshita Sahijwani, Min Chen, Sushmitha Rajeswari Muppa, Dayquan Julienne, Irene Shaffer, Chandra Inguva, Jenny Chen, Minha Hwang, Sam Ade Jacobs

## Dropped

- https://www.anthropic.com/claude-opus-5-5 — Filter A (ambiguous): featured card แสดง "October 31, 2026" ด้านบน แต่ markup ภายในการ์ดและรายการ news feed ของเพจเดียวกันระบุวันที่ "Sep 22, 2026" — เพจไม่ระบุชัดว่าวันไหนถูก จึงไม่สามารถยืนยัน 24h ได้
- Anthropic "AI for Science expands to foundations and research institutions" (Oct 28, 2026) — Filter A: 3 วันก่อน เกินกรอบ 24h
- NVIDIA–Meta Muse / Vera Rubin partnership extension (Oct 27, 2026 ตาม search snippet) — Filter A: 4 วันก่อน + ไม่มี URL จาก allow-list ปรากฏใน search results
- หลายรายการจาก search ที่ไม่ใช่โดเมน allow-list (cryptobriefing.com, toolnavs.com, ground.news, techradar.com ฯลฯ) — ตัดทั้งหมดเพราะไม่อยู่ใน reference/trusted-sources.md

> Note: 1 item passed both filters this run. Of ~8 candidates reviewed, 7 failed Filter A (เกิน 24h หรือ timestamp ambiguous), 0 failed Filter B.
> Infra note: Egress ชั้น runtime ของ Routine รอบนี้บล็อก DNS ของ openai.com, techcrunch.com, theverge.com, deepmind.google, research.google, ai.meta.com, arxiv.org, nvidia.com, blognone.com, beartai.com, thairath.co.th, matichon.co.th, prachachat.net, thestandard.co, reuters.com, bloomberg.com, theinformation.com, wired.com, technologyreview.com, ft.com, arstechnica.com ทำให้แหล่งข่าว Tier 1 ที่ตรวจสอบได้ในรอบนี้เหลือเพียง anthropic.com และ microsoft.com เท่านั้น
