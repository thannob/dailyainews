# Perspectives — 2026-07-31

## 1. Reddit Q2 solid but AI Overviews erode search referrals

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ให้เห็นว่ารายได้บริษัท (+61% YoY) กับสุขภาพ traffic ระยะยาวเป็นคนละมิติ — สอนนักเรียนวิเคราะห์งบว่าตัวเลขไหนคือ leading indicator (referral traffic) ตัวเลขไหนคือ lagging indicator (ad revenue) และทำไมตลาดหุ้นให้ราคาคนละแบบกัน
**ผู้เชี่ยวชาญด้าน AI:** AI Overviews กำลังเปลี่ยน search จาก link economy เป็น answer economy — Reddit CEO ยอมรับตรง ๆ ว่า referrals "choppy" ในไตรมาส; ข้อสังเกตทางเทคนิคคือ Google ยัง crawl Reddit เข้า summary แต่ user ไม่คลิกต่อ ทำให้ content producer สร้างมูลค่าให้ Google โดยไม่ได้ traffic กลับ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าเว็บหรือ product ของทีมพึ่ง search referral (SEO / content marketing) ให้ถือว่า traffic funnel นั้นกำลังหดเป็น structural trend ไม่ใช่แค่ noise ไตรมาสเดียว — เริ่มลงทุน direct channel (newsletter, app, community) ตั้งแต่วันนี้

## 2. Google Chrome — 1,072 security bugs fixed via AI (Big Sleep + CodeMender)

**อาจารย์ (มหาวิทยาลัย):** ใช้เปิดคลาส security engineering + AI สมัยใหม่ — 1,072 bugs ใน 2 releases สูงกว่า 23 releases ก่อนหน้ารวมกัน; ให้นักเรียนถามต่อว่า "ทำไม bug จำนวนมากถูกซ่อนอยู่ในโค้ดนานหลายปี" คำตอบไม่ใช่วิศวกร Google ไม่เก่ง แต่ scan capacity ไม่พอต่อ codebase ขนาดนี้ — AI เปิด ceiling ของสิ่งที่ scan ได้
**ผู้เชี่ยวชาญด้าน AI:** เห็น production-grade agent ที่ทำงานลึกใน security pipeline จริง — Big Sleep + CodeMender วิ่งใน Chrome CI ทุก 24 ชั่วโมงบนทุก code change; นี่คือ pattern "AI ในลูป CI" ไม่ใช่ทดลอง lab. Signal ที่สำคัญคือ Google ยอมเปิดเผยตัวเลขเชิงบวก — เพราะกำลัง reframe narrative ว่า AI = ช่วย security ไม่ใช่ทำลาย security ท่ามกลางข่าว OpenAI เจาะ Hugging Face
**โปรแกรมเมอร์มืออาชีพ:** ถ้ายังไม่มี AI security scanner ใน CI ของทีม พิจารณา CodeQL, Semgrep, หรือ Big Sleep เมื่อ Google เปิด — แต่ผลของ AI scanner สร้าง signal noise สูง; ต้องมี triage rubric ที่ทีม security review ได้ในเวลาที่ scale ไหว ไม่งั้นได้ 1,072 bug report แล้วไม่มีคนอ่าน

## 3. Judge — Trump admin lacks evidence for Anthropic supply-chain risk label

**อาจารย์ (มหาวิทยาลัย):** เปิดคลาส AI policy + procurement — Anthropic ปฏิเสธ mass surveillance และการใช้กับ lethal weapon เพราะระบุใน usage policy; Pentagon แย้งว่า private company ไม่ควรกำหนดวิธีใช้ของทหาร; ให้นักเรียนถกว่า "AI safety commitment ของบริษัท" กับ "อำนาจของรัฐในการซื้อและใช้" ควรหยิบยืมสมดุลแบบไหน
**ผู้เชี่ยวชาญด้าน AI:** เป็น legal test case แรกที่เห็นว่า **AUP (Acceptable Use Policy) ของ frontier lab มีน้ำหนักในศาลจริง** — จนถึงตอนนี้ AUP เป็นเอกสารตลาด ไม่มี enforcement mechanism ที่ชัด; ถ้าผลออกมาว่ารัฐบาลบังคับใช้ AI นอก AUP ไม่ได้ frontier lab อื่น (OpenAI/Google/Meta) จะเห็น precedent ว่า AUP เป็น shield ต่อ overreach ของรัฐ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าเป็น vendor B2B ที่ให้บริการ AI ต่อภาครัฐหรือลูกค้าองค์กรใหญ่ ทบทวน AUP ให้ enforce ได้จริง (rate limit / API scope / audit) — เพราะคดีนี้พิสูจน์ว่า AUP ไม่ใช่แค่ boilerplate ผู้ซื้อขนาดใหญ่จะเริ่มอ่านและ push back; อย่าตั้ง AUP ที่ enforce ไม่ได้เพราะจะโดนใช้เป็นหลักฐานว่าบริษัทไม่ serious

## 4. Simile — $200M Series B at $2B for "agentic twins" of consumers

**อาจารย์ (มหาวิทยาลัย):** เปิดคลาส market research + AI — Simile บอกว่าทำ "agentic twin" จำลอง user ได้ 85–99% accuracy; ให้นักเรียนถามว่า accuracy คำนวณเทียบอะไร (survey response? behavior in real world?) และวิธี validate คืออะไร — ตัวเลข accuracy ที่ไม่มี denominator ที่ชัดคือคำโฆษณา ไม่ใช่ evidence
**ผู้เชี่ยวชาญด้าน AI:** synthetic user มี generative history ตรงจาก Smallville paper ของ Joon Sung Park — simulation ที่ดู emergent behavior; ประเด็นเชิงเทคนิคที่ต้องจับตาคือ **generation-vs-recall trade-off** — model อาจสร้าง response ที่ดู realistic แต่สะท้อน training data มากกว่า population ที่กำลังจะทำ market research; ถ้า marquee customer อย่าง CVS/Deloitte ใช้ตัดสินใจ product ใหญ่ ๆ นี่คือ epistemic risk ที่ยังไม่มี consensus จะ audit อย่างไร
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีม product ใช้ synthetic user แทน user research จริง ให้ mix ไม่ใช่แทน — synthetic user เร็วและถูก ใช้ทำ hypothesis generation ได้ดี แต่การ validate ต้องเจอ user จริงก่อน launch; อีกด้าน ถ้าทำ AI application ให้ SME ลอง Simile หรือ open-source equivalent (มี generative agent library หลายตัว) เพื่อ prototype UX ก่อนใช้เวลากับ user จริง — ประหยัดเวลา discovery phase 2-4 สัปดาห์

## 5. Situational Awareness LP forced-sold to Citadel, kept Anthropic

**อาจารย์ (มหาวิทยาลัย):** เคสหายากที่รวม leverage + concentration + AI narrative ในเรื่องเดียว — 4x leverage บน AI stock, ARR ของกองทุนขึ้นถึง 1,000% ก่อน crash; ให้นักเรียนคำนวณ margin call trigger เอง และถกกันว่า risk management ของ prime broker (Goldman/JPM/BofA) ควรมี concentration limit สำหรับ single-theme fund หรือไม่
**ผู้เชี่ยวชาญด้าน AI:** ข้อมูล signal ที่สำคัญคือ Aschenbrenner **เก็บ Anthropic ไว้** (สินทรัพย์ ~$4B หรือ ~20% ของ fund) แม้ต้องเทหุ้นสาธารณะทั้งหมด — สื่อว่าถือ AI safety lab เป็น long-tail bet ที่แยกจากเทรด momentum ของ public AI stock; ยืนยัน narrative ว่า valuation Anthropic ที่ ~$965B ถูกมองว่าเป็น structural position ไม่ใช่ trade
**โปรแกรมเมอร์มืออาชีพ:** ไม่กระทบ engineering ตรง ๆ แต่ downstream: (1) ถ้า public AI stock rout ต่อเนื่อง infra spend ในสตาร์ทอัพ AI ที่พึ่ง VC จะโดนตัด — เตรียม runway forecast ที่ pessimistic; (2) ถ้าใช้ AI vendor ที่เพิ่ง raise รอบใหญ่ให้ตรวจ contract term เรื่อง price change / service depreciation ในไตรมาสหน้า เพราะ vendor อาจต้อง raise price หลังตลาดหด
