# Perspectives — 2026-06-13

## 1. SpaceX IPO + Google $920M/เดือนค่า compute ที่ xAI

**อาจารย์ (มหาวิทยาลัย):** เคสนี้สอนได้ตรง ๆ ว่าทำไม "AI compute" กลายเป็น strategic asset ระดับ corporate และ macro — Google ยอมจ่ายให้คู่แข่งโดยตรง (Musk/xAI) เพื่อเอา GPU มาให้ Gemini รัน ทั้งที่เพิ่งทำดีลคล้ายกันกับ Anthropic; สอนนักศึกษาให้แยก "ใครแข่งใน application layer" กับ "ใครเป็น supplier ใน infra layer" ออกจากกันให้ขาด
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 110,000 Nvidia GPU + 920 ล้านดอลลาร์/เดือน + ระยะ 32 เดือน บอกเราว่า inference demand ของ AI products รุ่นใหม่ของ Google เกิน internal capacity ไปแล้ว — และที่สำคัญกว่าคือ Google เลือก "เช่า" แทนการ "สร้าง" คือ signal ว่า opportunity cost ของการรอ data center ตัวเองสร้างเสร็จ > ค่าเช่าจากคู่แข่ง
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณตั้ง budget cloud spend สำหรับ AI workload ปี 2027 — ตัวเลขนี้บอกว่าตลาด GPU rental ยังตึงและราคาไม่ลดเร็ว ๆ นี้; การมี multi-cloud / multi-provider strategy ไม่ใช่ของฟุ่มเฟือยอีกต่อไป เพราะแม้แต่ Google ยังต้องไปเช่าที่อื่น

## 2. ผู้นำ AI เข้าร่วม G7 ที่ฝรั่งเศส 15–17 มิ.ย.

**อาจารย์ (มหาวิทยาลัย):** ใช้สอนวิชา international relations / tech policy ว่ารูปแบบ governance ของ AI กำลังเปลี่ยนจาก "regulator vs lab" เป็น "G7 + lab founders โต๊ะเดียวกัน" — ระวังว่า working lunch แบบนี้กำหนด rule ที่ regulator ต้องตามให้ทัน ไม่ใช่ในทางกลับกัน; ตั้งคำถามว่าใครเป็นตัวแทนของ civil society บนโต๊ะนั้นบ้าง
**ผู้เชี่ยวชาญด้าน AI:** การมีทั้ง 3 frontier lab + Mistral + Cohere + Black Forest Labs + Sarvam AI ของอินเดียอยู่ในงานเดียวกันคือสัญญาณว่า "middle powers" (EU, อินเดีย) จะพยายามดัน non-US-non-China framework; วาระ AI infrastructure + networks ในที่ประชุมจะกระทบ data residency law ภายในไม่กี่เดือน
**โปรแกรมเมอร์มืออาชีพ:** ระวัง voluntary commitment ที่ออกจาก summit นี้ — มันจะกลายเป็น checklist สำหรับ enterprise sales รอบหน้าทันที (เช่น "agent ของคุณรองรับ frontier safety commitments ของ G7 ฉบับล่าสุดไหม") เริ่ม track เอกสารตั้งแต่วันที่ joint statement ออก

## 3. Kioxia แซง Toyota ขึ้นเป็นบริษัทมูลค่าสูงสุดในญี่ปุ่นจาก AI memory demand

**อาจารย์ (มหาวิทยาลัย):** เป็น case study ของวิชา industrial economics — บริษัทที่ผลิต NAND flash memory ระดับ commodity ราคาหุ้นวิ่ง 660% ในปีเดียวเพราะการกลายเป็น "choke point" ของ supply chain AI; สอนว่า rent ของ choke point มีค่ามากกว่าราคาสินค้าโดยตรง
**ผู้เชี่ยวชาญด้าน AI:** AI inference cluster ต้องการ memory bandwidth + capacity ทั้ง HBM (Hynix/Samsung) และ NAND สำหรับ KV cache offload + checkpoint storage — Kioxia เลยได้ประโยชน์เต็ม ๆ จาก trend นี้; ใครกำลังออกแบบ inference stack ของตัวเองควรเข้าใจว่า memory cost จะกลายเป็น single largest line item แทนที่ GPU ในอีก 12–18 เดือน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ self-hosted inference หรือ on-premise AI service ใน TH/SEA — สั่ง SSD/NAND ตอนนี้ เพราะ supply allocation ปีหน้าจะไปที่ hyperscaler ก่อน ราคา enterprise SSD คาดว่าจะปรับขึ้นรอบใหม่ Q4 2026

## 4. Google ฟ้องเครือข่าย Outsider Enterprise ใช้ Gemini รัน phishing-as-a-service

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ใช้สอน computer ethics / cybersecurity law ได้ครบ — เป็นคดีแรกที่ AI lab รายใหญ่ฟ้อง threat actor ที่ใช้โมเดลของตัวเองรัน criminal operation; ปรากฏการณ์นี้ปลด lock ของคำถามว่า "ใครรับผิดเมื่อ AI ถูกใช้ก่ออาชญากรรม" — คำตอบรอบนี้คือ lab เลือกใช้ civil litigation
**ผู้เชี่ยวชาญด้าน AI:** เครือข่ายขาย kit phishing ราคา 88 ดอลลาร์/สัปดาห์หรือ 200 ดอลลาร์/เดือน พร้อม template เลียนแบบ >290 แบรนด์ — โมเดล safety filter ของ frontier lab ทุกค่ายต้องทบทวนว่ามี way ใดกัน Gemini/Claude/GPT ไม่ให้สร้าง phishing-page HTML/JS แม้ผู้ใช้กรอก prompt อ้อม; การฟ้องคู่กับการยึดโดเมนคือ playbook ที่ค่ายอื่นน่าจะลอก
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ product ใช้ Gemini / Claude / GPT รับ user prompt อิสระ — pattern phishing kit นี้คือ red-team scenario ที่ต้องทดสอบทันที; เริ่ม integrate detection ว่า output ของโมเดลถูกใช้สร้าง brand impersonation หรือไม่ก่อนปล่อยให้ลูกค้า abuse แล้ว lab โดน subpoena ลามมาถึง downstream developer

## 5. HayWire — AI newsletter สรุปตลาด hay 15,000 ล้านดอลลาร์ จาก USDA data

**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างที่ดีของวิชา data journalism / vertical AI — สองคนใช้ public data + AI model ขุดข้อมูลจาก USDA auction report สร้าง newsletter ฟรีที่ทำให้ตลาด commodity คลาสสิกโปร่งใส; สอนนักศึกษาว่า value creation ในยุค AI ไม่ใช่การสร้างโมเดล แต่เป็นการ position ตัวเองที่ specific market gap
**ผู้เชี่ยวชาญด้าน AI:** เคสนี้ยืนยัน thesis "vibecoded vertical" — สอง founder ใช้ AI coding tools เขียน ETL + summary pipeline แล้วส่งฟรีทุกอังคาร; โครงสร้างคือ small-model + retrieval over USDA reports + Markdown publish; ทำให้ entry cost ของ specialized media tools ต่ำพอที่ commodity vertical ไหนก็มี HayWire ของตัวเองได้
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณรู้จัก vertical ที่ pricing data กระจัดกระจาย (อาหารสด ปุ๋ย ปศุสัตว์ วัสดุก่อสร้าง TH) — pattern HayWire ใช้ AI pipeline + free distribution + sponsorship/listings monetization คือ template ที่คนคนเดียวก็ทำได้ ลองเริ่มจากแหล่งข้อมูลสาธารณะของกรมการค้าภายในหรือสำนักงานเศรษฐกิจการเกษตรของไทย
