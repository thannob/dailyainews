# Perspectives — 2026-07-29

## 1. 1,100+ AI workers ยื่นจดหมายขอให้รัฐ US ช่วย "pace" การพัฒนา AI

**อาจารย์ (มหาวิทยาลัย):** เคสตัวอย่างของ collective action ในอุตสาหกรรมเทคโนโลยี — พนักงานข้ามบริษัทคู่แข่ง (OpenAI, Anthropic, Google, Meta) รวมตัวเรียกร้อง governance mechanism จากภายนอก แสดงว่าลำพัง safety team ภายในไม่พอ.
**ผู้เชี่ยวชาญด้าน AI:** ตัวจดหมายไม่มีข้อเสนอเชิงเทคนิคที่เจาะจง (ยัง "แค่ขอให้รัฐช่วยหา") — timing ที่ตามหลัง OpenAI disclosure เรื่องโมเดลไม่ปล่อยที่ chain zero-day exploits ทำ RCE ก็บอกว่าเหตุการณ์เดี่ยว ๆ ยัง drive discourse เป็นหลัก ไม่ใช่ framework.
**โปรแกรมเมอร์มืออาชีพ:** ยังไม่มี regulatory impact ที่ต้องคุมโค้ดวันนี้ แต่ signal ว่า research access + red-team result ที่เคย public จะเริ่มโดน gate มากขึ้น ทีมที่ dependent บน pretrained model จาก frontier lab ควรเผื่อว่า release cadence จะช้าลงในครึ่งหลังปี 2026.

## 2. Sam Altman พร้อม "decelerate" — OpenAI + Anthropic หนุนจดหมายพนักงาน

**อาจารย์ (มหาวิทยาลัย):** ประโยค "pace...without it feeling like regulatory capture or collusion" เป็นบทเรียน tension classic ระหว่าง safety, market power, และ antitrust — เอาไปเปิดคลาส tech policy ได้ตรง.
**ผู้เชี่ยวชาญด้าน AI:** Altman ยอมรับ pacing ใน podcast (Invest Like the Best) โดยไม่มี technical mechanism เสนอ — เท่ากับ signal ยอม govern แต่ไม่ commit วิธี; ประเด็นน่าจับตาคือถ้า frontier lab ทั้งสองเจ้าเห็นด้วยจะเกิด de-facto slowdown ก่อนที่ regulation จะออกไหม.
**โปรแกรมเมอร์มืออาชีพ:** ผลระยะสั้นต่อ dev workflow น้อย — ถ้าจะเห็น impact จะเป็น release cadence ของโมเดลใหม่ (GPT/Claude รุ่นถัดไป) ที่ช้าลง ผู้ใช้ API ควรวางแผน roadmap โดยไม่พึ่ง capability jump ทุกไตรมาส.

## 3. Recursive Superintelligence เซ็นดีล compute $410M กับ AWS

**อาจารย์ (มหาวิทยาลัย):** Richard Socher (อดีต Salesforce chief scientist) ตั้ง startup เรียก "self-improving AI" — คลาส AI history ควรเปรียบเทียบกับ AutoML / meta-learning ยุคก่อน ว่าอะไรใหม่ (compute scale) อะไรเก่า (แนวคิด).
**ผู้เชี่ยวชาญด้าน AI:** "Open-ended self-improving" หมายถึงระบบที่ค้นจุดอ่อนตัวเองแล้วปรับ — ตามหลัก technical นี่ต้องการ evaluation loop ที่ trust ได้และ compute เผื่อ fail runs จำนวนมาก; $410M เป็น "smallest of many" ตามคำ Socher — สัญญาณว่า scale จะยิ่งใหญ่ขึ้น. Investors: GV + Nvidia + AMD จับพลังจากสองค่ายชิปพร้อมกันเป็นสิ่งไม่ธรรมดา.
**โปรแกรมเมอร์มืออาชีพ:** ยังไม่มี product ให้ใช้ — ประเด็นที่ใช้ได้จริงคือดีลใหญ่กับ AWS ยืนยันว่า hyperscaler ยังคือทางเลือกหลักของ frontier compute แม้ Nvidia จะทำดีลตรงกับ startup มากขึ้นในสัปดาห์ก่อน; ทีมที่ประเมิน cloud strategy ควรดู multi-hyperscaler capacity ไม่ใช่แค่ Nvidia ดีลตรง.

## 4. Spur Intelligence ระดมทุน $200M จาก Insight — bot > human traffic แล้ว

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข "bot > human traffic ครั้งแรกในประวัติศาสตร์ internet" (Cloudflare, mid-2026) เป็น datapoint สำหรับคลาส web engineering + trust & safety — cornerstone assumption ของ web analytics เปลี่ยนแล้ว.
**ผู้เชี่ยวชาญด้าน AI:** งานของ Spur คือ classify legitimate human vs bot — problem นี้ยากขึ้นแบบ combinatorial เพราะ agentic AI (Claude Computer Use, ChatGPT Agent, ฯลฯ) เลียนแบบพฤติกรรมมนุษย์ได้ดีขึ้น; ทีม detection ที่ใช้ heuristic เก่า (mouse move pattern, HTTP fingerprint) จะ obsolete ในไม่กี่ไตรมาส.
**โปรแกรมเมอร์มืออาชีพ:** ถึงเวลาต้องแยก 3 กลุ่มใน traffic pipeline: human, sanctioned agent (มี API key/attestation), และ unsanctioned bot — และ rate-limit + pricing tier แยกกัน ระบบที่นับ "unique user" แบบเก่าจะ overcount และ metric เชิง engagement จะ meaningless ถ้าไม่ segment.

## 5. AI ทำลายงาน call center — Uber ตัด 10%, CBA + Microsoft + Hyatt ตามมา

**อาจารย์ (มหาวิทยาลัย):** เคส labor economics ทันสมัย — automation wave ครั้งนี้กระทบ knowledge/service work ที่เคยเชื่อว่า "AI-resistant"; นักเรียนควรถามว่าอะไรทำให้ customer service เป็น target อันดับต้น (structured task, high volume, existing recorded conversations for training).
**ผู้เชี่ยวชาญด้าน AI:** สังเกตว่า Uber ตัด "10%" ไม่ใช่ "80%" — บ่งชี้ว่า AI ทำ tier-1 ticket ได้ดี แต่ complex case ยังต้องมนุษย์; อย่าเข้าใจผิดว่า generative AI ทดแทน call center ได้ 100% ในปี 2026 — realistic scenario คือ human agent ที่เหลือจะต้องจัดการ case ยากขึ้น + AI handoff quality กลายเป็น bottleneck.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมกำลังสร้าง support agent — priority วันนี้คือ (1) confidence-threshold routing ที่ escalate ไปมนุษย์เมื่อไม่มั่นใจ, (2) full transcript + tool-call audit สำหรับ case ที่จบแบบไม่ resolve, (3) plan สำหรับ human agent ที่จะรับ handoff ที่ยากขึ้นเรื่อย ๆ — ไม่ใช่แค่ deploy chatbot แล้วปลด CS ทั้งทีม.
