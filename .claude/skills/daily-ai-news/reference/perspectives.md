# Perspectives — 2026-05-29

## 1. Sesame เปิดตัว iOS app เอเจนต์สนทนา (Oculus founders)

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ใช้สอน HCI ได้ตรง — แทนที่จะวัดคุณภาพ chatbot ด้วย answer accuracy เพียงอย่างเดียว Sesame เลือกออกแบบให้บทสนทนา "ไหล" ต่อแม้ AI ต้องคิด ซึ่งเปลี่ยนเมตริกจาก latency-to-answer ไปสู่ conversational continuity ที่ยังไม่มี standard benchmark
**ผู้เชี่ยวชาญด้าน AI:** การมี 4 personas (Maya, Miles, Simone, Charlie) ที่มี memory แยกกันคือ design choice ที่น่าจับตา — แทนที่จะรวมเป็น universal assistant แบบ ChatGPT ทีมเลือก fragment ตัวตน ซึ่งช่วยทั้งเรื่อง alignment (เห็นบทบาทชัด, evaluation ทำได้ตรง persona) และเรื่อง engagement (user สัมพันธ์กับตัวละครได้)
**โปรแกรมเมอร์มืออาชีพ:** ปล่อยฟรีใน 39 ประเทศตั้งแต่ day-one แปลว่าทีม backend รับ load ระดับล้านได้แล้ว — ถ้าทำ voice/chat app ส่วนตัว ไปลองใช้ App Store เพื่อ benchmark p95 latency, turn-taking และ memory recall ของจริงก่อนตัดสินใจ stack ตัวเอง

## 2. AWS เปิด OpenSearch Serverless รุ่น agentic — internet กำลังถูกออกแบบใหม่เพื่อ machine

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข bots = 31% ของ HTTP traffic 6 เดือนล่าสุด และคาดว่า non-human traffic จะแซง human ใน 1H 2027 ต้องเข้าหลักสูตร internet/distributed systems ทันที — อีก 18 เดือน "ผู้ใช้ส่วนใหญ่" ของอินเทอร์เน็ตจะไม่ใช่มนุษย์อีกต่อไป
**ผู้เชี่ยวชาญด้าน AI:** การ decouple compute จาก storage และ scale ลงถึง zero ($0 ตอน idle) คือ business model สำหรับ agentic workload โดยเฉพาะ — agent burst เกิดเป็นวินาที spawn sub-agent หลายสิบตัวพร้อม query DB หลายร้อย table แล้วหายไป pricing เดิมที่คิดตามชั่วโมงไม่ work
**โปรแกรมเมอร์มืออาชีพ:** ถ้าระบบของคุณมี API endpoint ที่ agent เรียกได้ ทำ rate-limit + cost-cap แยกระหว่าง human user vs agent token ตั้งแต่ตอนนี้ — bill shock จะมาจาก agent ที่ spin up sub-agent หลายสิบตัวพร้อมกัน ไม่ใช่จาก user คนเดียว

## 3. RSI = AGI ตัวใหม่ของวงการ AI — แต่นิยามยังไม่ชัด

**อาจารย์ (มหาวิทยาลัย):** ใช้คู่กับ "AGI" ในวิชา philosophy of mind หรือ AI safety ได้ดี — RSI (Recursive Self-Improvement) ถูกผูกกับ takeoff scenario ของ Bostrom และ Yudkowsky มานาน นี่คือครั้งแรกที่ VC term sheet เริ่มใส่ RSI เป็น milestone จริง
**ผู้เชี่ยวชาญด้าน AI:** Recursive Superintelligence ของ Richard Socher และโครงการ Auto-Research ที่ใช้ agent swarm train LLM เป็น signal ว่า self-improving loop กำลังถูก operationalize เป็น engineering target — แต่ตามที่ TechCrunch ระบุ industry ยังห่างจาก closed loop ที่ meaningful อยู่มาก
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมเริ่มทำ AutoML/agent ที่ "ปรับปรุงตัวเอง" ออกแบบ feedback signal + stop condition ตั้งแต่ design doc — RSI ที่ไม่มี kill switch + bounded compute budget คือ classic chaos engineering disaster ที่รออยู่

## 4. General Compute สั่ง $300M ของ SambaNova SN50 — สงคราม inference compute ยกใหม่

**อาจารย์ (มหาวิทยาลัย):** ใช้เป็น case study เปรียบเทียบ GPU vs ASIC architecture ในวิชา computer architecture ได้ตรง — 600–700 tokens/sec vs 250 tokens/sec ของ GPU + air-cooled คือตัวเลขที่นักศึกษาวิศวะคำนวณ TCO ได้
**ผู้เชี่ยวชาญด้าน AI:** จุดที่แหลมที่สุดไม่ใช่ throughput แต่คือ "air-cooled, ติดตั้งใน existing DC ได้โดยไม่ต้องลงทุน infra ใหม่" — barrier ในการ swap GPU → SN50 ต่ำมากในสายตา neocloud และ enterprise ที่ไม่อยากสร้าง data center ใหม่
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีม serve inference budget สูง ลอง quote SambaNova/Groq/Cerebras พร้อม GPU ใน RFP รอบหน้า — pricing competition กำลังเปิดและ vendor lock-in กับ CUDA ไม่ใช่ default ที่ปลอดภัยสำหรับ inference workload อีกต่อไป

## 5. YouTube เพิ่ม AI podcast features ให้ Premium — แนะนำ podcast, Auto Speed, on-the-go mode

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข 800 ล้านชั่วโมง podcast/เดือนใน April 2026 + 1 พันล้าน MAU คือ data ที่ใช้สอน digital media economics ได้ — YouTube กำลังกลายเป็น podcast platform ที่ใหญ่ที่สุดในโลกอย่างเงียบ ๆ
**ผู้เชี่ยวชาญด้าน AI:** "AI recommendation by genre, mood, shows you enjoy" คือ contextual bandit / collaborative filtering แบบ Netflix ที่นำมาใช้กับ long-form audio — ความท้าทายอยู่ที่ feature representation ของ audio (transcript, prosody, topic shift) มากกว่าตัวโมเดล
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ podcast หรือ video content รื้อ metadata strategy รอบใหม่ — เมื่อ recommendation algo อ่าน mood/genre/topic แล้ว tag ของคุณคือ feature ตรงที่ส่งผลกับ surface area ไม่ใช่แค่ title/description optimization แบบ SEO เดิม
