# Perspectives — 2026-06-23

## 1. The AI world is getting 'loopy' — agents prompting agents

**อาจารย์ (มหาวิทยาลัย):** นี่คือก้าวที่สามของการเขียนโปรแกรม — จากมนุษย์เขียนโค้ด → agent เขียนโค้ดให้มนุษย์ → agent สั่ง agent เขียนโค้ดเอง ควรชวนนักเรียนสะท้อนว่า "การกำกับคุณภาพ" เปลี่ยนหน้าตาอย่างไรเมื่อมนุษย์ห่างจาก keyboard อีกขั้นหนึ่ง
**ผู้เชี่ยวชาญด้าน AI:** Cherny ไม่ได้พูดเล่น — meta-loop ที่ "agent หา duplicated abstraction แล้วรวมให้" คือ continuous refactor ที่ทำได้จริงในงาน production ปัจจุบัน แต่ค่าใช้จ่าย token และความเสี่ยง regression จะกระโดด ต้องมี evaluation harness และ guardrail ที่แน่นกว่ารอบก่อน ๆ
**โปรแกรมเมอร์มืออาชีพ:** ถึงเวลา audit ว่าทีมเรามี "loop budget" หรือยัง — กำหนดเพดาน token ต่อ loop, ขั้นต่ำ test coverage ก่อน merge, และ rollback กลไกที่ทำงานอัตโนมัติ ไม่งั้น Friday night จะมี PR ปลายเปิด 200 ฉบับรอ review

## 2. Google DeepMind + A24 $75M Hollywood deal

**อาจารย์ (มหาวิทยาลัย):** นี่คือกรณีศึกษา "AI พบศิลปะ" ที่ดีกว่า text-to-video เพราะมี artist guidance อยู่ใน loop — สอนได้ว่าทำไม "tool ที่นักสร้างต้องการจริง" ต่างจาก "tool ที่ vendor คิดว่านักสร้างต้องการ" ลึกเพียงใด
**ผู้เชี่ยวชาญด้าน AI:** $75M ไม่ใหญ่สำหรับ DeepMind แต่ใหญ่สำหรับ A24 — สิ่งที่ DeepMind ได้กลับมามีค่ามากกว่าเงินคือ "ground-truth feedback" จากนักสร้างที่มีรสนิยมระดับโลก ซึ่งเป็นสิ่งที่ benchmark สังเคราะห์ไม่เคยสะท้อนได้
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ creative-tools / video-gen อยู่ — โอกาสที่ DeepMind จะ open-source ส่วนของ pipeline ที่ผ่านการ co-design กับ A24 มีพอควรใน 12-18 เดือนข้างหน้า ติดตาม research blog และเตรียม integrate ใน workflow ของ creator ที่คุณ service อยู่

## 3. SpaceX + Reflection AI $6.3B compute deal

**อาจารย์ (มหาวิทยาลัย):** น่าสอนเรื่อง "compute เป็น new oil" — โดยเฉพาะข้อเท็จจริงที่ open-source lab อย่าง Reflection ต้องจ่าย $150M/month เพื่ออยู่ในเกม แม้ตัวเองไม่ได้ขายโมเดลแบบ closed-API ความสัมพันธ์ระหว่าง infrastructure capital กับ open ecosystem เปลี่ยนไปแล้ว
**ผู้เชี่ยวชาญด้าน AI:** Colossus 2 + GB300 หมายความว่า Reflection ได้ training cluster ระดับเดียวกับ frontier labs — คำถามคือพวกเขาจะใช้ scale นี้กับ research agenda แบบไหน ถ้าเป็น open-weight model ขนาดใหญ่ก็จะกระทบ landscape ทั้งหมด ถ้าเป็น narrow research ก็จะเป็น cost ที่ตอบแทนช้ากว่าคู่แข่ง closed
**โปรแกรมเมอร์มืออาชีพ:** การที่ SpaceXAI กลายเป็น compute provider ที่ third-party เลือกใช้ หมายถึง ecosystem ของ "ทางเลือกอื่นนอก AWS/Azure/GCP" เริ่มมีจริง — ถ้าทีมต้องการ negotiation leverage กับ hyperscaler ปัจจุบัน นี่คือ data point ใช้กดดันได้

## 4. Nvidia Halos for humanoid robots

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้สอน "transfer learning ระดับ industry" ได้ดี — Halos ที่พัฒนาเพื่อ autonomous vehicle ถูกย้ายมาใช้กับ humanoid robot โดยใช้ core safety pattern เดียวกัน ชวนถามว่า "อะไรคือ invariants ของระบบ safety-critical ข้าม domain"
**ผู้เชี่ยวชาญด้าน AI:** safety stack ที่ผ่าน ANAB accreditation ของ Halos = differentiator จริงในวันที่ humanoid วิ่งใน factory floor มีคนจริงรอบตัว functional safety certification เป็น barrier to entry ที่ใหญ่กว่า perception accuracy ของโมเดลในมุมการ commercialize
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีม robotics ที่ใช้ ROS 2 + Isaac อยู่แล้ว — IGX Thor + Halos OS จะกลายเป็น stack มาตรฐานสำหรับ humanoid ในปีหน้า ถ้ารายได้อยู่กับ industrial robotics ควรเริ่มทดสอบ Halos integration ก่อนคู่แข่งใช้เป็น procurement requirement

## 5. Qualcomm to acquire Modular for ~$4B

**อาจารย์ (มหาวิทยาลัย):** ใช้สอนเรื่อง "compiler และ developer tooling เป็นชั้นที่มูลค่าสูง" — Modular ไม่ได้ทำชิป แต่ทำ stack ที่ทำให้ workload AI วิ่งบนหลายชิปได้ Qualcomm ยอมจ่าย $4B เพื่อชั้นนี้บอกอะไรเกี่ยวกับโครงสร้างมูลค่าของ AI infrastructure
**ผู้เชี่ยวชาญด้าน AI:** Mojo + MAX engine ของ Modular เป็นเดิมพันว่า "portable AI compute" จะแทนที่ CUDA-lock-in ในระดับ inference Qualcomm ได้สิ่งที่ขาดมานานคือ developer story ที่แข่งกับ Nvidia ได้บน on-device และ edge — แต่จะ integrate กับ Snapdragon stack ได้เร็วแค่ไหนเป็นคำถามใหญ่
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมพัฒนา AI workload บน device หลายแพลตฟอร์ม (iOS/Android/laptop) — Mojo จะมี backing organization ที่ใหญ่และมั่นคงขึ้น คุ้มลงทุนทดลองใน research project ตอนนี้ ถ้า toolchain โต Qualcomm มีอำนาจ push ให้เป็น default บน Snapdragon ในปีหน้า
