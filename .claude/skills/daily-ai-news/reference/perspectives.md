# Perspectives — 2026-07-17

## 1. China-led AI body (WAICO) enlists Global South ahead of Xi's WAIC keynote

**อาจารย์ (มหาวิทยาลัย):** นี่คือกรณีศึกษาสด ๆ ของ "AI governance เป็นเครื่องมือทางการทูต" — องค์กร WAICO ถูกออกแบบตามแม่แบบ Shanghai Cooperation Organization; ในคลาสวิชานโยบายเทคโนโลยี ควรใช้ควบคู่กับกรณี OECD AI Principles และ EU AI Act เพื่อให้เห็นสามขั้วกฎเกณฑ์ที่กำลังตั้งขึ้นพร้อมกัน.
**ผู้เชี่ยวชาญด้าน AI:** เนื้อในของประเด็นนี้ไม่ใช่โมเดล แต่คือ **สิทธิ์การกำหนดมาตรฐาน** — dataset licensing, model card format, safety evaluation protocols; ถ้ามาตรฐาน WAICO ต่างจาก NIST/ISO อย่างมีนัย บริษัทที่ deploy หลายเขตอำนาจจะต้องรัน governance stack แยกสองสามชุดขนานกัน.
**โปรแกรมเมอร์มืออาชีพ:** เตรียมใจว่า compliance layer จะเป็น first-class concern ไม่ใช่ afterthought — ระบบต้อง log ได้ว่าข้อมูล/โมเดลผ่านการตรวจตามชุดกฎใด (US NIST / EU / WAICO) เพื่อสามารถตอบ audit จากตลาดที่บริษัทขยายเข้าไปได้.

## 2. Moonshot Kimi K3 ตั้งเป้าไล่ Anthropic Opus 4.8

**อาจารย์ (มหาวิทยาลัย):** อีกหนึ่งหลักฐานว่า "open-weight จีน" ไม่ได้ตามหลังอีกต่อไป — สอนควบคู่กับกรณี DeepSeek R1 และ Qwen เพื่อให้นักเรียนเห็นว่า frontier gap ระหว่างจีน-ตะวันตกในทางเทคนิคหดจนน่าจะน้อยกว่า 6 เดือนแล้ว.
**ผู้เชี่ยวชาญด้าน AI:** สเปกที่รั่ว (2–3T MoE, 1M context) น่าสนใจตรงจุด long-horizon coding + agent workload; แต่ทั่ว community มีสัญญาณเตือน — "รุ่นออกก่อน paper" ทำให้ยัง benchmark เทียบไม่ได้แบบ apples-to-apples กับ Opus 4.8, และ MoE 2.5T ต้อง infra ขนาดใหญ่มากในการรัน inference แบบ self-hosted.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมใช้ Opus 4.8 อยู่แล้ว การ swap ทดสอบ K3 คุ้มเวลา — เพราะ K3 open-weight = ราคาต่ำกว่า closed model 5–10 เท่าตามประวัติราคา Moonshot; แต่ต้องทดสอบบน eval suite ของตัวเองก่อน production, อย่าเชื่อ "closes the gap" ตามพาดหัว.

## 3. Roblox "Build" — เกมสร้างด้วย prompt บนมือถือ

**อาจารย์ (มหาวิทยาลัย):** เป็นตัวอย่างที่ครูสอนเทคโนโลยีการศึกษาใช้ได้เลย — barrier-to-entry ของ "game dev" ลดจากเรียนเดือน เหลือพิมพ์ประโยคเดียว; แต่ต้องคุยเรื่องคุณภาพและปัญหา "AI slop" ให้จบเป็นชั่วโมงเรียนเดียว.
**ผู้เชี่ยวชาญด้าน AI:** จุดที่ควรเจาะคือ Roblox ประกาศตรง ๆ ว่าใช้ทั้ง proprietary + open-source models — น่าจะเป็นบริษัท consumer app รายแรก ๆ ที่โปร่งใสเรื่องการผสมโมเดล; และการจัด ranking ด้วย player retention เป็นทางแก้ moderation ที่น่าจับตา — ระบบเกรดตัวเองแทน human review.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมทำ user-generated content ให้ดูอย่างจริงจัง — pipeline "prompt → 3D scene → runnable code → ranking loop" ที่ Roblox โชว์ เป็น pattern ที่ transferable ไป vertical อื่น (education tools, marketing landing pages, prototyping); ปัญหา slop จะเป็นโจทย์ engineering ไม่ใช่ policy.

## 4. Google AI Mode รองรับ Connected Apps (Instacart / Canva / YouTube Music)

**อาจารย์ (มหาวิทยาลัย):** ประเด็นที่ควรสอนคู่กับข่าว DoorDash `dd-cli` — search engine กำลังเปลี่ยนจาก "index หน้าเว็บ" เป็น "orchestrator ของ agents ต่าง app"; เป็น shift ของ web architecture ในระดับที่เทียบได้กับ web 2.0 → mobile-first.
**ผู้เชี่ยวชาญด้าน AI:** technical story คือ Google กำลัง productize MCP-style connector patterns ใน consumer surface — ระดับ app store ไม่ใช่แค่ enterprise; ถ้าจับคู่กับ Search แล้วมี ecosystem ของ Connected Apps ที่ >100 apps ได้ในปีนี้ นี่คือ competitive moat ที่ ChatGPT/Claude จะไล่ยาก เพราะ query volume Google ยังใหญ่กว่า order-of-magnitude.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมทำ SaaS ควรถามคำถามตรง ๆ วันนี้: **เราต้อง onboard เป็น Connected App ไหม?** — เพราะการที่ user query "AI, สั่งเสื้อไซซ์ M สีดำ" แล้ว AI Mode ไม่รู้จัก app ของเรา = เสีย funnel; API contract ต้องพร้อมภายในไตรมาสหน้าถ้าคู่แข่งไปก่อน.

## 5. DoorDash `dd-cli` — สั่งอาหารจาก terminal สำหรับ AI agent

**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างที่จับต้องได้ที่สุดของ "software สำหรับ agent ไม่ใช่มนุษย์" — ทำ workshop ให้เด็ก computer science เขียน agent สั่งอาหารเองได้ในบ่ายเดียว, สอนทั้ง API design + agent framework + ethical concern เรื่อง autonomous purchases พร้อมกัน.
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นน่าสังเกต — DoorDash เลือก CLI ก่อน API-only เพราะ CLI เหมาะกับ agent orchestration frameworks (Claude Code, Cursor agent, etc.) ที่มี tool-invocation loop อยู่แล้ว; นี่คือ signal ว่า vendor consumer เริ่มมองว่า distribution channel ใหม่คือ agent runtime ไม่ใช่ mobile app store.
**โปรแกรมเมอร์มืออาชีพ:** โอกาสจริงคือ **integration layer** — สร้าง agent workflow ที่เชื่อม `dd-cli` + calendar + payment + budget guardrail ให้ผู้ใช้ปลายทาง; แต่ต้อง engineer safety rail (spending cap, confirmation step) แน่นหนา เพราะ CLI ของเจ้าอื่นในอนาคตจะไม่ได้เชื่อถือได้เท่ากันหมด.
