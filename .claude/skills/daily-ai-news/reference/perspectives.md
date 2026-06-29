# Perspectives — 2026-06-29

## 1. Google Caps Meta's Use of Gemini AI Models

**อาจารย์ (มหาวิทยาลัย):** เคสนี้คือบทเรียน strategic dependency ที่ดีที่สุดของปี — บริษัทที่ใหญ่ที่สุดในโลกอย่าง Meta ยังต้องพึ่ง compute ของคู่แข่ง เพราะ build ของตัวเองไม่ทัน ห้องเรียน Industrial Organization ควรอ่านควบกับเคส OPEC quota ปี 1973
**ผู้เชี่ยวชาญด้าน AI:** การที่ Google "rationing" Gemini ตั้งแต่มีนาคมเป็นสัญญาณว่า inference demand ของ frontier model โต faster than data center build-out — ไม่ใช่แค่ training capacity ที่ตึง การ delay project ภายในของ Meta หมายความว่าวงจร train-eval-iter กำลังถูก throttle ในระดับ org ที่มี GPU เป็นแสนตัวอยู่แล้ว
**โปรแกรมเมอร์มืออาชีพ:** ถ้าใครพึ่ง third-party API ของ frontier model เป็น critical path อย่าสร้างผลิตภัณฑ์โดยสมมุติว่า quota จะ scale ตามที่ขอ — ออกแบบให้รองรับ rate-limit shock ตั้งแต่วันแรก พิจารณา multi-provider routing และ caching layer ก่อนที่ rate-limit จะ hit production

## 2. Firmus + Nvidia Indonesia Data Center

**อาจารย์ (มหาวิทยาลัย):** $30B offtake commitment ใน 6 ปี เป็นเคสคลาสสิกของ infrastructure financing ที่ใช้ guaranteed demand ปลดล็อก capex ห้อง Development Economics ของอาเซียนต้องอ่านควบกับเคส Singapore Jurong refinery — ความเหมือนคือ regional hub strategy ที่ "rent" demand จาก global player
**ผู้เชี่ยวชาญด้าน AI:** 360 MW + 170,000 GPU accelerator เปิดในไตรมาส 1 ปี 2027 หมายถึง latency ที่ดีขึ้นมากสำหรับลูกค้า inference ในอาเซียน-แปซิฟิก ที่ปัจจุบันต้องวิ่งผ่าน Singapore หรือ Sydney; Batam อยู่ห่างจาก Singapore แค่ตัดข้ามช่องแคบ — engineering trade-off คือ throughput ที่ใกล้ Singapore แต่ tax/regulatory framework ของอินโดนีเซีย
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ ship product ในไทย/อาเซียนและกำลังเลือก region สำหรับ inference workload ปี 2027 ควรประเมิน Batam เป็น option ตั้งแต่ตอนนี้ — early-mover discount ของ multi-tenant data center มักหายไปภายในปีแรก; เริ่มคุยกับ Firmus หรือ DayOne เรื่อง credit/pricing tier ก่อนที่ AI-native tenant อื่นจะจอง slot

## 3. BIS Warns of AI Bust Credit Risk

**อาจารย์ (มหาวิทยาลัย):** "Circular financing" ที่ BIS เตือนเป็น textbook financial fragility — เมื่อ Nvidia ลงทุนใน lab, lab จ่ายเงินซื้อชิปจาก Nvidia, แล้ว revenue stream ของทั้งสองฝั่งกลายเป็น mirror ของกันและกัน เคสนี้ตรงกับงานของ Hyman Minsky เรื่อง Ponzi finance — แต่ใส่ rebranding ปี 2026
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่ทำให้คำเตือนนี้แตกต่างจาก hype-bubble warning ทั่วไป คือมันมาจาก central bank ของ central bank — และระบุกลไกที่เฉพาะเจาะจง ($100B hyperscaler bonds, private credit shift, equity-for-compute swap) ไม่ใช่ macro mood วัด systemic risk จริง ไม่ใช่ sentiment
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณเป็น contractor หรือ founder ที่ revenue depends on AI vendor budget — สมมุติว่า budget นั้นจะ tighten ภายใน 12 เดือน ไม่ใช่ขยาย; vendor ที่ pay ผ่าน multi-year commit จะกลายเป็น risk concentration เริ่ม diversify customer base ก่อนเครดิตของ AI sector อยู่ภายใต้ stress

## 4. Austria Lobbies EU to Host Anthropic

**อาจารย์ (มหาวิทยาลัย):** เคสนี้คือจุดเริ่มต้นของ AI sovereignty era — เมื่อ frontier model กลายเป็น export-controlled asset ประเทศที่ไม่ใช่ผู้ผลิตเริ่มมองหาทางทำให้ตัวเองเป็น destination จุดที่น่าสนใจคือ Austria — ไม่ใช่ France หรือ Germany — เคลื่อนก่อน วิชา International Relations ต้องอ่านเคสนี้ควบกับ EU Sovereign Tech Stack
**ผู้เชี่ยวชาญด้าน AI:** ในเชิงปฏิบัติ ข้อเสนอนี้ยังเบลอมาก — "host" Anthropic ใน EU หมายถึง subsidiary, data residency, joint venture หรือ research lab? ก่อนรู้รายละเอียด ยากที่จะประเมินว่า model weight, fine-tuning capacity, หรือ inference endpoint จะอยู่ใน EU จริง; การประกาศทางการเมืองมาก่อน — engineering plan ตามไปทีหลัง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ build บน Claude API ในไทยควรจับตา 90 วันข้างหน้า — ถ้า Austria/EU push success อาจมี EU endpoint ที่ลูกค้าใน Asia-Pacific สามารถใช้ได้ผ่าน region อื่นที่ไม่ใช่สหรัฐ; เก็บ flexibility ในการ swap endpoint base URL โดยไม่ rewrite app

## 5. Ford Rehires "Gray Beard" Engineers After AI Falls Short

**อาจารย์ (มหาวิทยาลัย):** เคสนี้สอนสิ่งที่ Frederick Brooks เขียนใน Mythical Man-Month ตั้งแต่ปี 1975 — tacit knowledge ของ engineer ที่อยู่ในระบบมานานไม่สามารถถูก capture ผ่าน explicit rule ได้หมด ห้อง Knowledge Management ต้องอ่านเคสนี้ควบกับ Polanyi's "tacit knowing" — และตั้งคำถามว่า AI ที่ดี ควรเรียนจาก gray beard หรือ replace gray beard
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่ระบบ automated quality ของ Ford พลาด มักคือ edge case ที่ training data ไม่ครอบคลุม — failure mode ที่เกิดเดือนละครั้งจาก supplier ที่เพิ่งเปลี่ยน process การที่ Ford ใช้ gray beard ทั้ง "hunt for failure" และ "reprogram AI" เป็น loop ของ human-in-the-loop ที่ทำงานจริง ไม่ใช่ผ่าน RLHF lab — แต่ใน production
**โปรแกรมเมอร์มืออาชีพ:** หลายทีมในปีนี้ replace senior engineer ด้วย AI coding agent + junior — เคส Ford เป็นเตือนว่ารูปแบบนี้มี ceiling; senior ที่รู้ "ทำไม code นี้ exist" มีค่าตอนระบบเริ่ม drift จาก assumption; เก็บ senior ไว้ใน team อย่างน้อย 1-2 คนต่อ critical system อย่าให้ AI delete role นี้แม้ feature velocity จะดูสวยในไตรมาสแรก
