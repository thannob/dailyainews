# Sources — 2026-10-29

Generated: 2026-10-29 (Asia/Bangkok)
Runtime: WEBFETCH_BLOCKED
Freshness window: rolling 24h (Asia/Bangkok)
Dedup against: articles/2026-10-28-brief.md (0 URLs loaded — yesterday was a stub)

**ไม่มีข่าวที่ผ่านทั้งสองตัวกรองในรอบนี้**

- Filter A (รอบ 24h) — เป็นตัวบล็อกหลัก: WebSearch ในรอบนี้ไม่สามารถคืน URL จากโดเมนใน `reference/trusted-sources.md` ที่มี timestamp อยู่ในช่วง 2026-10-28/29 (Asia/Bangkok) ได้
- Filter B (dedup) — ไม่ใช่ตัวบล็อกในรอบนี้ (ฉบับ 2026-10-28 เป็น stub ว่าง, มี 0 URLs ให้เทียบ)

## Dropped (candidates seen in search snippets but could not satisfy Tier 2 verification)

- OpenAI math/physics "3 discoveries" follow-up — snippets อ้างถึง `openai.com/index/...` แต่ URL เฉพาะหน้าเรื่องนั้นไม่ปรากฏใน search results ของรอบนี้ มีแต่สำเนาจาก `foxnews.com`, `enoumen.substack.com`, `theirishchannel.com` ซึ่งไม่อยู่ใน trusted-sources.md
- Anthropic IPO filing (security breaches, training halt, $650B compute commitments) — ปรากฏใน `foxnews.com/live-news/...` และ `zerohedge.com/...` และ `venturedailydigest.com/...` ซึ่งไม่อยู่ใน allow-list; URL ของ Bloomberg Technology (ซึ่งอยู่ใน allow-list) ไม่ปรากฏใน search results ของรอบนี้ มีแต่สำเนาบน subdomain `news.bloomberglaw.com` ซึ่งถือว่าเป็นคนละ domain
- OpenAI–Google TPU deal reports — ปรากฏใน `zerohedge.com` และ `venturedailydigest.com` เท่านั้น ไม่ปรากฏใน `reuters.com`, `bloomberg.com`, `theverge.com`, `techcrunch.com` ซึ่งอยู่ใน allow-list
- Google DeepMind Genie 4 — snippet อ้างแต่ไม่มี primary URL จาก `deepmind.google` หรือ `research.google` ปรากฏในผลค้นหา
- Anthropic government deals / 40% discount Claude Enterprise — ปรากฏในสรุปรายวันของ aiweekly.co และ theneuron.ai เท่านั้น ไม่มี URL จาก anthropic.com, reuters.com, bloomberg.com

> Note: 0 items passed both filters this run. Of ~5 candidate stories surfaced in searches, 5 failed Filter A because the only URLs surfaced for them came from non-allow-listed domains (aggregator/syndicator copies). 0 failed Filter B.
