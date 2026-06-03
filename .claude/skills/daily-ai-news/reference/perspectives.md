# Perspectives — 2026-06-03

## 1. Microsoft Scout — OpenClaw-based always-on personal agent at Build 2026

**อาจารย์ (มหาวิทยาลัย):** Scout เป็น case study สดของ "agentic OS" — เปลี่ยน paradigm จาก app-centric ไปสู่ agent-centric computing นักศึกษาควรอ่านสถาปัตยกรรม OpenClaw เพื่อเข้าใจว่า framework แบบ open-source ที่ไม่ใช่ของ vendor รายเดียวกลายเป็นรากฐานของ proprietary product ระดับ flagship ได้อย่างไร
**ผู้เชี่ยวชาญด้าน AI:** การที่ Microsoft เลือก OpenClaw (open framework) แทนการสร้าง agent runtime เอง บอกว่า standardization layer ของ agent มาถึงแล้ว — ตามรอย LangGraph / AutoGen ก่อนหน้านี้ ส่วนการบังคับให้ Scout ต้องผูกกับ GitHub Copilot subscription คือ business-model lock-in classic — เปิด framework แต่ปิด distribution
**โปรแกรมเมอร์มืออาชีพ:** Scout requires GitHub Copilot subscription = ต้นทุน per-seat ต่อทีมจะขึ้น ถ้า org มี Copilot license อยู่แล้ว ลอง enroll Frontier program เพื่อเทสต์ workflow automation (calendar, meeting agenda, inbox triage) ก่อน lock-in vendor; ถ้ายังไม่มี ยังเร็วเกินไปที่จะจ่าย enterprise tier เพื่อ Scout อย่างเดียว — รอ benchmark vs Claude Sonnet 4.6 + Cursor agent หรือ Anthropic Cowork

## 2. OpenAI Codex + GPT-5.5/5.4 ขึ้น AWS Bedrock GA

**อาจารย์ (มหาวิทยาลัย):** นี่คือจุดสิ้นสุดของ "exclusive cloud" era ของ OpenAI กับ Microsoft อย่างเป็นทางการ — สอนวิชา platform economics ได้ตรง ๆ ว่า "exclusive deal" ที่เคยถือว่าเป็น moat กลายเป็น constraint เมื่อ supply side (compute capacity) กลายเป็น bottleneck
**ผู้เชี่ยวชาญด้าน AI:** Codex บน Bedrock ใช้ราคา per-token เท่ากับ OpenAI direct (ไม่มี markup) — นี่เป็น signal สำคัญ: ยุค "cloud vendor takes margin on every token" ที่ Azure OpenAI ทำมา 3 ปีกำลังถูก compress สำหรับ enterprise ที่ติด commitments บน AWS อยู่แล้ว → ลด friction ของการ adopt frontier AI ลงเกือบหมด
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมรันบน AWS อยู่แล้ว Codex ผ่าน Bedrock = ใช้ AWS credentials + IAM + VPC isolation ที่ทีม security ของคุณ approve มาแล้ว ไม่ต้องเปิด ticket ใหม่; ราคาตรงกับ OpenAI direct + นับเข้า AWS commitment ที่จ่ายไปแล้ว — เริ่ม pilot ทันที โดยเฉพาะถ้าเคยถูก security team block Azure OpenAI เพราะ data-residency policy

## 3. Alphabet ระดมทุน $80B equity — $10B Berkshire เป็น anchor

**อาจารย์ (มหาวิทยาลัย):** ดีลนี้คือ benchmark ใหม่ของวิชา capital markets — Bloomberg ระบุว่าจะกลายเป็น "biggest equity capital markets transaction of all time" สอนได้ทั้ง mechanism (at-the-market $40B + underwritten $30B + anchor $10B) และ behavioral angle (Berkshire signoff ในสุดสัปดาห์เดียวกลายเป็น market signal ใหญ่กว่าตัวเลข $10B)
**ผู้เชี่ยวชาญด้าน AI:** $80B raise โดย Alphabet ใน 4-5 วันหลัง Anthropic ยื่น S-1 ($965B valuation) และ Nvidia ส่ง Vera ออก = สัญญาณว่า capex race ของ frontier AI ไม่ใช่ marginal investment อีกต่อไป มันคือ existential ต้องสะสม compute capacity ก่อนจะแพ้ economics ของ scale law
**โปรแกรมเมอร์มืออาชีพ:** $80B → AI capex = Gemini capacity, custom TPU fleet, agentic infra ของ Google จะเร่งเครื่องในไตรมาส 3-4 ปีนี้ ถ้าทีมยังไม่ได้ทดสอบ Gemini 3.5 Flash หรือ Vertex AI Agent Builder ตอนนี้คือเวลาที่ Google จะลดราคา / เปิด generous free tier เพื่อแย่ง developer mindshare — ใช้ช่วงนี้ benchmark ก่อนราคาขึ้น

## 4. OpenAI ขยาย Codex ไปวงการ finance / legal / banking / sales — ตีตรง Anthropic

**อาจารย์ (มหาวิทยาลัย):** เคสตำราสำหรับวิชา product-market expansion — เริ่มจาก vertical แคบ (software engineering) แล้วใช้ infrastructure เดียวกัน expand ไป adjacent vertical (finance, legal) เป็น Christensen-style moves แต่ทำให้เร็วขึ้นด้วย agent framework ที่ generalize ได้
**ผู้เชี่ยวชาญด้าน AI:** Codex สำหรับ finance/legal คือ admission ว่า "agent คือ form factor" ไม่ใช่ "model คือ form factor" — Anthropic ครอง finance/legal vertical มาตลอด 12 เดือนผ่าน Claude (เห็นจาก Anthropic Economic Index) สิ่งที่ OpenAI ทำคือเอา agent runtime แบบเดียวกันใส่ vertical-specific tool/plugin — ขนาด moat ของ Anthropic ใน enterprise vertical จะแคบลงเร็ว
**โปรแกรมเมอร์มืออาชีพ:** ถ้าเคยพิจารณา Claude สำหรับ contract review / equity research workflow ให้ rebench ใหม่ทันที — OpenAI จะมา price-aggressive เพราะนี่คือ flagship verticals ของ Anthropic; ถ้าทีม build product สำหรับ finance/legal เอง เริ่ม design app ให้รองรับทั้ง Codex agent และ Claude — vendor switch จะกลายเป็น quarterly decision แทน annual

## 5. VivaTech 2026 — Europe ปั้น industrial-AI strategy ตัดกับ Silicon Valley

**อาจารย์ (มหาวิทยาลัย):** วิชา comparative innovation policy ได้ตัวอย่างชัด — US AI = scale + dominance, EU AI = compliance + sovereignty + industrial integration กลยุทธ์ที่ TechCrunch ชี้คือ "deploy AI ใน regulated vertical ที่ Silicon Valley เข้าไม่ได้" (manufacturing, healthcare, energy) เป็นการเลือก battlefield แทนการแข่ง frontier-model
**ผู้เชี่ยวชาญด้าน AI:** Europe ไม่มี frontier lab ขนาด Anthropic/OpenAI/Google แต่มี domain expertise + regulated-industry capital ที่ใหญ่ — Mistral ทำหน้าที่เป็น national-champion model ส่วน application layer แตกไปที่ vertical specialist (Cognigy, Aleph Alpha, Owkin) คำถามใหญ่: open-weight model จะเหลือเข้าไม่ถึง EU customer ในไตรมาส 3 หรือไม่หลัง AI Act enforcement เริ่มเต็มที่
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีม build SaaS ที่ขายเข้า EU enterprise ปีนี้ — vertical-AI playbook ของยุโรปกำลังจะกลายเป็น default expectation ของ buyer: ต้อง explain provenance ของ training data, ต้องระบุ model weight, ต้องมี audit log ของ agent action ไม่ใช่แค่ output; ใช้ VivaTech (17-20 มิ.ย.) เป็น calibration point ดู vendor checklist ที่ EU enterprise buyer ใช้
