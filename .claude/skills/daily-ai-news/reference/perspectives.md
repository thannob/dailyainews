# Perspectives — 2026-05-04

## 1. Harvard study: AI more accurate ER diagnoses than two human doctors (TechCrunch, 2026-05-03)

**อาจารย์ (มหาวิทยาลัย):** ข้อค้นพบที่น่าสอนคือ "ช่องว่าง 10%+" ที่อยู่ใน triage ช่วงต้น (ข้อมูลน้อย) แล้วแคบลงเหลือ 2–10% เมื่อข้อมูลเพิ่ม — สะท้อนว่าโมเดลเก่งเรื่องการ "พ่นสมมติฐานเชิงกว้าง" จากข้อความเล็กน้อย ส่วนแพทย์เก่งกว่าเมื่อใช้สัญญาณ multimodal เนื้อนิยายของ paper จึงเหมาะสำหรับห้องเรียน evidence-based medicine และ research methods มากกว่าจะเป็น "AI แทนหมอ" ตามพาดหัว
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 67% และส่วนต่าง 10%+ ดูดี แต่อยู่ในเงื่อนไข "text-only" — ไม่มีภาพ, เสียง, หรือ nonverbal cue ของผู้ป่วยเข้ามาในโมเดลเลย เป็นการพิสูจน์ว่า reasoning model อย่าง o1 ทำ structured differential diagnosis ได้ดี ไม่ใช่การพิสูจน์ว่ามันแทน clinical judgment ทั้งหมด ผู้วิจัยเองยังเรียกร้อง controlled trial — ซึ่งตรงตามมาตรฐาน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ product ฝั่ง healthcare บทเรียนคือ — กรณี "ข้อมูลน้อย ตัดสินใจเร็ว" (เช่น triage ER, pre-screening) คือจุดที่ LLM reasoning ทำ value ได้สูงสุด ไม่ใช่ "วินิจฉัยขั้นสุดท้าย" ออกแบบ pipeline ให้คนกับโมเดลแบ่งงานตามข้อมูลที่มี ไม่ใช่แบ่งตามขั้นตอน

## 2. KC Green vs Artisan: 'This is fine' creator says AI startup stole his art (TechCrunch, 2026-05-03)

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เกือบเป็น textbook case ของ "fair use vs derivative use" — โฆษณาเชิงพาณิชย์ที่หยิบงานต้นฉบับไปดัดแปลงเล็กน้อยเพื่อขายสินค้า เป็นจุดที่กฎหมายลิขสิทธิ์มักไม่เข้าข้างผู้ใช้ สอนคู่กับกฎ Oscar ที่ออกเมื่อสองวันก่อนได้ดี — สถาบันต่างวงการเริ่มขีดเส้น "human authorship" คนละทาง
**ผู้เชี่ยวชาญด้าน AI:** ข้อสังเกต — สิ่งที่ Artisan ทำ (เอามีมไปแก้แคปชัน) ไม่ใช่ "AI stole" ในเชิงเทคนิค (ไม่ได้ generate จาก training data) แต่เป็นการใช้งาน asset ของศิลปินไปทำโฆษณาโดยไม่ขออนุญาต บริษัทใช้แบรนดิ้ง "AI-first" เพื่อสร้างกระแสซ้ำๆ จากแผ่นโฆษณาที่ controversial โดยตั้งใจ; ประเด็นนี้เลยเป็นเรื่อง brand ethics + IP มากกว่า technology ของ generative AI
**โปรแกรมเมอร์มืออาชีพ:** ถ้าออกแบบ marketing automation ที่ฝั่ง creative สร้าง asset ใหม่ — ใส่ check ก่อนปล่อยเสมอ: (1) มี source attribution ไหม (2) reverse image search เคยให้คน clear แล้วหรือยัง (3) ถ้า template ใช้มีมที่ดังจริง ต้องสันนิษฐานว่า "ต้องขอ" ไม่ใช่ "ขอเฉพาะที่นึกได้" บริษัทเล็กที่เคย scrape มีมเป็น marketing วันนี้รับ legal exposure ไม่ไหวอีกต่อไป

## 3. California DMV: police can ticket robotaxis under new AV rules (TechCrunch, 2026-05-03)

**อาจารย์ (มหาวิทยาลัย):** สำคัญในเชิง public administration — กฎเก่าตั้งสมมติฐานว่า "คนขับมีหน้าที่รับผิด" ซึ่งใช้กับรถไร้คนขับไม่ได้ การที่ DMV เปลี่ยน frame ให้ผู้ผลิตเป็นผู้รับใบสั่งโดยตรง คือการขยับโครงสร้าง liability ให้สอดคล้องกับเทคโนโลยี เป็นกรณีที่อาจารย์รัฐประศาสนศาสตร์ใช้ได้ทันทีในวิชา regulatory innovation
**ผู้เชี่ยวชาญด้าน AI:** กฎข้อที่น่าสนใจกว่า "ใบสั่ง" คือเงื่อนไข — รับสายฉุกเฉินภายใน 30 วินาที และยอมรับ "electronic geofencing directive" ของหน่วยกู้ภัย หมายความว่ารัฐกำลังบังคับให้ AV เปิด API ให้คน override ได้แบบ real-time นี่คือ "human override" ที่ทำให้ระบบถูกตรวจสอบได้ ซึ่งเป็นโจทย์ engineering ที่ AV maker ทุกรายต้องตอบ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมทำ fleet/AV/automation — โครงสร้าง "72 ชม. รายงาน, 24 ชม. ถ้ามี collision, 30 วินาที first-responder, geofencing accept" คือ requirement spec ที่ใช้ตรงๆ ได้แล้ว ออกแบบ event log + queue + ack callback ตั้งแต่วันแรก หลีกเลี่ยงการต่อ pipeline แบบ best-effort ที่ใช้ในแอปทั่วไป — ในตลาดนี้ SLA คือกฎหมาย

## 4. Bloomberg Dispatch: It's a Weird Time to Be Named Claude (Bloomberg, 2026-05-03)

**อาจารย์ (มหาวิทยาลัย):** ดูผิวเผินเหมือนเรื่องเบาๆ แต่ใช้สอนเรื่อง "everyday social impact of platform AI" ได้ดี — ปัญหาที่เกิดจาก naming collision ระหว่างชื่อคนกับชื่อ AI assistant สะท้อนว่า AI เริ่มซึมเข้า identity layer ของชีวิตประจำวัน เหมาะสำหรับ STS (Science, Technology and Society) syllabus
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นที่ overlooked ในข่าวนี้คือ — ชื่อ "Claude", "Alexa", "Siri" เริ่มเป็น brand name ที่ตลาดจดจำมากจนคนชื่อเดียวกันต้อง "negotiate identity" กับเทคโนโลยี ไม่ใช่ตรงข้าม นี่คือ adoption signal ที่ราคาตลาดสะท้อนช้ากว่า — Anthropic วาง "Claude" เป็น first-name positioning ตั้งแต่แรกและตอนนี้กำลังเก็บเกี่ยว
**โปรแกรมเมอร์มืออาชีพ:** บทเรียน practical — ถ้าทีมตั้งชื่อ AI agent หรือ feature ภายในที่จะเปิดให้ลูกค้าใช้ คิดเรื่อง "namespace collision" กับชื่อจริงของคนตั้งแต่ตอนเลือก ใช้ชื่อสั้น เฉพาะ มี trademark check และเตรียม branding fallback ถ้าฐานผู้ใช้ขยายข้ามภาษา การตั้งชื่อแบบ Anthropic ที่จงใจเลือกชื่อ "ฟังเหมือนคน" ทำให้ adoption ดี แต่ก็ลากปัญหา social มาด้วย
