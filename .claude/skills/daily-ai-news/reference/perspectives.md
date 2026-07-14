# Perspectives — 2026-07-14

## 1. TSMC's Sales Soar 36% in Latest Sign of AI Spending Momentum

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข 36% ของ TSMC เป็นกรณีศึกษา "leading indicator" ที่ดี — เมื่อดีมานด์ปลายทาง (AI capex ของ hyperscaler) จะเกิดขึ้นจริงหรือไม่ ให้ดูคำสั่งซื้อของ foundry ก่อนดูรายได้ของบริษัทซอฟต์แวร์.
**ผู้เชี่ยวชาญด้าน AI:** ระดับการเติบโตนี้บอกว่ากลุ่ม hyperscaler ยังไม่ลด order chip ขั้นสูงแม้ตลาดหุ้น AI จะย่อ — สัญญาณว่า capacity plan อีก 12-18 เดือนข้างหน้าถูก lock ไปแล้ว.
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่วาง roadmap ปี 2027 การที่ inference capacity ยังจะโตต่อเนื่องหมายถึงราคา token ต่อหน่วยมีแนวโน้มถูกลงอีก — เขียนโค้ดที่ประเมิน cost per token ให้เป็น dynamic parameter ไม่ใช่ hard-code.

## 2. The wildest allegations in Apple's trade secrets lawsuit against OpenAI

**อาจารย์ (มหาวิทยาลัย):** คดีนี้เปิดบทเรียนสำคัญเรื่อง trade-secret law ในยุค talent war — พนักงานที่ย้ายบริษัทเทคโนโลยีขั้นสูงต้องเข้าใจขอบเขตของ NDA และ non-solicitation ที่ยังผูกพันข้ามพรมแดน.
**ผู้เชี่ยวชาญด้าน AI:** ข้อกล่าวหาเรื่อง "coordinated effort" ในการดึงข้อมูลจากอดีตพนักงานสะท้อนว่าการแข่งขันในรอบนี้ ไม่ได้แข่งกันที่โมเดลอย่างเดียว แต่แข่งกันที่ tacit knowledge ในหัวของทีม — ซึ่งเป็นทรัพย์สินที่ยากจะปกป้องด้วยกฎหมายทั่วไป.
**โปรแกรมเมอร์มืออาชีพ:** ก่อนเปลี่ยนงานไปคู่แข่ง ให้ตรวจ non-compete และเก็บ paper trail ของโค้ดส่วนตัวไว้ให้ชัด — case แบบนี้ทำให้ทั้งฝ่าย HR และฝ่าย legal ของนายจ้างใหม่จะระวังมากขึ้น มีผลตั้งแต่ขั้นสัมภาษณ์.

## 3. Waze adds new AI-powered features and customization updates

**อาจารย์ (มหาวิทยาลัย):** ตัวอย่าง product ที่ใช้ conversational UI แทน form-based UI — น่านำมาสอนหลักการ HCI ยุค LLM ที่ปุ่มและเมนูค่อยๆ ถูกแทนด้วย natural-language intent.
**ผู้เชี่ยวชาญด้าน AI:** การรายงานสภาพถนนแบบ conversational เป็นการใช้ LLM แก้ปัญหาที่ deterministic system เก่งอยู่แล้ว (ปุ่ม "แจ้งอุบัติเหตุ") — คำถามคือ latency และ battery cost จะแลกกับ UX ได้คุ้มไหมในตลาดที่ user คุ้นกับปุ่ม.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าจะเพิ่ม voice/LLM ลง UI ที่มีอยู่ อย่าลืมออกแบบ fallback ให้ user กลับไปใช้ปุ่มได้ทุกจุด — user ที่ขับรถอยู่ต้องการ deterministic path เมื่อ LLM ตีความผิด.

## 4. Washington Is Looking to Keep China From Training Its AI on US Models (distillation debate)

**อาจารย์ (มหาวิทยาลัย):** distillation คือ knowledge transfer จาก teacher model ไป student model — เมื่อบริษัทหนึ่งอ้างว่าเป็น "การขโมย" และอีกฝ่ายเรียกว่า "แค่การใช้งาน API" นี่คือ classic case ของ IP law ตามเทคโนโลยีไม่ทัน.
**ผู้เชี่ยวชาญด้าน AI:** ในแง่เทคนิค distillation ผ่าน API query ทำให้ student model เก่งขึ้นจริงในหลาย benchmark โดยไม่ต้องมี compute ระดับ frontier — ถ้ากฎออกมาห้าม logging output ก็จะกระทบทั้ง alignment research และ commercial fine-tuning ด้วย ไม่ใช่แค่คู่แข่งต่างชาติ.
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ output จากโมเดล frontier มา fine-tune โมเดลของตัวเองต้องอ่าน ToS ให้ละเอียด — โอกาสสูงที่กฎรอบใหม่จะกระทบ workflow นี้ก่อน case จีน-สหรัฐฯ จริงๆ.

## 5. Satya Nadella has issued a shocking warning to companies using AI

**อาจารย์ (มหาวิทยาลัย):** "paying twice" เป็น framing ที่มีประโยชน์ — สอนนักศึกษา economics ของ AI ผ่าน dual currency ของ token cost + data cost แทนที่จะสอนแค่ราคา subscription.
**ผู้เชี่ยวชาญด้าน AI:** ข้อสังเกตของ Nadella สะท้อนว่า data leakage ยังเป็น hidden cost ที่บริษัทส่วนใหญ่ไม่ได้ track — โดยเฉพาะบริษัทที่ใช้ consumer tier แทน enterprise tier เพราะไม่อยากจ่าย premium.
**โปรแกรมเมอร์มืออาชีพ:** ก่อน paste code หรือ log ลงในหน้า chat AI เช็คว่าอยู่ใน enterprise workspace หรือ personal account ให้ชัด — และให้ทีม security ออก policy เรื่อง context ที่พนักงานเอาไปใส่ในโมเดลเป็นมาตรฐาน ไม่ใช่รอให้เกิดปัญหาก่อน.
