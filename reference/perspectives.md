# Perspectives — 2026-11-22

## 1. A tale of two Nvidias — earnings vs. stock vs. Huang-return petition

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็นตัวอย่างชั้นเรียน corporate governance ที่ดี — แยก "performance of the business" (Q3 earnings แข็งแรง) ออกจาก "performance of the stock" (ร่วงต่อเนื่อง) และจาก "legitimacy of the leadership" (petition เรียก Huang กลับ vs. board ยืนยัน exit ถาวร) ให้ชัดเจน ให้นักเรียนวาด decision tree ว่าถ้าเป็น interim CFO Colette Kress ควรจัดลำดับความสำคัญระหว่าง execution, communication, และ culture reset อย่างไร
**ผู้เชี่ยวชาญด้าน AI:** การยุติการขาย H200 ไปจีนคือการปิด loophole ที่ใช้ US re-export + 25% tariff เป็นทางผ่าน ซึ่งหมายความว่า China AI stack จะพึ่ง Huawei Ascend/SMIC และ domestic model ingestion มากขึ้น — ประเด็น technical ที่ต้องจับตาคือ gap ทางด้าน interconnect (NVLink/CX7) และ CUDA ecosystem ไม่ใช่แค่ FLOPS ของ GPU ซึ่งเป็นเหตุผลที่ transitional period 12–24 เดือนจะ stressful กว่าจำนวน tokens/sec ที่รายงาน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมของคุณ deploy training ใน China region อยู่แล้ว ให้ตรวจ cluster roadmap ของ cloud provider ว่าสำรองไว้ด้วย B200/B300 (ที่ยังขายได้) หรือต้องสลับไป AMD/Huawei — การวางแผน cutover ต้องเริ่มไตรมาสนี้ ส่วน dev ที่อยู่นอกจีนจะได้ประโยชน์ทางอ้อม เพราะ Nvidia จะหันไปขาย inventory ที่เหลือใน US/EU/APAC ทำให้ queue ลดลง 1–2 สัปดาห์

## 2. Signal restricts mobile screenshots to counter agentic-AI "existential threat"

**อาจารย์ (มหาวิทยาลัย):** น่าเอาไปใช้ในวิชา HCI/privacy — OS-level agent ที่อ่าน screen ของทุก app โดย default เป็น architectural change ไม่ใช่แค่ feature ใหม่ เปรียบเทียบกับ accessibility service บน Android ในอดีตที่ถูก abuse สำหรับ overlay malware — model mental "trust boundary" ของผู้ใช้ส่วนใหญ่ยังไม่เคยคิดว่า "app ที่ฉันเปิดอยู่ = ข้อมูลที่ OS agent เห็นด้วย"
**ผู้เชี่ยวชาญด้าน AI:** จุดที่ Whittaker ยิงถูกคือ documentation gap — ไม่ชัดว่า screenshot ที่ agent เอาไป process อยู่บน-device หรือส่ง server เพราะ hybrid inference ของ Gemini/Apple Intelligence ทำให้ model routing เปลี่ยนตาม load; สิ่งที่ community ต้องการคือ attestable boundary (SEV-SNP/TDX + remote attestation) ไม่ใช่ marketing wording "processed locally when possible"
**โปรแกรมเมอร์มืออาชีพ:** ถ้า app ของคุณถือ sensitive data ให้พิจารณา FLAG_SECURE (Android) / UIScreen.capturedDidChangeNotification + obscure overlay (iOS) ทันที — เพิ่ม 10–20 บรรทัด ป้องกันทั้ง screen recording ของ OS agent, user screenshot, screen mirroring และ accessibility abuse ได้ครอบคลุม; อย่ารอให้ compliance บังคับ

## 3. Wall Street asks what can save the AI trade after Anthropic wipeout

**อาจารย์ (มหาวิทยาลัย):** บทเรียน behavioral finance — "catalyst-that-wasn't" คือสัญญาณที่ sentiment พลิก IPO ขนาด historic ที่ตั้งใจให้เป็น re-ignition กลับกลายเป็น accelerator ของ sell-off = ตลาดเลิก price ความคาดหวังเดิมแล้ว ใช้ร่วมกับทฤษฎี Minsky moment สอนนักศึกษาปริญญาตรีเรื่อง displacement → boom → euphoria → profit-taking → panic
**ผู้เชี่ยวชาญด้าน AI:** สัปดาห์ที่แย่ที่สุดของ Nasdaq-100 ตั้งแต่มี.ค. 2020 ส่งผลระยะยาวต่อ capex cycle: hyperscaler อาจชะลอ data-center build-out 1–2 ไตรมาส → การเทรน frontier model รุ่นถัดไปของ OpenAI, Anthropic, Google ต้อง re-priotize; GPU demand ลดลง ⇒ allocation สำหรับ academic/independent researcher อาจกลับมา (ข่าวดีของการวิจัย open-weight)
**โปรแกรมเมอร์มืออาชีพ:** Diversify dependencies เลย — abstraction layer ที่พูดถึงเมื่อวานไม่ใช่เรื่องรองอีกต่อไปแล้ว ถ้า Anthropic ต้องขึ้น price หรือ limit rate เพื่อ defend margin, provider switch time = ความอยู่รอดของ product; ตั้ง monthly cost alert และ budget headroom 30% สำหรับทุก LLM-dependent service

## 4. The SMS-native AI agent category: Poke, Folk, Fambot, Stanley, Town

**อาจารย์ (มหาวิทยาลัย):** นี่เป็น case study การ "unbundling" interface — AI ที่ไม่ต้อง launch app ใหม่ กลับไปใช้ SMS/iMessage ที่ผู้ใช้เปิดอยู่แล้ว 100+ ครั้ง/วัน ให้นักเรียน UX ออกแบบ conversation flow ที่ constraint ด้วย 160 อักขระ + ไม่มี rich UI — เป็น discipline training ที่ web/app นักออกแบบรุ่นใหม่ขาด
**ผู้เชี่ยวชาญด้าน AI:** ช่องนี้คือ latency + cost battleground จริง — SMS → NLU → tool-use → reply ต้องเสร็จภายใน 2 วิเพื่อไม่เสียความรู้สึก "chatting"; จะเห็นการใช้ Haiku-class / small-model-first + conditional escalate ไป frontier model กลายเป็น default architecture
**โปรแกรมเมอร์มืออาชีพ:** Twilio Programmable Messaging + webhook → LLM pipeline สร้างได้ภายในสุดสัปดาห์ ลงทุนต่ำ แต่ระวังเรื่อง A2P 10DLC registration (US), 2-way carrier compliance, และ opt-out keyword handling (STOP/UNSUBSCRIBE) — ถูก carrier ban ทั้ง brand ถ้าทำผิด; ไทยใช้ SMS gateway ของ AIS/True ต้องผ่าน content screening ของ NBTC ก่อน

## 5. Microdrama startup Shortical licenses actor's face for AI-generated series "Inevitable"

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็นจุดเปลี่ยนในกฎหมายทรัพย์สินทางปัญญา — "สิทธิของบุคคล" (right of publicity) + "ลิขสิทธิ์ใน performance" + "data ที่ใช้ train" คือสาม layers ที่ต้องแยกออกจากกันในสัญญา; ตอนนี้ยังไม่มี template มาตรฐาน และ SAG-AFTRA ของสหรัฐฯ ก็ยังรบกับ studios อยู่ ไทยยังไม่มี framework เลย — ใช้สอนนักกฎหมายเรื่อง tech contract drafting ได้ดี
**ผู้เชี่ยวชาญด้าน AI:** microdrama vertical video + face licensing = ตลาดทดสอบที่ชัดสำหรับ identity-preserving video generation (Sora-style แต่ถูก consent-gate) ปริมาณคอนเทนต์ + จำนวนตัวละครต่อซีรีส์ของ microdrama ต้องการ model ที่ render consistent identity ข้ามหลายร้อย shot โดยไม่ drift — ยังเป็นปัญหาเปิดในวันนี้
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณเขียน pipeline สำหรับ video generation ทีมที่ใช้ face licensing ให้พิจารณา: (1) watermark + C2PA signature ทุก asset ที่ output, (2) revocation protocol ถ้า talent withdraw consent (ต้อง takedown ได้เร็วกว่า distribution), (3) audit log ของ prompt + checkpoint ที่ใช้ — มี 3 อย่างนี้ก็ลด liability surface ได้มาก
