# Perspectives — 2026-04-23

## 1. กูเกิลเปิดตัว TPU รุ่นที่ 8 แยกชิปฝึกโมเดลออกจากชิปรัน (Blognone)

**อาจารย์ (มหาวิทยาลัย):** การแยกสถาปัตยกรรมระหว่าง training และ inference เป็นตัวอย่างที่ดีของหลัก separation of concerns ในงานฮาร์ดแวร์ — นักเรียนควรเข้าใจว่าเวิร์กโหลดสองแบบต้องการ memory bandwidth, latency และความแม่นยำตัวเลขที่ต่างกัน ไม่ใช่ "ชิปเดียวเก่งทุกอย่าง"
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 2.7× perf/$ เหนือ Ironwood บน TPU 8t เป็นการเปลี่ยนสมการเศรษฐกิจการฝึกโมเดลใหญ่ ส่วน TPU 8i ที่เพิ่ม on-chip SRAM สามเท่า ตั้งใจแก้ปัญหา KV-cache ที่เป็นคอขวดของโมเดล MoE ขนาดใหญ่โดยตรง
**โปรแกรมเมอร์มืออาชีพ:** สำหรับคนที่จ่ายบิล cloud ทุกเดือน นี่หมายถึงตัวเลือกใหม่ในการ optimize cost — งาน batch training ไปที่ TPU 8t ส่วน endpoint ที่ต้อง low-latency เอา TPU 8i; ถึงจะยังไม่ GA แต่ควรเริ่มวางแผน capacity planning ตั้งแต่ตอนนี้

## 2. Google Releases New AI Agents to Challenge OpenAI and Anthropic (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** การที่ Google เปิด developer platform ที่รวมโมเดลของคู่แข่ง (Claude) เข้ามาด้วย ชี้ให้เห็นว่าตลาด AI platform กำลังเข้าสู่ยุค "multi-model orchestration" — ผู้เรียนควรฝึกเปรียบเทียบ capability/price ของโมเดลหลายค่าย ไม่ผูกติดกับยี่ห้อเดียว
**ผู้เชี่ยวชาญด้าน AI:** no-code agent builder สำหรับ Workspace เป็นสัญญาณว่า "agent" กำลังเลื่อนจากระดับ API ไปเป็นระดับ product ที่ business user ก็ใช้ได้ — Project Mariner (web-browsing agent) คือการทดสอบจริงว่า browsing agent จะรับมือกับ real-world website ได้ดีแค่ไหน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าลูกค้าองค์กรของคุณเป็น Google Workspace shop อยู่แล้ว pressure จะมาจากฝั่งธุรกิจให้ integrate agents เข้ากับกระบวนการก่อน — เตรียม governance layer, audit log และ rollback pattern ก่อนที่ no-code agent จะถูก deploy แบบควบคุมไม่ทัน

## 3. Google deepens Thinking Machines Lab ties with new multi-billion-dollar deal (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** ดีลระดับ multi-billion ระหว่าง cloud provider กับ frontier lab เล็กๆ (Thinking Machines ของ Mira Murati) ช่วยให้นักศึกษาเห็นโครงสร้างอุตสาหกรรม AI ที่ compute capacity เป็น currency หลัก ไม่น้อยไปกว่า talent หรือ data
**ผู้เชี่ยวชาญด้าน AI:** การที่ Thinking Machines เลือก AI Hypercomputer ของ Google มากกว่า Nvidia stack เป็นสัญญาณทางเทคนิคว่า TPU-based pipeline พร้อมสำหรับงานวิจัย frontier-scale ไม่ใช่แค่งาน production inference อีกต่อไป
**โปรแกรมเมอร์มืออาชีพ:** สำหรับคนทำงานกับ startup AI — บทเรียนคือ compute contract ระยะยาวอาจเป็น dilution-free funding รูปแบบใหม่ แต่ก็ lock-in ด้าน framework/toolchain ตามไปด้วย ต้องชั่งน้ำหนักก่อนเซ็น

## 4. SpaceX preempted a $2B fundraise with a $60B buyout offer for Cursor (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษาสำคัญเรื่อง corporate strategy — SpaceX (ซึ่งเพิ่งควบรวมกับ xAI) ยอมจ่ายราคา premium เพื่อ "จองสิทธิ์" ซื้อ Cursor แทนที่จะรอ VC round ชี้ให้เห็นว่ามูลค่า AI coding tool ในสายตาผู้ซื้อเชิงยุทธศาสตร์อาจสูงกว่าที่ตลาด VC คำนวณ
**ผู้เชี่ยวชาญด้าน AI:** AI coding เป็น category ที่สร้างรายได้จริงและวัดผลได้ชัดเจนที่สุดในยุคนี้ — ดีล $60B บอกว่า Musk มองว่าเครื่องมือเขียนโค้ดด้วย AI คือ moat ที่สำคัญในการแข่งกับ OpenAI/Anthropic ไม่ใช่แค่ฟีเจอร์เสริม
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมของคุณพึ่ง Cursor อยู่ ให้เริ่มประเมิน vendor risk — roadmap อาจเบนไปทาง xAI/Grok stack หลังดีลสมบูรณ์; มี contingency (Zed, VS Code + Copilot, Windsurf, หรือ Claude Code เป็นต้น) ไว้พร้อม

## 5. Meta will record employees' keystrokes to train its AI models (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** นี่คือกรณีสดที่จะสอนหัวข้อ AI ethics — เส้นแบ่งระหว่าง "training data" กับ "surveillance" เริ่มพร่ามัว; ผู้เรียนควรฝึกวิเคราะห์ทั้งในมิติ legal (labor law, GDPR-like regime) และมิติ philosophical (consent, purpose limitation)
**ผู้เชี่ยวชาญด้าน AI:** ในทางเทคนิค การมี behavioral trace จริงของคนทำงาน (mouse, keystroke, screenshot) เป็นข้อมูล high-signal สำหรับฝึก computer-use agent — แต่เป็นข้อมูลที่มี bias สูงต่อ workflow ภายในเมตาและเต็มไปด้วย PII ที่ต้อง sanitize เข้มงวด
**โปรแกรมเมอร์มืออาชีพ:** พนักงานควรตรวจสอบว่ามี software ลักษณะนี้บนเครื่อง work laptop ของตัวเองหรือไม่ และแยก personal account ออกจากเครื่องงานให้ชัด; ฝั่งผู้บริหาร IT ต้องเตรียมคำตอบเรื่อง opt-out และ data retention ให้พนักงานก่อนที่ morale จะพัง
