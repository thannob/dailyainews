# Perspectives — 2026-08-31

## 1. Musk's faster path to more gas turbines comes with pollution problem

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เป็นตัวอย่างชัดของ "externalities" ในวิชาเศรษฐศาสตร์สิ่งแวดล้อม — ต้นทุนคำนวณของ compute AI (ต่อ token) ไม่ได้ครอบคลุมผลกระทบสุขภาพชุมชนใกล้โรงไฟฟ้า; ควรใช้กรณี Memphis (NAACP vs xAI) สอนการวิเคราะห์ environmental justice ควบคู่กับ energy economics
**ผู้เชี่ยวชาญด้าน AI:** การที่ Musk ต้องเปิดโรงหล่อ blades/vanes เองสะท้อนว่า **compute bottleneck ในระดับ frontier ตอนนี้เลื่อนจาก chip ไปที่ power generation supply chain** — GPU มีให้ซื้อ แต่ turbine casting ไม่มีขายในตลาดเปิด; ทีมสาย infra ควรจับตาว่า vertical integration แบบนี้จะเปลี่ยน cost curve ของ AI infrastructure อย่างไรใน 3-5 ปีข้างหน้า
**โปรแกรมเมอร์มืออาชีพ:** เป็นสัญญาณเชิงระบบว่า **carbon-aware / region-aware scheduling** จะเข้มขึ้นเป็นข้อบังคับ ไม่ใช่แค่ nice-to-have — ทีมที่รัน batch inference/training ควรเริ่มออกแบบ workflow ที่เลือก region ตาม grid mix ได้ และวางตัวเลข energy per request ไว้ใน SLO เผื่อลูกค้าองค์กร (โดยเฉพาะที่มี ESG mandate) เริ่ม audit สายซัพพลาย compute ที่ตัวเองใช้

## 2. Caterpillar is bringing to AI deployment what it learned from automating mining

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ดีสำหรับสอน "AI adoption in incumbent industries" — Caterpillar ไม่ใช่บริษัท AI แต่มี proprietary data (1.6M connected assets, 16+ PB) และประสบการณ์ 20+ ปีในการ deploy autonomous systems จริงในสภาพงานอันตราย; ใช้เปรียบเทียบกับ tech-first companies เพื่อให้เห็นว่าค่า "AI readiness" ที่แท้จริงคือ data + operations, ไม่ใช่โมเดล
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นที่น่าสนใจไม่ใช่ Cat AI Assistant เอง (voice UI over procedures — patterns คุ้นเคย) แต่คือ **จำนวน connected assets 1.6 ล้านชิ้น + 16 PB ของ structured data** ที่เป็น moat ยากลอกเลียน — ทีมที่แข่งใน vertical AI ควรถามตัวเองว่า data flywheel ของตัวเองมีขนาดกี่ order-of-magnitude ห่างจาก incumbents เจ้าถิ่น และมี path ปิดช่องนั้นได้ไหม
**โปรแกรมเมอร์มืออาชีพ:** งบ $100M / 5 ปี ต่อ 118,000 employees = **~$170 ต่อคน ต่อปี** สำหรับ AI upskilling — เป็น benchmark ที่ทีม engineering leaders ในบริษัทไทยเทียบได้เวลา propose budget; และแสดงว่า industrial AI = voice + retrieval-over-proprietary-docs + fleet telemetry เป็น pattern มาตรฐาน — ทีมที่จะ pitch ลูกค้ากลุ่ม heavy industry ควรเริ่มจาก demo pattern แบบนี้ก่อน จินตนาการเรื่อง agentic workflow ทีหลัง

## 3. TechCrunch Mobility: The hidden human cost of robotaxis

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เป็น case study ที่หายากในวิชา Human Factors / AI Safety — **ผู้ได้รับผลกระทบจาก AI failure ไม่ใช่ผู้โดยสาร แต่เป็น safety test driver ที่นั่งอยู่ในรถ**; รูปแบบ liability ก็ซ้อนกัน (Transdev จ้าง test driver ให้ Waymo แต่ Waymo เป็นเจ้าของ software) — เหมาะสอน labor law × algorithmic accountability
**ผู้เชี่ยวชาญด้าน AI:** "brake jab" 24+ ครั้งใน 2 ปีจาก false-positive object detection ชี้ว่า **safety-critical decision boundary ของ perception model ยังไม่สมมาตร** — โมเดลถูก tune ให้ false-positive (เบรกโดยไม่จำเป็น) ดีกว่า false-negative (ชนคน) ซึ่งถูกต้องต่อผู้โดยสาร แต่ **shift ต้นทุนไปที่คนใน loop** — RL/safety teams ควรพิจารณา cost function ที่นับ occupant injury เป็น penalty ด้วย
**โปรแกรมเมอร์มืออาชีพ:** สำหรับใครที่ทำ agent/autonomy stack (โดยเฉพาะที่ human-in-the-loop) — ต้อง log **motion/impact events** ไม่ใช่แค่ decision events, และวาง safety metric ในระดับ user-visible SLO ตั้งแต่แรก; incident 175 วันในลอสแอนเจลิสเป็นตัวอย่างว่า downstream cost ของ false-positive อาจสูงกว่า runtime cost หลายเท่า
