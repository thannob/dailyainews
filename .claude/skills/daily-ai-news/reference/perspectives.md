# Perspectives — 2026-08-16

## 1. Alibaba AI Models Hit 3B Downloads, Passing Meta, Google

**อาจารย์ (มหาวิทยาลัย):** เคสสอน "distribution beats performance" — Alibaba ไม่ได้แซง frontier benchmark แต่แซง download count เพราะกลยุทธ์ open-weight + ราคาถูก + license เอื้อ; ห้องเรียน strategy น่าให้เทียบกับ Android vs iOS ปี 2011.
**ผู้เชี่ยวชาญด้าน AI:** 3B downloads เป็น cumulative จาก Hugging Face — สะท้อน adoption ในระดับ developer/researcher มากกว่า production revenue; ยังต้องแยก download กับ inference volume ที่ Meta ยัง lead ใน production เพราะ Llama ฝังใน AWS Bedrock/Azure; แต่ก็ปฏิเสธไม่ได้ว่า "China open weight" กำลังกิน mindshare ทั้ง academic + startup ecosystem.
**โปรแกรมเมอร์มืออาชีพ:** ถ้ายังไม่เคยลอง Qwen — ควรลองเป็น fallback สำหรับ Llama; license Qwen อนุญาต commercial use กว้าง, มี 460 model variants ให้เลือก (จาก edge 0.5B ไปยัง MoE 500B+), coding + Thai/CJK เก่งกว่า Llama บาง benchmark; แต่ระวัง US export/geopolitical risk ถ้าลูกค้าเป็นภาครัฐ US/EU.

## 2. Bond Traders Agonize Over AI Companies' $70B Shadow Credit Backstops

**อาจารย์ (มหาวิทยาลัย):** เคสสอน off-balance-sheet obligation + circular financing — คล้าย SIV/CDO ก่อน 2008 แต่ underlying คือ GPU + data-center capacity ไม่ใช่ mortgage; ห้องเรียน corporate finance ควรอ่านคู่กับกรณี Enron special-purpose entities.
**ผู้เชี่ยวชาญด้าน AI:** $70B phantom liability เกิดจาก **residual value guarantee** ที่ Nvidia + peers เขียนให้ AI cloud + neocloud (CoreWeave, Nebius, Crusoe) เพื่อให้ debt raise ได้ต้นทุนต่ำ — ถ้า GPU utilization drop หรือ next-gen chip ทำให้ H100/B200 obsolete เร็วกว่าคาด residual value จะ crystallize เป็น real liability; Nvidia $500B consortium (BlackRock/Goldman) เป็นการ "share the risk" แต่ก็ concentrate risk ใน 6-7 financial institutions.
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่พึ่ง neocloud (CoreWeave/Lambda/Nebius) สำหรับ GPU rental — ควรเช็ค credit rating + contract stability ของ vendor; ถ้า vendor default = service interruption; ทีมที่ commit long-term GPU reservation ควร diversify ไปยัง hyperscaler (AWS/GCP/Azure) อย่างน้อย 30% ของ workload; อย่า lock-in long-term contract > 12 เดือน ตอนนี้ (pricing มีโอกาสลง 20-30% ถ้า market cool).

## 3. Chaiyachonok / TH-AI Passport ซักฟอก

**อาจารย์ (มหาวิทยาลัย):** เคสสอน public procurement + AI governance ในบริบทไทย — 1,621 ล้านบาทเพื่อ Generative AI ฟรี 1 ปีให้ 5 ล้านคน = ต้นทุนเฉลี่ย ~324 บาท/คน/ปี (ราคาถูกจริง แต่ opportunity cost คืออะไร?); ห้องเรียน public policy น่าเทียบกับโครงการ Chip Wallet สิงคโปร์หรือ Digital Skills Fund UK.
**ผู้เชี่ยวชาญด้าน AI:** ความเสี่ยงจริงที่ต้องจับตา: (1) vendor lock-in — โครงการเลือก "top-tier Generative AI" ยี่ห้อไหน? ถ้า GPT/Claude/Gemini แสดงว่า data flow ออก TH; (2) data sovereignty — prompt ของ 5M คน ไปที่ไหน, ใช้ retrain ไหม; (3) sustainability — ปี 1 ฟรี ปี 2 ใครจ่าย, ถ้ารัฐไม่จ่ายต่อ = citizens ที่ผูกงานกับ AI แล้วจะถูก throttle; (4) ทำไมไม่ใช้ open-weight (Qwen/Llama/Gemma) ที่ deploy on-shore ได้; (5) transparency ของ RFP + winner ยังไม่เปิดครบ.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณเป็นทีม developer ไทยและอยากให้ทีม/นักเรียนของคุณได้ใช้ frontier AI — รอลงทะเบียน TH-AI Passport เมื่อเปิด (ปลาย ก.ค.-ต้น ส.ค. ตามที่ปลัดดีอีระบุก่อนหน้า); แต่ควรมี exit plan — export prompt history, ใช้ทักษะที่ transferable, อย่าสร้าง product/business ที่พึ่งเฉพาะ TH-AI Passport tier เพราะ program อาจ discontinue หลังปี 1; ผู้ประกอบการ startup — โครงการนี้เป็นโอกาส demand-side subsidy สำหรับ AI-native product ในไทย ปีนี้ user acquisition cost ต่ำลงชั่วคราว.

## 4. NST Fair 2569 (มหกรรมวิทย์ฯ) เปิด — ชู AI-นวัตกรรม

**อาจารย์ (มหาวิทยาลัย):** โอกาสพานักเรียน/นิสิตไปเห็น AI แบบ hands-on 15-23 ส.ค. ที่ IMPACT — จุดที่น่าใช้เป็น field trip: "AI Revolution: The New Human Edge" + Coding & AI workshops; ควรออกแบบ pre/post visit assignment ให้ผู้เรียนไม่ใช่แค่ "ดู" แต่ต้อง critique การนำเสนอ AI (hype vs substance).
**ผู้เชี่ยวชาญด้าน AI:** งานลักษณะนี้มักเน้น demonstration มากกว่า capability boundary — ตัวชี้วัดที่น่าจับตาคือมีวิจัยไทย (Vistec, จุฬาฯ, สจล., NECTEC) ที่โชว์ result ระดับ international ไหม, หรือแค่ demo consumer LLM ต่างชาติ; นักวิจัย + policy maker ควรถือโอกาสนี้ scope ว่าไทย invest ตรงจุดหรือไม่ในระยะ 3-5 ปี.
**โปรแกรมเมอร์มืออาชีพ:** ถ้ามีเวลา 1 วันที่กรุงเทพ ระหว่าง 15-23 ส.ค. ควรไปดูงาน — networking กับ startup + academic ไทยที่โฟกัส AI/robotics ในบริบท SEA ทำ business dev cheap มาก (ค่าเข้าฟรี); โฟกัสที่ startup pavilion + academic booth ที่โชว์ working prototype (ไม่ใช่ slide); เก็บ contact สำหรับ hiring pipeline ถ้าทีมคุณกำลังหา ML engineer / robotics engineer ในไทย.
