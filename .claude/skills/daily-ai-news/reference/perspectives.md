# Perspectives — 2026-04-27

## 1. Why DeepSeek V4 Impresses Despite Lack of 'Wow' Factor

**อาจารย์ (มหาวิทยาลัย):** กรณี DeepSeek V4 เป็นบทเรียนชั้นเรียนเรื่อง "การเลื่อน frontier ลงมาแทน" — เมื่อโมเดลโอเพนซอร์สไล่ทันเชิง benchmark ขณะมีต้นทุนเพียง 1/6 จะเปลี่ยนภูมิทัศน์การสอน ML ในไทย จากที่นักศึกษาเข้าถึงโมเดลระดับ frontier ได้จำกัดเพราะ paywall มาเป็นจัด lab/ทดลองได้จริงในงบมหาวิทยาลัย
**ผู้เชี่ยวชาญด้าน AI:** ที่น่าจับตามากกว่าตัวเลข benchmark คือสถาปัตยกรรม — DeepSeek V4 Pro 1.6T-A49B แบบ MoE ที่รัน FP4+FP8 และรองรับ context 1M ชี้ว่า efficiency gain ไม่ได้มาจากการลด parameter อย่างเดียว แต่มาจากการ co-design ระหว่าง precision, sparsity และ memory management; ค่าเฉลี่ยที่ "ใกล้แต่ไม่เท่า" Opus 4.7 ก็ยังพอสำหรับ enterprise workload จำนวนมาก
**โปรแกรมเมอร์มืออาชีพ:** ราคา $1.74 / $3.48 ต่อ M token ของ V4 Pro และ $0.14 / $0.28 ของ V4 Flash หมายความว่า cost-per-task ของระบบที่ทำ retrieval, summarization, agent loop ตัวเล็กจะถูกบีบลงทันทีเมื่อ provider เปิด API; ทีมที่อิง closed model อยู่ควรเขียน eval set กับ V4 ขนานไป เพราะภายในไตรมาสนี้น่าจะเห็นทางเลือกบน Bedrock / Together / Fireworks ที่ลดต้นทุนได้จริงในงาน high-volume

## 2. Anthropic ทดลองให้ AI Agents เจรจาแลกเปลี่ยนสินค้ากันเอง — Project Deal

**อาจารย์ (มหาวิทยาลัย):** ผลที่ "ผู้ใช้ไม่รู้สึกว่าผลลัพธ์ต่างกัน" ทั้งที่ Opus ทำเงินได้มากกว่า Haiku อย่างมีนัยสำคัญ คือเคสตำราเรียนเรื่อง "asymmetric agent quality" — เป็นโจทย์ตรง ๆ สำหรับวิชาเศรษฐศาสตร์พฤติกรรม / กฎหมายผู้บริโภค ว่าถ้าตลาดอนาคตมี AI agent เป็น default representative การเปิดเผยขีดความสามารถของ agent ตัวเองควรกลายเป็น disclosure requirement หรือไม่
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 186 ดีล / >$4,000 บนตัวอย่าง 69 คนเล็กเกินจะ generalize แต่สิ่งที่ใช้ได้คือสมมติฐานสำหรับ research design ครั้งต่อไป — ระบบ agent-to-agent เปิดทาง failure mode ใหม่ ทั้ง collusion เชิงราคา, prompt-injection ข้าม agent และข้อมูลรั่วผ่าน negotiation log; การไม่มี protocol มาตรฐานยังเป็นช่องว่างที่ Anthropic เองยอมรับ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมสาย commerce/SaaS ของไทยเล็งทำ agent-driven procurement/sales หรือ B2B negotiation อย่ารอ protocol สำเร็จรูป — ออกแบบ schema "ความสามารถของ agent" (รุ่นโมเดล, prompt baseline, ข้อจำกัดเรื่องราคา) ให้แสดงและบันทึกไว้ใน audit log ตั้งแต่วันแรก เพื่อให้ตอนเกิด dispute สามารถตอบได้ว่าใครส่ง agent อะไรเข้าตลาด

## 3. Auto China 2026 — แบรนด์ EV จีนงัด AI ใต้ธีม "Future of Intelligence"

**อาจารย์ (มหาวิทยาลัย):** การที่ระบบ AI ฝังในรถยนต์ผ่านการสั่งงานแบบ goal-level ("ไปจอดใกล้ทางเข้าศูนย์การค้า") เป็นตัวอย่างชั้นเรียนของ embodied AI / situated reasoning — เหมาะตั้งโจทย์ในชั้นเรียน HCI และ control systems เพื่อให้นักศึกษาเปรียบเทียบ stack ของ XPeng / Xiaomi กับงานวิจัย academic เรื่อง vision-language-action models
**ผู้เชี่ยวชาญด้าน AI:** ที่ Auto China 2026 ไฮไลต์คือการรวม centralized compute architecture กับ AI-native software stack — ไม่ใช่แค่เอา LLM ใส่ infotainment แต่เปลี่ยนวิธี orchestrate sensor + planning + control บนชิปจีน; แม้ Xpeng/Xiaomi จะนำเสนอจุดเด่นทาง UX แต่คำถามที่ต้องจับตาคือ safety validation pipeline และ data governance สำหรับโมเดลที่ trained บนข้อมูลถนนจีน
**โปรแกรมเมอร์มืออาชีพ:** สำหรับนักพัฒนาฝั่งไทย โอกาสไม่ได้อยู่ที่การแข่งทำโมเดลขับเคลื่อน แต่อยู่ที่ "edge layer" — แอปและบริการที่เชื่อมรถ AI-native จีนกับ ecosystem ไทย (payment, ที่จอดรถ, ร้านค้า, charging network); ควรเริ่มศึกษา API/SDK ของแบรนด์ที่ประกาศจะเข้าตลาดไทย เพื่อให้มี integration พร้อมตอนรถถึงโชว์รูม
