# Perspectives — 2026-07-11

## 1. Apple sues OpenAI over alleged trade secret theft

**อาจารย์ (มหาวิทยาลัย):** เคสนี้จะเป็นวัตถุดิบชั้นดีของวิชา tech law และ innovation policy ไปอีกหลายปี — ประเด็นคือเส้นแบ่งระหว่าง "ความรู้ที่พนักงานพาไปด้วย" กับ "ความลับทางการค้า" กำลังถูกทดสอบใหม่ในยุคที่ product roadmap ของบริษัทหนึ่งกลายเป็น starting point ของอีกบริษัท.
**ผู้เชี่ยวชาญด้าน AI:** ที่น่าสังเกตคือ Apple ไม่ได้ฟ้องเรื่องโมเดลหรือ weights แต่ฟ้องเรื่อง **hardware design** — สะท้อนว่า race ของ AI ปี 2026 เคลื่อนไปสู่ device layer แล้ว, และ Jony Ive/OpenAI hardware team คือคู่ต่อกรตรงของ Apple มากกว่า ChatGPT-vs-Siri.
**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบระยะสั้นสำหรับ engineer ที่ย้ายระหว่างบริษัท AI คือ NDA และ non-solicit clause จะถูกเขียนใหม่ให้เข้มขึ้น — ถ้าอยู่ FAANG แล้วมองย้ายไป lab AI ให้เตรียมล่วงหน้าเรื่อง garden leave, laptop return, และห้ามใช้ personal email รับ work document; hygiene เหล่านี้จะกลายเป็นเรื่องปกติ.

## 2. SK Hynix raises $26.5B in the biggest foreign IPO in US history

**อาจารย์ (มหาวิทยาลัย):** IPO ระดับนี้เป็น teaching moment ของ macro-finance × industrial policy — ทำไม memory-chip vendor จากเกาหลีถึงเลือก Nasdaq มากกว่า KOSPI และทำไม US ถึงกดดันให้ SK Hynix สร้าง fab ในสหรัฐ; คำตอบเชื่อมโยง CHIPS Act, geopolitical risk premium, และ HBM supply chain ที่เข้มข้นในไม่กี่ราย.
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข 7× oversubscribed บอกว่าตลาดยังเชื่อว่า HBM demand จะไม่ collapse ใน cycle นี้ — แต่ประวัติศาสตร์ chip cycle เตือนว่า boom ทุกครั้งจบด้วย glut; risk indicator ที่ควรจับตาคือ (1) HBM inventory day ของ NVIDIA/AMD, (2) ราคา DDR5 spot vs. contract, (3) capex guidance ของ hyperscaler ปีหน้า.
**โปรแกรมเมอร์มืออาชีพ:** ไม่กระทบ workflow ตรง ๆ แต่กระทบราคา cloud GPU ทางอ้อม — ถ้า HBM supply ยังตึงต่อ, on-prem inference บน commodity GPU และ open-weight model (Ollama pattern จากเมื่อวาน) จะยิ่งคุ้มกว่า renting frontier API สำหรับ workload token-heavy.

## 3. Meta pulls Muse Image AI feature on Instagram after backlash

**อาจารย์ (มหาวิทยาลัย):** case study ตรงตัวสำหรับวิชา AI ethics / product-launch decision — Meta มี internal review เป็นเดือน ๆ แต่ยังปล่อยฟีเจอร์ที่ไม่แจ้งเจ้าของภาพว่าถูกใช้; สะท้อนช่องว่างระหว่าง legal-compliance ("public account = fair use") กับ social contract ที่ user คาดหวัง.
**ผู้เชี่ยวชาญด้าน AI:** ปัญหาที่แท้จริงไม่ใช่โมเดล แต่คือ **default consent architecture** — เมื่อ image generator เข้าถึง reference image ของบุคคลจริงได้แบบ programmatic, ทุกภาพในบัญชี public จะกลายเป็น "training-time reference" โดย opt-out ล่าช้าเสมอ; SAG-AFTRA เจอเรื่อง likeness ก่อนหน้านี้แล้ว, รอบนี้แค่ scale ใหญ่ขึ้น.
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้าง generative feature ควรเช็ค checklist ก่อน launch: (1) ถ้า model ใช้ user content เป็น input, มี explicit opt-in ต่อผู้ถูก reference ไหม, (2) มี inbound signal (notify/audit log) ให้เจ้าของ content เห็นการ use ไหม, (3) rate-limit + abuse pipeline พร้อมไหม; ข้ามข้อไหนข้อหนึ่ง = ready to be pulled ภายในสัปดาห์.

## 4. Hugging Face CEO: companies are done renting their AI

**อาจารย์ (มหาวิทยาลัย):** เป็นเคส classic "unbundling → rebundling" ของ platform economics — ยุคแรก API ชนะเพราะ integration cost ต่ำ, ยุคต่อไป open-weights ชนะเพราะ scale cost ต่ำ; แต่คำถามที่ยังไม่ชัดคือ enterprise มี **skill** ทั้ง MLOps และ security-hardening สำหรับ self-host หรือไม่.
**ผู้เชี่ยวชาญด้าน AI:** Delangue ไม่ได้พูดผิด — cost curve ของ frontier API สำหรับ workload token-heavy (agent, RAG, batch summarization) โตเร็วกว่า on-prem inference อย่างเห็นได้ชัด; แต่ควรระวัง narrative bias เพราะ Hugging Face เป็นเจ้าของ distribution ของ open-weights; **eval quality gap** ระหว่าง open และ frontier ยังมีอยู่จริงในหลาย task (long-context reasoning, tool-calling reliability).
**โปรแกรมเมอร์มืออาชีพ:** ทำ **cost model จริง** สัปดาห์นี้: token throughput ต่อเดือน × ราคา frontier API vs. TCO ของ on-prem GPU + engineer time. ถ้า workload อยู่ในช่วง 10-500B token/เดือน, break-even ของ self-host มักมาถึงเร็วกว่าที่คิด — เริ่มด้วย hybrid: frontier สำหรับงานยาก, open-weight บน Ollama/vLLM สำหรับ bulk.

## 5. Big Tech doubles debt load to $350B in the AI spending spree

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข $350B บ่งชี้การเปลี่ยน capital structure ครั้งใหญ่ — Big Tech เคยเป็นบริษัท debt-light แคช-หนัก, ตอนนี้กลายเป็น capital-intensive builder แบบ utility/telco เก่า; หัวข้อ finance-class ที่ควรสอนคือ AI capex ยังนับเป็น "growth investment" หรือกลายเป็น "recurring maintenance cost" ที่กด margin ระยะยาว.
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณสำคัญคือ debt-fund ถูกใช้กับ **data-center + power + interconnect** ไม่ใช่ R&D — ยืนยันว่า scale bottleneck ปี 2026-2027 คือไฟฟ้าและ HBM supply, ไม่ใช่ algorithm; ทีมที่วางกลยุทธ์ compute ควร lock capacity commitment ล่วงหน้าอย่างน้อย 12-18 เดือน.
**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบทางอ้อม — cloud AI service ราคาจะ **ไม่ลง** เร็วเท่าที่คาด เพราะ hyperscaler ต้อง service debt ก้อนใหญ่; workload ที่ตั้งงบไว้ตาม assumption "AI ราคาลด 50% ทุก 12 เดือน" ต้องรีวิว; hedge ด้วย open-weight fallback path ในทุก production critical path.
