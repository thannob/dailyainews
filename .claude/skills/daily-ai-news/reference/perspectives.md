# Perspectives — 2026-07-13

## 1. OpenAI, Meta, SpaceX Compete for More Cost-Efficient AI Models (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** สังเกตว่าคลื่นการแข่งขันเปลี่ยนจาก "ใครฉลาดสุด" มาเป็น "ใครประหยัดสุดที่ยังใช้งานได้จริง" — เป็นตัวอย่างคลาสสิกของทฤษฎีสินค้าคอมโมดิตี้ (commoditization) เมื่อคุณภาพระหว่างคู่แข่งเริ่มบรรจบกัน ราคาเลยกลายเป็นสนามรบใหม่.
**ผู้เชี่ยวชาญด้าน AI:** การขับเน้นเรื่อง cost-efficiency สะท้อนว่า inference cost คือคอขวดจริง ไม่ใช่ capability อีกต่อไป — โมเดลที่ทำงานได้ 90% ของ frontier ในราคา 1/5 คือความได้เปรียบเชิงกลยุทธ์ที่มีน้ำหนักมากกว่าคะแนน benchmark 1-2 จุด.
**โปรแกรมเมอร์มืออาชีพ:** ถ้ายังใช้ frontier tier เป็น default อยู่ ให้กลับไป audit workload — งานส่วนใหญ่ (classification, summarization, mid-complexity code) ควรวิ่งบน tier ประหยัดก่อน แล้วส่ง fallback ไปที่ frontier เฉพาะ prompt ที่ตรวจสอบว่ายากพอ.

## 2. Funds Fret Over $4.4 Trillion AI Trio's Grip on Emerging Markets (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** เป็นกรณีศึกษาที่ดีเรื่อง concentration risk ของ index-based investing — เมื่อ 3 บริษัทควบคุมผลตอบแทนของทั้ง asset class การ diversify ระดับประเทศจึงไม่เท่ากับการ diversify ระดับ risk factor.
**ผู้เชี่ยวชาญด้าน AI:** ปรากฏการณ์นี้ยืนยันว่ามูลค่าของ AI ในตลาดทุนยังกระจุกที่ upstream (semiconductor และ platform) มากกว่า downstream — สัญญาณว่าโมเดลรายได้จาก AI application ยังไม่ scale พอที่จะทำให้ portfolio manager เชื่อมั่นในหุ้นชั้นสอง.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าถือ ESPP หรือ RSU บริษัทเทค ให้เข้าใจว่าตำแหน่งของคุณอาจซ้อนกับ concentration risk ที่ portfolio อื่นก็มีอยู่แล้ว — ไม่ใช่แค่ risk เดี่ยวของบริษัทตัวเอง.

## 3. Options Brokers With Niche Expertise Defy Automation, AI Shift (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างที่บอกว่าเทคโนโลยี disruption ไม่ได้เดินเป็นเส้นตรง — งานที่ต้องการ tacit knowledge, relationship, และการอ่านสถานการณ์นอก playbook มักอยู่รอดนานกว่าที่ hype cycle คาดการณ์.
**ผู้เชี่ยวชาญด้าน AI:** AI ปัจจุบันเก่งเรื่อง pattern-match บนข้อมูลที่ label ดี แต่ที่ยังห่างจากคนคือ "การรู้ว่าจะไม่ทำอะไร" ในสถานการณ์ที่ข้อมูลไม่พอ — งาน broker niche ที่ต้องประเมิน counterparty risk แบบ real-time ยังอยู่ในโซนที่ automation ยังไปไม่ถึง.
**โปรแกรมเมอร์มืออาชีพ:** บทเรียนสำหรับ engineer คือ — งานเขียนโค้ดเชิงกลไก (boilerplate, CRUD) ถูก automate เร็ว แต่ system design, incident response, และการต่อรอง requirement ยังต้องอาศัย tacit skill ที่ AI ยังตามไม่ทัน. โฟกัสสะสมทักษะเหล่านี้.

## 4. TechCrunch Mobility: A robotaxi ultimatum (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** การยุบ partnership Uber–Waymo ที่ Phoenix เผยความจริงของ platform economics ว่า co-opetition (คู่แข่งกึ่งพันธมิตร) มีอายุจำกัดเสมอ — เมื่อ tech provider มีช่องทางลูกค้าเองได้แล้ว เจ้าของ demand channel จะถูกทิ้ง.
**ผู้เชี่ยวชาญด้าน AI:** การที่ NHTSA เสนอปรับ FMVSS ให้ยอมรับรถไม่มีพวงมาลัย/แป้นเหยียบ คือสัญญาณว่า regulator เริ่มออกแบบมาตรฐานที่ตอบรับ autonomous stack โดยตรง — เป็น regulatory unlock ที่สำคัญกว่า capability breakthrough ทาง technical.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าอยู่สาย embedded หรือ safety-critical systems ให้ติดตาม FMVSS revision รอบนี้ให้ดี — spec ใหม่จะนิยาม interface และ evidence-of-safety ที่ vendor ต้องส่ง regulator ซึ่งจะกลายเป็น engineering requirement ในสาย automotive stack ทั้งวงการ.
