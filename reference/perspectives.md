# Perspectives — 2026-10-03

## 1. Apple ขัน Full Disk Access บน macOS รับมือ AI agent

**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษาตรงจุดในวิชา OS/security — permission model ที่ออกแบบไว้สำหรับ "โปรแกรม backup ทำงานได้" ถูก AI agent generation ใหม่ repurpose เป็นช่องทางอ่าน mail, messages, browsing history แบบไม่มี consent granular; สอนให้เห็นว่า threat model ปี 2020 อายุไม่ถึง 6 ปี ก็ล้าสมัยเพราะ actor profile เปลี่ยนจาก "โปรแกรมที่ user เลือกเอง" เป็น "agent ที่ user เพียง delegate เป้าหมาย"
**ผู้เชี่ยวชาญด้าน AI:** จุดสำคัญคือ Apple ยอมรับว่า "ความเสี่ยงเพิ่มขึ้นอย่างมีนัยสำคัญ" จาก AI agent — เพราะ agent เรียก API นี้ซ้ำ ๆ โดย user ไม่ทันเห็นแต่ละครั้งว่าอ่านอะไร; ปัญหาเชิง alignment ไม่ใช่แค่ model แต่คือ **permission system รอบนอก model** ที่ไม่ได้ออกแบบให้ถาม consent ต่อ action ไม่ใช่ต่อ install
**โปรแกรมเมอร์มืออาชีพ:** macOS dev ที่ขอ Full Disk Access สำหรับ feature AI assistant ต้องเตรียมเปลี่ยน UX — "explicit user action per session" น่าจะหมายถึง re-authorize ทุกครั้งที่ app เปิดใหม่ หรือทุก N นาที; ควรทบทวนว่า agent features จริงต้องการ full disk หรือใช้ scoped bookmark + user-granted folder ก็พอ และเริ่ม refactor เผื่อ ก่อน Apple ปล่อย beta เอง

## 2. Broadcom ระดม $60B หา chip ให้ Anthropic

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข $125.2B lease 5 ปีของ Anthropic คือ **capital intensity ของ AI frontier lab** ที่สูงกว่าอุตสาหกรรม chip, airline, telecom รวมกัน; สอนให้นักเรียน finance เห็นว่าเมื่อ marginal cost ของ inference ต่ำแต่ fixed cost ของ training infrastructure สูงมหาศาล business model จะย้ายไปทาง utility (ขายต่อเนื่องตามการใช้) ไม่ใช่ product (ขายเป็นหน่วย)
**ผู้เชี่ยวชาญด้าน AI:** การที่ Anthropic ย้าย compute หนักไปที่ Broadcom TPU-style ASIC (ไม่ใช่ NVIDIA) คือสัญญาณว่า **inference workload ของ Claude** ถูก optimize จนทำงานบน custom silicon คุ้มกว่า general-purpose GPU; เทรนด์นี้ทำให้ performance per dollar ของ frontier model จะต่างกันตาม silicon partner มากขึ้น ไม่ใช่แค่ algorithm อีกต่อไป
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build บน Claude API — รอดู latency/pricing change ปี 2027 เมื่อ Broadcom capacity online จริง; team ที่ cost-sensitive ควรเตรียม abstract layer ให้ switch provider ได้ (OpenAI/Anthropic/Google) โดยไม่ต้อง rewrite — vendor lock-in ที่ compute capacity ไม่พอ จะทำให้ pricing power อยู่ที่ provider ไม่ใช่ customer

## 3. Trump เตรียมตั้ง Jay Clayton เป็น AI Czar

**อาจารย์ (มหาวิทยาลัย):** การควบตำแหน่ง DNI (national intelligence) + AI czar ในคนเดียวเป็น case study น่าสอนในวิชา public administration — merge หน้าที่ security intelligence (classified, defensive) กับ industrial policy (public-facing, promotional) ในคนเดียวจะสร้าง conflict of interest ที่ตรวจสอบยาก; เทียบกับ David Sacks ที่ลาเพราะข้อจำกัด special-government-employee บทเรียนคือรัฐบาลเลือก revolving door แบบไหน model governance ก็เป็นแบบนั้น
**ผู้เชี่ยวชาญด้าน AI:** การแต่งตั้งเกิดไม่กี่วันหลังพบ Jensen Huang + Dario Amodei ที่ White House lunch ว่าด้วย safety — Clayton ไม่มี track record ด้าน AI safety แต่มี network กับ intelligence community; สัญญาณคือ Trump จะมอง AI safety ผ่าน lens ของ national security (export control, model weight protection) มากกว่า consumer harm (bias, misinformation)
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ ship model หรือ weights ไป international market ต้องจับตา export control update ครึ่งแรก 2027 — Clayton จาก intelligence community น่าจะ push ให้ขยาย CFIUS/EAR cover model artifact มากกว่าปัจจุบัน; team ที่มี customer จีน/ตะวันออกกลาง เตรียม compliance review ว่า weights distribution ที่ทำอยู่ ถ้าโดน rule ใหม่ ต้อง re-architect อย่างไร

## 4. Shinhan Bank โดนแฮกด้วย AI tool — 25,000 ลูกค้ากระทบ

**อาจารย์ (มหาวิทยาลัย):** credential stuffing ไม่ใช่เทคนิคใหม่ แต่ **AI-powered credential stuffing** ย้ายการโจมตีจาก "ทดสอบ password list ทีละชุด" เป็น "generate variants + bypass rate limiting + solve CAPTCHA ตามจังหวะ bank"; สอนให้เห็นว่า defender assumption ที่ว่า "attacker จะช้าพอให้ WAF จับได้" กำลังหมดอายุ — threat model ต้องปรับให้ assume attacker มี unlimited concurrency + context-aware behavior
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นสำคัญคือข้อมูลที่หลุด (resident registration number 66 ราย + income + borrow limit) เพียงพอทำ synthetic identity fraud ต่อเนื่องได้; AI tool ที่ช่วย attack ยังช่วย process ข้อมูลที่ขโมยได้ออกมาเป็น identity package ขาย dark market ด้วย; ธนาคารต้องรองรับ scenario ว่าข้อมูลที่หลุดจะกลับมาเป็น attack surface อีกครั้งใน 6-12 เดือน
**โปรแกรมเมอร์มืออาชีพ:** sysadmin ธนาคารไทย — review loan/credit platform ว่าแยก auth จาก deposit system จริงไหม (Shinhan ถูกเจาะที่ loan-broker ไม่ใช่ core banking), เพิ่ม **passkey/FIDO2** แทน password สำหรับ customer-facing portal, เปิด **anomaly detection ที่ session-level** ไม่ใช่แค่ IP-level เพราะ AI-powered attack จะ rotate IP ให้ดูเหมือน legitimate user; audit log ต้องเก็บ behavioral signal (typing cadence, mouse pattern) สำหรับ post-mortem forensic

## 5. Microsoft MAI-Voice-2.1 รองรับภาษาไทย

**อาจารย์ (มหาวิทยาลัย):** การขยาย TTS จาก 15 เป็น 23 ภาษาในรุ่น 2.1 โดย single speaker identity สลับภาษาได้พร้อม native accent เป็นก้าวสำคัญของ **multilingual speech synthesis** — ตอน education ทำได้คือสอน content ด้วย voice ของอาจารย์คนเดียวแต่ render หลายภาษาสำหรับ international student; สอนให้เห็นว่า voice เริ่มกลายเป็น "ภาษา-neutral asset" ที่ brand/บุคคล own ได้
**ผู้เชี่ยวชาญด้าน AI:** $22 per 1M characters สำหรับ MAI-Voice-2.1 (vs ElevenLabs ~$80/M, OpenAI TTS-HD ~$30/M) + MAI-Voice-2.1-Flash ที่ latency 150ms ทำให้ Microsoft แข่งราคา aggressive; ประเด็นที่ต้อง watch คือ error rate 2.5% ของ MAI-Transcribe-2-Streaming จริงบน Thai accent — benchmark ที่ Microsoft publish มักไม่ representative ของ dialect ภูมิภาคเหนือ/อีสาน/ใต้
**โปรแกรมเมอร์มืออาชีพ:** dev ไทยที่ใช้ TTS/STT อยู่ (contact center, voice bot, accessibility) ลอง benchmark เทียบกับที่ใช้อยู่ (Google, OpenAI, Microsoft เดิม) ภายในสัปดาห์นี้ — ถ้าได้ quality พอ ประหยัด cost 30-60% มี impact ชัดต่อ unit economic; MAI-Voice-2.1-Flash 150ms เหมาะกับ real-time use case เช่น voice assistant, live interpreter; ลงทะเบียน OpenRouter/Azure Voice Live ก่อนเริ่ม production
