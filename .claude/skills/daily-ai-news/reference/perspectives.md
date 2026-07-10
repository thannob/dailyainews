# Perspectives — 2026-07-10

## 1. OpenAI GPT-5.6 (Sol / Terra / Luna) GA

**อาจารย์ (มหาวิทยาลัย):** เคสสอน **AI governance in practice** — 13 วัน limited preview ที่ประสานกับรัฐบาลสหรัฐก่อน general availability คือรูปแบบใหม่ของ "responsible release" ที่ห่างจากรุ่นก่อนของ GPT-4/5 มาก. ให้เด็กเปรียบเทียบ 3 tier (Sol/Terra/Luna) ในแง่ cost × capability curve — model routing decision framework
**ผู้เชี่ยวชาญด้าน AI:** จุดสังเกต 2 อย่าง: (1) Terminal-Bench 2.1 ที่ 91.9% ของ Sol Ultra เป็นเลข head-to-head สำคัญกับ Claude/Grok ที่ต้อง cross-check ด้วย SWE-bench Verified และ LiveCodeBench, (2) การ tier ออกเป็น 3 รุ่นในวัน GA แสดงว่า OpenAI ยอมรับว่า one-size-fits-all จบแล้ว — เข้าสู่ยุค router-first design
**โปรแกรมเมอร์มืออาชีพ:** ต้อง update routing rules ทันที — Luna แทนที่ GPT-5.5 mini สำหรับงาน bulk/summary, Terra สำหรับงาน day-to-day, Sol เก็บไว้ให้ task ที่คุ้ม price. Latency profile ของ Sol น่าจะสูงกว่าเดิม — ทดสอบ p95 บน endpoint จริงก่อน rollout production

## 2. Meta Muse Spark 1.1 (paid agentic coding model)

**อาจารย์ (มหาวิทยาลัย):** เคส **strategy shift** ของ Meta — จาก open-weights (Llama) ที่เป็นแรงต่อรอง ecosystem ไปสู่ paid closed-weights ที่แข่งกับ Anthropic/OpenAI ตรง ๆ. คำถามชั้นเรียน: ทำไม Meta คิดว่าตลาด paid API มี room อีก 4th competitor หลัง OpenAI/Anthropic/Google?
**ผู้เชี่ยวชาญด้าน AI:** ราคา $1.25/$4.25 per M tokens เป็น aggressive ประมาณ 1/4 ของ Claude Opus 4.8 และ GPT-5.5. คำถามคือ **quality gap** เท่าไหร่ — agentic coding benchmark, SWE-bench, tool-calling reliability ยังไม่มี independent eval; รอ 1–2 สัปดาห์. การรองรับทั้ง OpenAI SDK + Anthropic Messages format ลด switching cost อย่างชาญฉลาด — Meta ตั้งใจให้ทีมที่ใช้ Claude/GPT swap เพียง base URL
**โปรแกรมเมอร์มืออาชีพ:** ถ้ามี agent workload ที่ token-heavy (long-running task, RAG pipelines) และ US-only ok เตรียมสร้าง A/B test คู่ Muse Spark 1.1 vs. current model — ราคาต่างมากพอจะเปลี่ยน unit economics. Watch out: closed-weights + preview status = ToS เปลี่ยนได้; อย่า migrate production critical path จนกว่าจะเห็น GA และ SLA

## 3. OpenAI ChatGPT Work (long-running agent)

**อาจารย์ (มหาวิทยาลัย):** ให้ปิดคำถาม "agent จะทำงานยาวได้แค่ไหน" — ChatGPT Work ประกาศตัวเองว่ารัน "for hours" คือ signal ว่า OpenAI คิดว่า **task horizon** ของ agent ขยายจาก 5–30 นาที เป็นระดับชั่วโมง. Assignment: ออกแบบ evaluation ที่วัด task completion ระดับ multi-hour (ไม่ใช่แค่ single-turn accuracy)
**ผู้เชี่ยวชาญด้าน AI:** จับตา (1) **failure mode** ในงาน multi-hour — memory drift, context poisoning, tool errors สะสม, (2) **cost per completed task** เทียบกับ human baseline. OpenAI ปล่อยพร้อม GPT-5.6 GA แสดงว่า ChatGPT Work น่าจะรันบน Sol เป็นหลัก — cost model ต้องแรง
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมมี workflow ที่ทำ document/spreadsheet/slide/web-app แบบ semi-repeat ให้ทดสอบ ChatGPT Work บน task ที่ **ประเมินผลลัพธ์ได้ชัด** (export ได้, มี ground truth) ก่อน. อย่าปล่อย agent รันหลายชั่วโมงบน task ที่ประเมิน quality ไม่ได้ — คุณจะจ่ายเงินโดยไม่รู้ว่าได้อะไรกลับ

## 4. Google AI-ad disclosure

**อาจารย์ (มหาวิทยาลัย):** เคสสอน **platform governance** — Google เป็น ad network ใหญ่ที่สุดในโลก, disclosure "made with AI" คือ policy signal ที่จะเป็น de-facto standard. เชื่อมกับ FTC endorsement rules, EU AI Act disclosure requirements, และ Thailand PDPA/AI regulatory drafts
**ผู้เชี่ยวชาญด้าน AI:** จุดที่ต้องระวังคือ **นิยาม "made with AI"** — Photoshop generative fill นับหรือไม่, upscaler นับหรือไม่, script generated โดย LLM แต่ voice จริงล่ะ? Google ยังไม่ประกาศเกณฑ์ชัด. Watermark & C2PA-style provenance chain น่าจะเป็นทางออกเทคนิค — จับตา metadata standard ที่ Google จะยอมรับ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมทำ ad tech / creative tool ต้องเตรียม pipeline **tag content ที่ถูก AI สร้าง/แก้ไข** ตั้งแต่ต้นทาง. ระยะสั้น: audit ทุก creative workflow ที่ส่ง ad ให้ Google. ระยะกลาง: ผสาน C2PA content credentials เข้ากับ export pipeline

## 5. Ollama $65M Series B

**อาจารย์ (มหาวิทยาลัย):** เคส **open source × commercialization** ที่งาม — 14 พนักงาน, 8.9M dev, 85% Fortune 500 = ratio revenue-per-employee ที่แทบไม่มี startup ใดทำได้. วิเคราะห์ทำไม Ollama ชนะที่ layer local model runner แต่ Docker Desktop ที่ผู้ก่อตั้งเดียวกันสร้างต้อง monetize นานกว่าจะสำเร็จ
**ผู้เชี่ยวชาญด้าน AI:** signal สำคัญคือ **on-prem/local inference** ยังโตอยู่ในยุค frontier-cloud — ผลจาก data-residency regulation (finance/healthcare/gov) + cost pressure ของ 24/7 inference. 67,000 integrations = network effect แข็ง; Ollama กลายเป็น distribution channel ของ open-weight model ที่ Meta, DeepSeek, Mistral ต้องผ่าน. ตัวชี้วัดต่อไป: Ollama Cloud (managed inference) จะแข่ง Together/Fireworks/Groq ได้แค่ไหน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมยังไม่ใช้ Ollama บน dev machine หรือ CI ให้ pilot ทันที — เร็วกว่า docker-compose LLM. ถ้าออกแบบ product ที่ต้อง embed local LLM (privacy-first app, offline mode) Ollama runtime + model catalog + multi-OS binary คือ shortcut ที่ประหยัด 2–3 เดือน. ระวัง: Ollama Cloud เป็น product แยก, pricing อาจเปลี่ยน — อย่า lock-in
