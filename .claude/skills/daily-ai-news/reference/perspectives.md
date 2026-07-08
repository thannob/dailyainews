# Perspectives — 2026-07-08

## 1. Claude Cowork expands to mobile and web

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เห็นชัดว่า agent product-market fit ไม่ได้อยู่ที่ coding อีกต่อไป — ตัวเลขที่ Anthropic เปิดว่ามากกว่า 90% ของ Cowork task ไม่ใช่ dev work บอกกับนักศึกษาว่า "AI คือเครื่องมือของ knowledge worker ทุกสาขา" ไม่ใช่แค่วิศวกรรม; ให้ลอง audit workflow ของตัวเอง 1 สัปดาห์ แล้วชี้ 3 task ที่เหมาะจะ delegate ไป cloud agent
**ผู้เชี่ยวชาญด้าน AI:** จุดที่ต้อง highlight คือ background execution บน cloud — Cowork หลุดจาก desktop VM แล้ว, task รันต่อเมื่อ device offline; นี่คือ shift จาก "agent as UI feature" เป็น "agent as durable service" ที่ต้องคิดเรื่อง state, retry, resume จริงจัง เหมือน job queue มากกว่า chat
**โปรแกรมเมอร์มืออาชีพ:** ถึงเวลาปฏิบัติ — sync task ข้าม device หมายถึงเราต้อง design product ให้ handle agent handoff ระหว่าง web/mobile/desktop; UX pattern เช่น task inbox, progress notification, resume-from-any-surface ควรกลายเป็น baseline. เริ่มจากออกแบบ status endpoint + push channel ให้ agent ที่รันในระบบเรา ไม่ใช่ปล่อย spinner ค้างใน tab เดียว

## 2. Microsoft joins AI cost-cutting trend by relying more on its own MAI models

**อาจารย์ (มหาวิทยาลัย):** เคสสอน supply chain ของ AI ในองค์กร — Microsoft เป็นทั้ง investor รายใหญ่ของ OpenAI และเป็น platform ที่ขาย third-party model ผ่าน Azure ในเวลาเดียวกัน; การหันไปใช้ MAI in-house สอนว่า vendor lock กับ cost structure ตัดสินใจแยกกัน และองค์กรใหญ่จะทยอย diversify model ที่ตัวเองรัน routing ได้เอง
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นเทคนิคที่ต้องจับตาคือ Microsoft ไม่ได้ swap ทั้ง prompt volume แต่ route "บาง percentage" ของ prompt ใน Excel/Word ไป MAI — แสดงว่ามี classifier หรือ policy layer ที่ตัดสินใจ per-request; นี่คือรูปแบบ hybrid stack ที่จะเห็นมากขึ้น: cheap in-house model รับ high-volume/low-risk workload, frontier model สงวนไว้สำหรับ hard task
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมพึ่ง OpenAI/Anthropic API 100% ตอนนี้เป็นสัญญาณให้เตรียม routing layer — abstract prompt call ผ่าน gateway (LiteLLM, OpenRouter, Vercel AI Gateway) เพื่อสามารถส่งบาง traffic ไป cheaper model เมื่อ margin ต้องบีบ; วางระบบ eval ตัวเองให้ตัดสินได้ว่า workload ไหน tolerate model swap ได้บ้าง

## 3. AI law startup Norm raises $120M at $1.2B valuation

**อาจารย์ (มหาวิทยาลัย):** vertical AI in law เป็น case ที่ดีสำหรับสอน commercial law + AI ethics — ทำไม LLM แบบ generic ยังไม่ shake up law firm ได้ แต่ startup ที่ vertical-specific กลับ raise unicorn round? คำตอบสั้น ๆ: domain knowledge + workflow integration + liability model. ให้นักศึกษา JD/Business ลอง map value chain ของงาน paralegal-junior-partner แล้วชี้จุดที่ AI แทนที่ vs. เสริม
**ผู้เชี่ยวชาญด้าน AI:** valuation $1.2B บน Series C ในเวลา 3 ปีบอกว่า vertical AI ที่ "own workflow + own data" ยังได้ premium สูงกว่า horizontal wrapper แม้ในยุคที่ frontier model แข่งขันดุเดือด; ประเด็นเทคนิคที่ทีม vertical AI ต้อง solve คือ domain benchmark ที่ frontier lab ไม่มี — hallucination rate ในการอ้างอิงคำพิพากษาต้องต่ำมาก, retrieval ต้องพิสูจน์ auditable
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ dev ที่คิดสร้าง product AI ใน vertical เฉพาะ (law, medical, finance, compliance) นี่คือ signal ว่า market ยังเปิด — moat จริงคือ (1) proprietary corpus, (2) evaluation harness เฉพาะ domain, (3) enterprise procurement channel (SOC 2, DPA, on-prem option). อย่ามัวแข่ง UI กับ ChatGPT — แข่งที่ integration ลึกกับ workflow ของ vertical นั้น

## 4. Why the rise of open source AI isn't hurting Anthropic ... yet

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข "Anthropic > 50% ของ Vercel spend" ทั้งที่ GLM 5.2 ราคาถูกกว่า ~5 เท่าและ close gap ใน benchmark คือปรากฏการณ์ quality premium ที่ควรอ่านคู่กับทฤษฎี switching cost ใน microeconomics — enterprise ยอมจ่ายเพิ่มเพื่อ predictability, safety review และ SLA ที่ open-weight ยังให้ไม่ได้เต็มรูปแบบ
**ผู้เชี่ยวชาญด้าน AI:** ต้องแยก 2 signal — (ก) เชิง capability GLM 5.2 close gap แล้ว "ภายในช่วง 1 percentage point บน agentic benchmark หนึ่ง" ไม่ใช่ทุก benchmark, (ข) เชิง economics DeepSeek/GLM ครองส่วน price-sensitive แต่ Anthropic ครอง workload ที่ต้องการ tool use, long context และ agent orchestration ที่ยัง stable กว่า; "yet" ใน headline คือ hedging ที่สมเหตุสมผล — trajectory ราคา token frontier ที่พุ่งสวนต้นทุน open source เร่ง cross-over
**โปรแกรมเมอร์มืออาชีพ:** ถ้าสถาปัตยกรรมของทีมยัง lock กับ Anthropic ล้วน ๆ ให้ทดลอง shadow-route 5–10% ของ non-critical workload ผ่าน GLM 5.2 หรือ DeepSeek ผ่าน OpenRouter/Vercel gateway วัด quality gap ด้วย eval ของตัวเอง; ถ้า gap ทำใจได้ก็จะประหยัด burn rate ได้ทันที และมี fallback ถ้า vendor ราคาขยับ

## 5. Meta rolls out Muse Image — agentic AI image generator

**อาจารย์ (มหาวิทยาลัย):** case ที่สอน creative AI + platform economics ในหนึ่งเรื่อง — Meta ฝัง Muse ใน stack ที่มี user 3B+ ต่อวัน แปลว่า marginal cost ของ AI image ต่อ user ต่ำลงมาก เทียบคู่แข่งที่ต้องหา distribution เอง; ให้นักศึกษาถามคำถามจริยธรรม: consent ของ subject ในภาพที่ generate, การใช้ social context (Instagram) เป็น personalization signal, และ label ภาพ AI สำหรับผู้ใช้ทั่วไป
**ผู้เชี่ยวชาญด้าน AI:** จุดสำคัญคือ Muse ไม่ใช่ diffusion-to-image แบบ classic แต่เป็น agent ที่ invoke search, coding tool, self-refine, และใช้ test-time compute scaling — สถาปัตยกรรมนี้บอกว่าอุตสาหกรรมเริ่มย้าย image generation เข้าสู่ paradigm เดียวกับ o-series/Fable reasoning: latency สูงขึ้นในการ generate หนึ่งภาพ เพื่อคุณภาพและ instruction adherence ที่ดีขึ้นมาก
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ integrate image gen ใน product (marketing, product listing, UGC tool) — เตรียมโครงสร้าง cost/latency ที่รองรับ agentic image: 5–30s per generation ไม่ใช่ 500ms อีกต่อไป, cache hit rate สูงกว่าเดิมมีค่ามาก; ในเชิง compliance อย่าลืมว่า Muse image เข้า pipeline advertising — audit trail + provenance metadata (C2PA) ควรเป็น default ในระบบเรา
