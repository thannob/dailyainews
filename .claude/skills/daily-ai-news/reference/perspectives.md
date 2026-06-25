# Perspectives — 2026-06-25

## 1. OpenAI unveils first custom chip "Jalapeño" built with Broadcom for LLM inference

**อาจารย์ (มหาวิทยาลัย):** เคสนี้สอนเรื่อง vertical integration — ผู้ผลิตซอฟต์แวร์ทำชิปเอง คล้ายที่ Apple ออก M1 — แต่สิ่งที่น่าสอนคือ "ใช้โมเดลของตัวเองช่วยออกแบบชิป" ปิดวงจร AI-designs-AI-hardware ที่ตำราเรียนจะเริ่มต้องเขียนใหม่
**ผู้เชี่ยวชาญด้าน AI:** เก้าเดือนจาก design ถึง tape-out ผิดปกติเร็วมากสำหรับ ASIC ระดับนี้ — ของจริงคือ inference cost ต่อ token ที่ OpenAI คุมได้เอง ไม่ใช่แค่ NVIDIA margin ที่หายไป ถ้า Jalapeño ส่งของได้ปลายปีจริง pricing ของ ChatGPT/API จะกดลงได้อีกครั้ง
**โปรแกรมเมอร์มืออาชีพ:** ฝั่ง backend ที่ใช้ OpenAI API เริ่มวางแผนได้ว่าตั้งแต่ Q1 2027 token rate น่าจะถูกลงและ throughput สูงขึ้น แต่ระวัง vendor lock-in ที่จะลึกขึ้น — feature ใหม่ ๆ บางอย่างอาจ optimize เฉพาะ Jalapeño จน fallback ไป model อื่นได้ผลต่างกัน

## 2. Google poised to lose two more high-profile Gemini researchers — Jonas Adler and Alexander Pritzel — to Anthropic

**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษา "talent flight" คลาสสิก — ทำไม top researcher ยอมทิ้ง compensation ของ Big Tech ไป startup ใกล้ IPO เรื่อง pre-IPO equity vs cash compensation เป็นบทเรียน organizational economics ที่สอนได้ทันที
**ผู้เชี่ยวชาญด้าน AI:** Adler ดูแล AI coding ส่วน Pritzel อยู่ที่ training infra ของ Gemini — สองด้านที่ Anthropic ขาดแคลนน้อยที่สุดในเชิง headline แต่ขาดแคลนมากที่สุดในเชิง depth การได้คนระดับนี้พร้อมกันสองคน หมายความว่า Gemini 3/4 อาจช้าลงและ Claude Opus 4.9/5.0 อาจมาเร็วขึ้น
**โปรแกรมเมอร์มืออาชีพ:** หกวันก่อนหน้านี้ Jumper ออก Shazeer ออก ตอนนี้ Adler+Pritzel ออก — โมเมนตัมของ Google ในการรักษาคนพังเป็นรูปแบบ ถ้าทีมพึ่ง Gemini เป็น primary model อยู่ ต้องเริ่มตั้งคำถามว่ารุ่นถัดไปจะมาทันคู่แข่งหรือไม่ และเตรียม fallback ที่ทดสอบจริงไว้ในมือ

## 3. Anthropic accuses Alibaba of "illicitly" accessing Claude via 25,000 fraudulent accounts in distillation campaign

**อาจารย์ (มหาวิทยาลัย):** เคสนี้คือตำราเรียน "trade secret meets ML" — distillation attack คือการสกัด capability จาก model เก่งไปสอน model เล็ก คำถามทางจริยธรรมและกฎหมายคือ output ที่ลูกค้าจ่ายเงินซื้อ ผู้ขายห้ามนำไป retrain ของตัวเองได้ไหม กฎหมายลิขสิทธิ์ปัจจุบันยังตอบไม่ชัด
**ผู้เชี่ยวชาญด้าน AI:** 28.8 ล้าน exchange จาก 25,000 บัญชีในช่วง 6 สัปดาห์ — เลขนี้บอกว่า fraud-detection layer ของ Anthropic ตอบสนองช้ากว่าที่ควร ในเชิงเทคนิค การตรวจ distillation pattern แบบ real-time ต้องใช้ behavioral signature ของ traffic ไม่ใช่แค่ rate limit ต่อ account — เหตุนี้ Anthropic ถึงพึ่ง remediation ทางการเมือง (จดหมายถึง Senate) แทนการตรวจจับเอง
**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบเชิงปฏิบัติ — ToS ของ vendor frontier-model จะเข้มขึ้นทันที ทีมที่ใช้ Claude output ใน synthetic data pipeline สำหรับ fine-tune model ของตัวเอง ต้องอ่าน ToS ฉบับล่าสุดให้ละเอียด และเก็บ audit log ของการใช้งาน ก่อนที่ Anthropic จะ flag account โดย proactive

## 4. Engineering jobs proved the most resilient role across Tech Majors — 55% of 2025 new hires

**อาจารย์ (มหาวิทยาลัย):** ข้อมูลนี้ขัดกับ narrative กระแสหลัก — สอนนักศึกษาให้แยก hype จาก data ได้จริงคือทักษะอันดับหนึ่งของยุคนี้ ใช้กราฟ 2019 vs 2025 ของ SignalFire เปิดคาบเรียนพรุ่งนี้
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลขนี้ไม่ได้แปลว่า AI ไม่กิน engineer แต่หมายความว่าตำแหน่งที่ AI ทำแทนได้ — ตำแหน่ง junior/repetitive — ถูก absorb เข้าไปในตำแหน่ง engineer ที่ใช้ AI ทำงานต่อ องค์ประกอบของงานเปลี่ยน ปริมาณงานไม่ลด
**โปรแกรมเมอร์มืออาชีพ:** ข่าวดีคืออาชีพยังอยู่ ข่าวร้ายคือ leverage ต่อหัวเพิ่มขึ้นชัดเจน — ถ้าวันนี้ทีมยังเขียน boilerplate เองโดยไม่ใช้ AI tooling จริงจัง จะเสียเปรียบใน performance review รอบหน้า เร่งฝึก agentic workflow กับ Codex/Claude/Cursor ให้ default ของทีมเปลี่ยน

## 5. Micron stock at record high as memory-chip crunch turns into AI tailwind

**อาจารย์ (มหาวิทยาลัย):** เคสคลาสสิก "shortage of complement" — เมื่อสินค้า A (GPU) ต้องคู่กับสินค้า B (HBM/DRAM) supply ของ B กลายเป็น constraint ทันที สอน Porter's value chain ได้ตรง ๆ ราคา HBM ในปี 2026 น่าจะเป็นกรณีศึกษาเศรษฐศาสตร์อุตสาหกรรมของหลายปี
**ผู้เชี่ยวชาญด้าน AI:** HBM scarcity คือ "next GPU shortage" — บริษัทที่ training/inference scale ใหญ่จะแย่งกันล็อก supply ระยะยาว ดีลที่ Anthropic-Micron-Series H lock supply ไว้คือ template ใหม่ — vendor หน่วยความจำกลายเป็น strategic partner ไม่ใช่ commodity supplier
**โปรแกรมเมอร์มืออาชีพ:** ผลทางอ้อมต่องาน engineer — cloud GPU instance ที่ HBM แรงและพอ จะหา reservation ยากขึ้นเรื่อย ๆ โดยเฉพาะ A100/H100/H200 และ Blackwell ใหม่ ถ้าทีม training/fine-tune ของตัวเอง วางแผน capacity ล่วงหน้า 6-9 เดือนแทนรายเดือน ไม่งั้นจะติด queue
