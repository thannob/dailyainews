# Perspectives — 2026-05-09

## 1. Airbnb says AI now writes 60% of its new code

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข 60% เป็นจุดดีในการสอนเรื่อง "metric ที่บอกอะไร / ไม่บอกอะไร" — มันคือ proportion ของบรรทัดที่ผ่าน AI tool, ไม่ใช่ measure ของ design judgement; นักศึกษาควรเข้าใจว่าการ "เขียนโค้ดได้ผ่าน LLM" กับ "ออกแบบระบบที่ถูกต้องและรับผิดชอบได้" เป็นสองทักษะที่แตกต่างกันชัดเจน
**ผู้เชี่ยวชาญด้าน AI:** ที่ Airbnb พูดสอดคล้องกับ Google (>30%) และ Microsoft (~30%) — สิ่งใหม่ไม่ใช่ตัวเลข แต่คือการที่ engineering manager กลับมาเขียนโค้ด เพราะ Claude Code/Codex ลด context-switching cost ระหว่าง "review" กับ "implement"; นี่เปลี่ยน org structure มากกว่า productivity metric
**โปรแกรมเมอร์มืออาชีพ:** practical takeaway — ถ้าทีมยังให้ junior engineer "เขียนโค้ดเอง" อย่างเดียวเพื่อฝึกพื้นฐาน เริ่มหลงยุค; ควรย้ายไปฝึก review skill, debugging AI-generated code, และการเขียน prompt/spec ที่ชัดเจนแทน เพราะ baseline workflow ของบริษัทระดับ Airbnb เปลี่ยนไปแล้ว

## 2. Cloudflare says AI made 1,100 jobs obsolete, even as revenue hit a record high

**อาจารย์ (มหาวิทยาลัย):** กรณี Cloudflare เป็น case study ทองสำหรับ labor economics — บริษัทมีรายได้สูงสุดเป็นประวัติการณ์ (+34% YoY) พร้อมๆ กับเลิกจ้าง 20% ของพนักงาน ซึ่งสวนทางกับ Solow paradox ที่เคยใช้สอนกัน; ควรชวนนักศึกษาวิเคราะห์ว่ามันคือ productivity gain ที่แท้จริง หรือ rationalization narrative สำหรับการ restructuring
**ผู้เชี่ยวชาญด้าน AI:** Matthew Prince อ้าง "AI usage โต 600% ใน 3 เดือน" เป็นสัญญาณที่ต้อง interpret ระวัง — usage กับ value creation ไม่ใช่อันเดียวกัน; ที่น่าสนใจกว่าคือ severance package (full base pay ถึงสิ้นปี + healthcare) ที่ส่งสัญญาณว่าบริษัทกลัว talent backlash ในตลาด AI engineering ที่ยังหิว
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ engineer ที่ทำงานในตำแหน่ง support / ops / customer success — เริ่ม audit งานตัวเองว่ามีกี่ % เป็น repetitive task ที่ AI agent ทำได้แล้ว; เริ่ม build portfolio ในส่วนที่ AI ยังอ่อน (ambiguous root-cause analysis, customer trust, escalation judgement) ภายใน 6 เดือน — Cloudflare เป็นตัวอย่างแรก ไม่ใช่ตัวอย่างสุดท้าย

## 3. The biggest US power grid is under strain from AI — and no one is happy

**อาจารย์ (มหาวิทยาลัย):** การที่ capacity price กระโดดจาก $28.92 → $329.17/MW-day ในเวลา 2 ปี เป็นเคสคลาสสิกของ externality — ต้นทุนการเทรน LLM ที่ดูเหมือนถูกในระดับ corporate กลับ pass-through ไปยังผู้ใช้ไฟฟ้าทั่วประเทศ; ควรใช้สอนเรื่อง infrastructure economics ของ AI ที่ไม่ได้จบที่ค่า GPU
**ผู้เชี่ยวชาญด้าน AI:** PJM ส่งสัญญาณว่ามี "years, not decades" ก่อน grid พัง — ผลกระทบจริงคือ training run ขนาดใหญ่กำลังจะถูก gate โดย power availability มากกว่า GPU supply; AEP ขู่ออกจาก PJM แปลว่า hyperscaler ต้องเริ่มมอง self-supply (nuclear SMR, behind-the-meter solar+storage) ไม่ใช่ option แต่เป็น default
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ทำ inference workload ในไทย/อาเซียน นี่คือสัญญาณให้เริ่ม optimize cost per token จริงจัง — model distillation, quantization, KV-cache reuse, batched inference; ค่าไฟ datacenter ของ provider จะขึ้นในรอบ contract ถัดไป และ vendor pass-through จะไม่กรุณา

## 4. Anthropic Inks $1.8 Billion Computing Deal With Akamai

**อาจารย์ (มหาวิทยาลัย):** ดีลนี้สำคัญในแง่ academic เพราะมันแสดงว่า "compute provider" ไม่จำเป็นต้องเป็น hyperscaler ดั้งเดิม (AWS/Azure/GCP) อีกต่อไป — Akamai (เดิม CDN) กำลังกลายเป็น compute supplier; เป็นวัตถุดิบดีในการสอน industry structure ของ cloud ในยุค AI
**ผู้เชี่ยวชาญด้าน AI:** Anthropic กระจายความเสี่ยง compute ไปยัง 4 พาร์ทเนอร์ใน 2 สัปดาห์ — Google ($200B / 5 ปี), SpaceX Colossus 1 (300MW), Akamai ($1.8B / 7 ปี), AWS เดิม; เป็น textbook supply diversification เพื่อรับ 80x QoQ revenue growth ที่ Dario Amodei รายงาน — และเป็นสัญญาณว่า Anthropic ไม่ยอมล็อกตัวเองกับ Google เพียงรายเดียวแม้จะเป็น strategic investor
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ใช้ Claude API ในการ production — ดีลแบบนี้ลด latency risk และ outage risk ระยะกลาง แต่ก็แปลว่าราคา API จะ stable หรือลดลงช้ากว่าที่คาด เพราะ Anthropic ต้อง amortize compute commitment $200B+; ถ้าทำ multi-LLM router ไว้ก่อน (Claude / GPT-5.5 / Gemini) อย่างน้อยมี optionality ที่ Anthropic เองยังเลือกใช้กับ compute supplier
