# Perspectives — 2026-07-18

## 1. Moonshot AI เปิดตัว Kimi K3

**อาจารย์ (มหาวิทยาลัย):** สอนนักศึกษาว่าเรากำลังเข้าสู่ยุคที่ open-weight model จีนไม่ได้ตามหลังอีกต่อไป — Kimi K3 ระดับ Opus 4.8 ที่ราคา Sonnet เปลี่ยนสูตร "closed frontier คือมาตรฐาน" ให้กลายเป็นสมมติฐานที่ต้องตรวจสอบใหม่ทุกไตรมาส. เหมาะเป็นเคสสอนวิชา AI economics และ open-source strategy คู่ DeepSeek R1.
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 2.8T พร้อมสถาปัตยกรรม KDA + AttnRes และ MoE 896/16 experts น่าสนใจแต่ต้องดู throughput inference จริงและ agent workload real-world ก่อนตัดสิน; benchmark DeepSWE / Terminal Bench / SWE Marathon เป็น proxy ที่ดีสำหรับ coding แต่ไม่ครอบคลุม tool-use loop กับ multi-step reasoning ที่ enterprise ใช้จริง. เตรียม eval harness ภายในไว้ swap-test วัน weights ปล่อย 27 ก.ค.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าราคา $3/$15 ต่อล้านโทเค็นจริงตามที่ประกาศ นี่คือ Opus-class ที่ Sonnet-price — ให้เตรียม fork ของ pipeline production ไว้ 1 branch, benchmark กับ workload ของทีมเอง (ไม่เชื่อพาดหัว), และคำนวณ break-even จุดสลับผู้ให้บริการ. รอวันดาวน์โหลด 27 ก.ค. เพื่อทดสอบ self-hosted บน H100/GB200 ในกรณีที่ latency กับ cost per request สำคัญ.

## 2. Xi Jinping ขึ้นเวที WAIC ครั้งแรก — "AI for All"

**อาจารย์ (มหาวิทยาลัย):** สุนทรพจน์ Xi ยกระดับจากปีที่แล้วชัดเจน — เมื่อผู้นำจีนยืนยันบทบาท rule-maker ระดับโลก คลาสสอนนโยบายเทคโนโลยีต้องขยาย framework จากสองขั้ว (US/EU) เป็นสามขั้ว (US/EU/China) ทันที; วาทกรรม "symphony of international cooperation" เป็นตัวอย่างวาทศิลป์ diplomatic ที่ควรมองคู่กับการกระทำจริง (WAICO membership, model export control).
**ผู้เชี่ยวชาญด้าน AI:** ประโยค "safety risks must be contained" ที่ Xi พูดเป็นครั้งแรกในระดับนี้เปิดช่องให้ engagement กับ safety community ตะวันตกได้จริงขึ้น — จับตาว่ามีข้อเสนอ concrete เช่น shared eval, red-teaming มาตรฐาน หรือแค่ rhetorical position; ถ้ามี agreement ระดับ working group จริง ๆ นั่นคือ turning point.
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ deploy หลายเขตอำนาจ นี่คือสัญญาณว่า compliance layer ต้องเตรียม third bucket — จีน — เพิ่มจาก US NIST / EU AI Act; ระบบ audit log ควรเก็บ metadata ว่าข้อมูล/โมเดลผ่านการตรวจตามชุดกฎใด. อย่ารอให้กฎออกก่อนถึงเริ่ม refactor architecture.

## 3. อนุทิน เสนอ 3 หลักธรรมาภิบาล AI ที่ WAIC

**อาจารย์ (มหาวิทยาลัย):** การที่ผู้นำไทยขึ้นเวที WAIC พร้อม framework 3P (Protection / Potential / Prosperity) เป็นวัสดุการสอนชั้นดีในวิชานโยบาย — ควรวิเคราะห์คู่กับ AI Act ของ EU และ AI Bill of Rights ของสหรัฐ เพื่อให้นักศึกษาเห็นว่าแต่ละประเทศเลือก "ค่านิยมนำ" ต่างกันอย่างไร; และ SHIELD platform ร่วม UNODC เป็นตัวอย่าง multilateral tech cooperation ที่ทำจริง.
**ผู้เชี่ยวชาญด้าน AI:** 3P framework ยังเป็นระดับ high-level principle — คำถามที่ต้องกดต่อคือ implementation: หน่วยงานไทยใดจะเป็น regulator, มี sandbox หรือไม่, เกณฑ์ risk-classification จะสอดคล้อง EU/NIST อย่างไร. SHIELD platform ที่ร่วม UNODC น่าจับตาเพราะเน้น cross-border crime data — เกี่ยวข้อง fraud detection, deepfake enforcement โดยตรง.
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ทำผลิตภัณฑ์ตลาดไทยควรเริ่มออกแบบ product ให้เข้ากับ 3P — โดยเฉพาะ "Protection" ที่แปลว่าต้องมี privacy-by-design, consent flow ที่ชัด, และ audit trail; ถ้าธุรกิจเกี่ยวกับ financial fraud หรือ online safety ให้ติดตามการเปิดตัว SHIELD เพื่อพิจารณา integration โดยเร็ว.

## 4. Kimi K3 ทำหุ้น AI / เซมิคอนดักเตอร์ร่วงทั่วโลก

**อาจารย์ (มหาวิทยาลัย):** เคสตลาดตอบสนอง Kimi K3 คู่กับ DeepSeek shock (มกราคม 2025) เป็นเนื้อหาชั้นดีสำหรับวิชา financial markets & innovation — สอนว่า disruption ที่ประกาศจาก non-US lab กระทบ NVIDIA/Broadcom multiple ทันที ไม่ใช่ในเวลาไตรมาส; และ "reflexivity" ของนักลงทุน AI แคปเอ็กซ์กับ demand curve.
**ผู้เชี่ยวชาญด้าน AI:** market rout ไม่ใช่ verdict ทางเทคนิค — ราคาหุ้นเคลื่อนจากคำ narrative "gap closed" ไม่ใช่จาก benchmark ที่นักวิเคราะห์รัน; ผู้เชี่ยวชาญควรเตือนสาธารณะให้แยก "โมเดลนี้ทำอะไรได้จริง" ออกจาก "นักลงทุนคิดว่ามันหมายถึงอะไร" ระหว่างสัปดาห์นี้.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมพึ่ง cloud GPU บน hyperscaler ให้ล็อค reserved capacity ล่วงหน้า — market shock แบบนี้บางครั้งทำให้ราคา spot GPU ผันผวน; และถ้าทีมเป็น NVIDIA-heavy อย่าง reactive เกินไปกับ headline: hardware demand จริงไม่ได้ลด, แค่ demand ระดับ inference-focused vs training-focused กำลัง rebalance.

## 5. Zoom "Don't record me" hack ต่อต้าน AI transcription

**อาจารย์ (มหาวิทยาลัย):** เคสง่าย ๆ ที่สอนได้ในคาบเรียนเดียว — พูดถึง consent, notice-and-consent framework, และช่องว่างของกฎหมาย wiretapping ในยุค AI note-taker; ให้นักเรียนออกแบบ interaction design ที่ AI recording ต้อง opt-in ทุกฝ่าย และเปรียบเทียบกับ GDPR / PDPA.
**ผู้เชี่ยวชาญด้าน AI:** ปรากฏการณ์นี้ชี้ว่า always-on transcription กำลังกลายเป็น default ที่ไม่มี consent layer ทำ — vendor อย่าง Zoom, Google Meet, Otter, Fireflies ควรมี machine-readable "no-record" signal (คล้าย robots.txt สำหรับ meeting participants) เพื่อไม่ต้องพึ่ง social hack แบบเปลี่ยนชื่อ display.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมทำ note-taker หรือ agent ที่ observe meeting ให้เพิ่ม parser ที่ตรวจ display name / bio field แล้ว honor เจตนา "do not record" ทันที; และเก็บ audit log ว่ามี participant opt-out หรือไม่ — เพราะการเพิกเฉยต่อสัญญาณนี้จะกลายเป็น liability ก่อนที่กฎหมายจะบัญญัติทัน.
