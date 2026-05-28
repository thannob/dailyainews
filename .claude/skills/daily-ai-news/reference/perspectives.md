# Perspectives — 2026-05-28

## 1. Cognition raises $1B at $25B pre-money valuation

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้ใช้สอนเรื่อง valuation multiples ของ AI startup ได้ตรง — $492M ARR ที่ $26B post-money = ราว 53x ARR; ให้นักเรียนเทียบกับ SaaS รุ่นพี่ที่ปกติเทรดที่ 10–15x ARR และตั้งคำถามว่า premium 3–5 เท่านี้สะท้อน "agent leverage" จริง หรือสะท้อน fear-of-missing-out ของ VC
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข enterprise usage โต 50% MoM ต่อเนื่อง 6 เดือนเป็น signal ว่า autonomous coding agent ผ่าน "demo → production" gap แล้ว และลูกค้าระดับ Goldman Sachs/NASA ใช้จริง — moat ของ Cognition ไม่ใช่โมเดล (ใคร ๆ ก็ใช้ Claude/GPT ได้) แต่คือ runtime + verifier + sandbox ที่ทำให้ agent ไม่ทำลายของ production
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมของคุณยังไม่มี policy เรื่อง agent-written code review/merge ปีนี้คือปีที่ต้องเขียน — Devin อยู่ใน CI/CD ของ Fortune-500 หลายรายแล้ว ภายในไม่กี่เดือนทีมคุณจะมี PR จาก agent เข้ามาด้วยไม่ว่าจะวางแผนหรือไม่

## 2. Meta launches Plus subscriptions for IG/FB/WhatsApp + AI tier coming

**อาจารย์ (มหาวิทยาลัย):** Meta อยู่ภายใต้กฎ DMA/GDPR ในยุโรปที่บีบให้ต้องมี "pay-or-consent" model — กรณีนี้คือ business-model laboratory สดของ post-ad-tracking era ดีสำหรับวิชา digital economy/regulation ใช้เทียบกับ Apple ATT (2021) ที่บังคับให้ Meta ปรับโครงสร้างรายได้รอบหนึ่งแล้ว
**ผู้เชี่ยวชาญด้าน AI:** บรรทัดที่น่าจับตาที่สุดไม่ใช่ $3.99/mo แต่คือ "additional subscription offerings for its AI" — Meta กำลังจะแยก AI feature ออกจาก feed default ทำให้ Llama-based assistant กลายเป็น paywall product เหมือน ChatGPT Plus คำถามคือ free tier ของ Meta AI จะถูก downgrade ขนาดไหน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ marketing/growth ที่พึ่ง Instagram organic reach เตรียมตัว — "wider audience reach" ที่ขายใน Plus tier หมายความว่า free post จะถูกบีบ algorithm ลงอีกชั้น; ถ้าทำ third-party automation บน WhatsApp Business API ต้องดูว่า WhatsApp Plus เปลี่ยน rate limit หรือ policy เรื่อง bot/AI integration หรือไม่

## 3. Robinhood lets AI agents trade stocks

**อาจารย์ (มหาวิทยาลัย):** กรณีคลาสสิกของ delegation ตามทฤษฎี principal-agent — ผู้ใช้ delegate authority ให้ AI agent ภายใต้ constraint ที่ออกแบบไว้ (dedicated wallet, pre-loaded balance) ใช้สอนใน fintech regulation course ได้ตรง คำถามชวนคิด: เมื่อ agent ขาดทุน ใครรับผิดชอบ — ผู้ใช้, Robinhood, หรือผู้สร้างโมเดล?
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่ Robinhood ทำคือ "capability sandboxing" — pre-loaded wallet จำกัด blast radius ของ misalignment เป็นรูปแบบที่ AI safety community พูดมานานว่าจำเป็นสำหรับ agent deployment ในโลกจริง น่าจับตาว่า throughput/slippage เมื่อมี autonomous agent เข้าตลาดพร้อมกันหลายแสน account จะเปลี่ยน microstructure ของหุ้นรายย่อยอย่างไร
**โปรแกรมเมอร์มืออาชีพ:** ถ้าสร้าง trading agent บน Robinhood API ใหม่ ออกแบบให้ idempotent ตั้งแต่แรก (ส่งคำสั่งซ้ำต้องไม่ trade ซ้ำ) และ log ทุก decision พร้อม reasoning trace — เมื่อ regulator มาถาม "ทำไม agent ขาย AAPL ตอน 03:42" คุณต้องตอบได้

## 4. China keeping its best AI talent at home (travel restrictions)

**อาจารย์ (มหาวิทยาลัย):** เคสนี้คือ talent-flow geopolitics ที่ตำราเศรษฐศาสตร์การพัฒนายังไม่ทันอัปเดต — เปรียบเทียบกับ Soviet-era exit visa หรือ Manhattan Project secrecy ได้ตรง สำหรับนักเรียน international relations: ช่องว่างประสิทธิภาพโมเดล US-CN ที่ลดจาก 31% (2023) → 2.7% (มี.ค. 2026) สะท้อนว่ามาตรการ export control ของสหรัฐช่วยชะลอแค่ฮาร์ดแวร์ ไม่ใช่ talent
**ผู้เชี่ยวชาญด้าน AI:** ข้อเท็จจริงสำคัญที่หลายคนมองข้าม: Stanford AI Index ใช้ benchmark ที่ส่วนใหญ่เป็นภาษาอังกฤษ ถ้าวัดบน benchmark ภาษาจีนหรือ multilingual ช่องว่างอาจกลับด้านอยู่แล้ว มาตรการ travel ban นี้บอกว่าจีนเชื่อว่าตัวเองอยู่ใน competitive position ที่คุ้มค่าจะปกป้อง human capital
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมเปิด collaboration กับนักวิจัย/วิศวกรในจีน ต้องคุยกันก่อนว่าใครออกประเทศ conference ได้ และมี approval process กี่วัน; ถ้าใช้ open-source model จากแล็บจีน (Qwen, DeepSeek) ตรวจ supply chain ของ weight + license terms อีกรอบ — เกิดสถานการณ์ที่นักวิจัยหลักไม่อยู่ในประเทศตัวเองชั่วคราวอาจกระทบ release cadence

## 5. Tech CEOs and "AI psychosis"

**อาจารย์ (มหาวิทยาลัย):** Aaron Levie กำลังบรรยาย principal-agent gap ในเวอร์ชัน intra-firm — CEO (principal) อยู่ห่างจาก last-mile work (ทำโดย agent คือพนักงาน) จนประเมิน capability ผิด ใช้กับ organizational behavior course ได้ดี เปรียบเทียบกับ McKinsey reports ที่อ้าง productivity gain 30-40% แต่ field study วัดได้จริง 5-10%
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข layoff 5 เดือนแรกของ 2026 = เกือบเท่าทั้งปี 2025 + อ้าง AI เป็นเหตุผล = signal ว่าหลาย CEO ตัดสินใจ headcount จาก demo มากกว่า measurement ที่น่าทำคือ track "AI-justified layoff" cohort หลัง 6-12 เดือนว่าบริษัทไหนต้อง rehire และในตำแหน่งไหน — นั่นคือข้อมูลจริงเรื่อง agent capability
**โปรแกรมเมอร์มืออาชีพ:** ถ้าหัวหน้าพูดว่า "agent จะทำแทนเราภายในไตรมาสนี้" ขอ benchmark concrete ก่อน: ตั๋ว Jira กี่ใบที่ปิดได้แบบ end-to-end, false-positive rate ของ PR เท่าไร, on-call alert ที่ agent วิเคราะห์ได้แม่นแค่ไหน ตัวเลขเหล่านี้คือ vaccine ต่อ AI psychosis ระดับ executive
