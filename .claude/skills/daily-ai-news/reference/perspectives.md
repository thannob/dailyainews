# Perspectives — 2026-08-15

## 1. Uber & Pony.ai — 2,000 robotaxis สู่ยุโรป

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เป็นตัวอย่างชั้นเรียน platform economics + ยุทธศาสตร์ตลาดผสม: ผู้ผลิตเทคโนโลยี (Pony.ai จีน) + platform demand (Uber) + operator ท้องถิ่น (Verne โครเอเชีย) — สอนได้ว่าเหตุใด vertical integration ไม่ใช่คำตอบเดียว และการแบ่งหน้าที่ 3-ทางสามารถ scale ข้ามพรมแดนกฎหมายที่ซับซ้อนได้เร็วกว่า.
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณสำคัญคือจีน "export" autonomous-driving stack เข้าตลาดยุโรปได้แล้ว — ไม่ใช่แค่ HW แต่เป็น model + safety case + operational envelope; ยังไม่เผยเมืองและ timeline = แสดงว่า regulatory friction ยังใหญ่ (EU AI Act + local vehicle-type approval) และดีลนี้เป็น framework agreement มากกว่า deployment ที่พร้อมยิงจริง.
**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบระยะสั้นต่อทีม engineer แถบยุโรปคือ opportunity ในตลาด mobility-adjacent (fleet ops software, HD-map tooling, teleop console) จะเปิดใน 12-18 เดือน; ทีมที่ทำ ride-hailing integration หรือ trip-router ควรเริ่มดู Pony.ai API surface และ Uber developer platform ตั้งแต่ตอนนี้.

## 2. Google เปิดสวิตช์ปิด visible watermark บน AI generations

**อาจารย์ (มหาวิทยาลัย):** ประเด็นชั้นเรียน media literacy / trust: การมี invisible SynthID + C2PA เพียงพอไหมเมื่อผู้ใช้ทั่วไปมองไม่เห็น? เทียบกับ visible watermark ที่เป็น social signal โดยตรง — ผู้เรียนควรอภิปรายว่า trust surface กำลังย้ายจาก "หน้าตาไฟล์" ไปที่ "verification pipeline" ที่ต้องใช้ tool เฉพาะจึงจะอ่านได้.
**ผู้เชี่ยวชาญด้าน AI:** Google เดิมพันว่า SynthID (statistical watermark ในภาพ) + C2PA (cryptographic metadata) จะทำหน้าที่แทน — ทั้งสองเทคนิค survive re-encoding บางระดับได้ แต่ crop / heavy re-color / screenshot ยังทำลาย SynthID ได้; policy compromise ที่น่าสังเกตคือ EU ยังบังคับ visible watermark ต่อ = เห็น divergence ของ AI transparency regime ระหว่างภูมิภาคชัดขึ้น.
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้าง product ใช้ Gemini/Nano Banana/Omni/Lyria — ตอนนี้เนื้อหาที่ generate ออกมาจะไม่มี visible mark เป็น default (นอกจากลูกค้าอยู่ EU) = flow production พร้อมใช้ทันที; ทีม trust & safety / newsroom / stock-media ต้องรีบ integrate SynthID detector + C2PA reader ก่อนที่รูปไม่มี mark จะไหลเข้า pipeline; อย่าตัดสินจาก visible mark อย่างเดียวอีกต่อไป.

## 3. Z.ai ปล่อย GLM-5.3 — แข่ง coding + cybersecurity กับ Claude / GPT

**อาจารย์ (มหาวิทยาลัย):** เคสสอน scaling law ยุคใหม่ — Z.ai ใช้ base model ขนาดเดิม (~700B params) แต่ scale post-training อย่างเข้ม → ผลลัพธ์ดีขึ้น 50% ใน coding + แซง Anthropic/OpenAI ใน CyberGym; ห้องเรียน ML ควรอภิปรายว่าเหตุใด "post-training investment" (RLHF, RLVR, tool-use SFT) จึงกลายเป็น axis หลักของ competitive edge แทน "pretraining scale" ในปี 2026.
**ผู้เชี่ยวชาญด้าน AI:** ข้อระวัง 3 อย่าง: (1) benchmark เป็น company-reported ยังไม่ผ่าน independent eval — CyberGym 84.5% vs Mythos 5 83.8% เป็นระยะห่างที่อยู่ใน noise band ของ eval variance; (2) การ scale post-training บน base model เดิมมี ceiling — ครั้งหน้าคงต้อง pretrain รอบใหม่; (3) weights จะปล่อยใน 2 สัปดาห์ = community จะเช็คได้จริง, รอ eval จาก LMSys / MMLU-Pro / SWE-bench Verified ก่อนสรุป.
**โปรแกรมเมอร์มืออาชีพ:** ทีม security engineer + devsecops ที่รอ open-weight model สำหรับ vulnerability research ควร queue Z.ai GLM-5.3 ไว้ทดสอบตอน weights ปล่อย (~ปลาย ส.ค.); ทีม coding agent — อย่าเพิ่งสลับจาก Claude/GPT/Gemini เพราะยังไม่มี real-world SWE-bench score; ทีมที่ใช้ coding model ผ่าน API ควร monitor Z.ai API pricing เมื่อประกาศ — จีนมักตั้งราคาต่ำกว่า US frontier 3-5×.

## 4. Alibaba / Baidu / Kuaishou — แรงกดดัน AI cost ก่อนประกาศงบ

**อาจารย์ (มหาวิทยาลัย):** เคสสอน corporate finance + strategy: บริษัทจีนกลุ่มนี้ต้องอธิบายกับนักลงทุนพร้อมกันว่า (a) AI capex ยังต้อง scale ต่อ (b) revenue จาก AI ยัง narrow (c) การแข่งขันในประเทศบีบ margin — เหมือน "trilemma" ที่ Big Tech US เจอเมื่อ 12-18 เดือนก่อน; วิเคราะห์ได้ว่าใครจะเป็น "winner" ใน post-DeepSeek era.
**ผู้เชี่ยวชาญด้าน AI:** signal สำคัญคือ "death zone" — ผู้เล่นที่ไม่ frontier + ไม่ market-breaking pricing จะถูกบีบออก; Alibaba มี Qwen 3.8-Max เป็น frontier claim + Z.ai (Zhipu) กด pricing → Baidu Ernie + Kuaishou Kling ตกอยู่ในกลุ่มกลาง ๆ ที่เสี่ยงสุด; เฝ้าดู earnings call ว่า capex guidance จะขึ้นหรือลง (ถ้าลง = ยอมแพ้ frontier race, ถ้าขึ้น = double-down).
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ใช้ Chinese AI API ระวัง pricing volatility ใน 6 เดือนหน้า — ผู้เล่นบางรายอาจตัดฟีเจอร์หรือขึ้นราคาแทนที่จะแบก loss; ทีมที่ integrate Qwen / Ernie / Kling ควรมี fallback ไปโมเดล US หรือ open-weight (Llama / Muse Glimmer / GLM-5.3 หลัง release) เผื่อ vendor ปิด; อย่า lock-in single Chinese vendor ในตลาด global product เพราะ regulatory risk (US export control) ก็เพิ่มด้วย.

## 5. Kushner (Thrive) เตือน AI euphoria ใน VC letter ครั้งแรก

**อาจารย์ (มหาวิทยาลัย):** เคสสอน financial cycle + venture capital pedagogy — เมื่อ mainline growth investor (Thrive สนับสนุน OpenAI, Stripe, Instagram) ออก letter เตือนพวกเดียวกันเรื่อง euphoria = สัญญาณคลาสสิกของ late-cycle behavior (ตำราการเงินสมัย Charles Kindleberger); น่าใช้เป็น case study เทียบกับ Warren Buffett memo ปี 2000 หรือ Howard Marks memo หลายฉบับ.
**ผู้เชี่ยวชาญด้าน AI:** Kushner ไม่ใช่ AI skeptic — Thrive ลงทุน OpenAI หนัก; letter นี้เป็น "internal critique" ที่มีน้ำหนักเพราะ speaker มี skin in the game; ประเด็นที่ควรอ่านเต็มคือ (1) valuation กับ multiples ของ AI startup ตอนนี้เทียบกับ SaaS 2021, (2) แนวโน้ม "AI investment as story" vs "AI investment as unit economics", (3) implicit warning ต่อ LP ให้เตรียม J-curve ที่ยาวกว่าปกติ.
**โปรแกรมเมอร์มืออาชีพ:** วิศวกรที่พิจารณาย้ายไป AI startup — ให้ weight signal นี้เป็น 1 ในหลาย factor; ถ้า startup ไม่มี unit economics ชัด (paying customer ที่ retain > 12 เดือน) และพึ่ง narrative round เดียว = risk สูงเมื่อ market cool; วิศวกรที่ทำงาน enterprise AI ในบริษัทใหญ่ — ประโยชน์ระยะสั้นคือ pricing power ของ vendor ที่ overheated จะเริ่มลง, negotiation window เปิดในไตรมาสหน้า; ทีม infra ที่ยังไม่ commit annual GPU contract — ช้าลงหนึ่งไตรมาสน่าจะคุ้ม.
