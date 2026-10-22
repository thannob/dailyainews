# Perspectives — 2026-10-22

## 1. Anthropic launches Claude Duet research preview

**อาจารย์ (มหาวิทยาลัย):** Claude Duet เป็นก้าวสำคัญจาก "ผู้ช่วยที่รอคำสั่ง" ไปสู่ "ตัวแทนที่คิดและริเริ่มเอง" ซึ่งเป็นหัวข้อที่ต้องสอนในวิชา Human–AI Interaction อย่างจริงจัง นักเรียนควรฝึกออกแบบ consent gate และ fail-safe mechanism เมื่อ AI มีสิทธิ์ลงมือทำแทนเราในเรื่องการเงินและเอกสาร
**ผู้เชี่ยวชาญด้าน AI:** การที่ Duet ขอ permission ก่อนส่งข้อความ จ่ายเงิน หรือลบไฟล์ สะท้อนว่า Anthropic จงใจออกแบบ asymmetric autonomy — ให้ agent อ่าน/วิเคราะห์ได้อิสระ แต่ action ที่กลับไม่ได้ต้องมีมนุษย์ยืนยัน รูปแบบนี้จะกลายเป็น baseline ของอุตสาหกรรมเมื่อ long-running agent เพิ่มขึ้น
**โปรแกรมเมอร์มืออาชีพ:** งานประเภท on-call rotation, inbox triage, และการตามงานข้ามเครื่องมือ (Linear/Slack/GitHub) จะถูก compress ลงอย่างรวดเร็วถ้า Duet ทำงานได้จริงอย่างที่โฆษณา แต่ก่อนจะปล่อยให้มันเชื่อม production ควรกำหนด scope ของ connected apps และตั้ง alert เมื่อมี tool call ที่เกิน budget รายวัน

## 2. OpenAI models are coming to Google Cloud

**อาจารย์ (มหาวิทยาลัย):** ดีลนี้เป็นตัวอย่างคลาสสิกของ co-opetition ที่ควรสอนในวิชา strategic management — คู่แข่งโดยตรงของ Gemini ยอมเปิด Model Garden ให้ลูกค้าซื้อ GPT ได้ สะท้อนว่า distribution channel สำคัญกว่าการปกป้องผลิตภัณฑ์เดี่ยว นักเรียนควรเทียบกับกรณี Apple ยอมใส่ Google Search เป็น default บน Safari
**ผู้เชี่ยวชาญด้าน AI:** การที่ OpenAI มีช่องทางจำหน่ายผ่าน AWS, Azure, และตอนนี้ Google Cloud ครบทั้งสาม hyperscaler หมายความว่ายุคของ "exclusive cloud partnership" จบลงอย่างเป็นทางการ และ model routing / cost arbitrage จะกลายเป็นงานทาง engineering ที่สำคัญกว่าการเลือก vendor
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ตัดสินใจแล้วว่าใช้ GCP เพื่อ data pipeline แต่เลือก Azure OpenAI เพราะไม่มีทางเลือก ตอนนี้สามารถเรียก GPT ผ่าน Model Garden ได้ ลดความซับซ้อนของ IAM, egress cost, และ VPC peering ลงได้มาก และยัง burn Google Cloud commit ที่เหลือได้ด้วย

## 3. NVIDIA debuts OpenShell Reference Architecture at GTC Berlin

**อาจารย์ (มหาวิทยาลัย):** OpenShell ยกระดับ "AI safety" จากหัวข้อ ethics ไปสู่ engineering concrete — ใช้ hardware isolation (BlueField-4), kernel-level sandbox, และ policy YAML เป็นชั้นเดียวกันที่ enforce ได้จริง เหมาะเป็น case study ให้นักเรียน CS ที่เรียน OS/Security ได้เห็นว่า agent safety ไม่ใช่แค่เรื่อง alignment ของโมเดล
**ผู้เชี่ยวชาญด้าน AI:** การวาง Sentry ลงบน DPU แยกจาก host CPU สำคัญมาก เพราะหมายความว่า agent ที่ถูก prompt-inject ให้ปิดระบบ monitoring จะไม่สามารถทำได้ — observer อยู่คนละชั้น trust domain เลย ที่เหลือคือดูว่า partner (Anthropic, OpenAI โดยไม่เปิดเผย) จะยอมใช้ container stack ของ NVIDIA ในระดับไหน
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่กำลัง deploy agent บน on-prem หรือ edge การมี reference architecture ที่พร้อม production (Rubin + Vera + BlueField) ลด integration cost ลงมาก แต่ควรประเมิน vendor lock-in ให้ดี เพราะทั้ง stack ยัง proprietary อยู่ยกเว้นตัว OpenShell runtime
