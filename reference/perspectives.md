# Perspectives — 2026-09-26

## 1. Astra and Opus just passed Turing's other test — Enigma cracked

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ต้องยกให้เป็นตัวอย่างในคาบ AI + history — Turing เคยแตก Enigma ด้วยเครื่องกลไก, วันนี้ LLM แตก Enigma ที่เหลืออีก 2 ข้อความในเวลาไม่กี่วัน ประเด็นสอนคือ AI เร่ง *research throughput* ได้ (ค้น archive, จำลอง machine, ทดสอบสมมติฐาน) แต่ยังต้องมีมนุษย์ตั้งโจทย์และ verify ผล
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่น่าสนใจไม่ใช่ "AI แตก crypto ได้แล้ว" — Enigma ไม่ใช่ modern crypto — แต่เป็น demonstration ว่า agentic search-and-simulate loop ทำงานได้จริงในโดเมนที่มี ground truth ให้ตรวจ (Willis ใช้ known officer signature เป็น key oracle) และ workflow นี้ scale ไปได้กับ scientific literature-heavy problems อื่น ๆ
**โปรแกรมเมอร์มืออาชีพ:** วิธีที่ Leffen ใช้ — prompt โมเดลให้ search archive → build simulator → recover plaintext — คือ blueprint สำหรับ agent tool-use pipeline ที่คนทำ product ควรลอกไปใช้ทันที; key takeaway คือให้ agent มี code-execution + archive-search + verify-against-ground-truth ครบ 3 ตัว ถ้าขาดตัวใดตัวหนึ่ง output จะดีแค่ที่มันดูจริง แต่ไม่จำเป็นต้อง *เป็น* จริง

## 2. Nscale secures $3.36B pre-IPO convertible

**อาจารย์ (มหาวิทยาลัย):** ตัวเลขนี้ควรใช้สอนใน finance/econ ควบ AI — $3.36B convertible note **ก่อน** IPO เป็น signal ว่า public market ยังไม่พร้อมจะดูดหุ้น neocloud ที่ค่าใช้จ่ายด้าน infrastructure สูงมากในราคาเดียวกับ big tech ให้ห้องเรียนวิเคราะห์ risk profile ของธุรกิจที่มี capex สูงและ margin บาง
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นสำคัญคือ Nvidia ลงเงินอีก $1B — เท่ากับ Nvidia กำลัง back-stop demand ให้ compute buyer ของตัวเอง (customer financing) การพึ่งพา financial engineering แบบนี้ทำให้ AI compute supply chain ทั้ง stack เชื่อมกันแน่นขึ้นและ concentration risk สูงขึ้น
**โปรแกรมเมอร์มืออาชีพ:** ในทางปฏิบัติ ถ้าโปรเจกต์คุณคิดจะเช่า H100/B200 cluster ยาว ๆ ให้ contract ที่ Nscale/CoreWeave-class neocloud มี clause ป้องกัน bankruptcy/asset-sale (SLA carve-out, escrow of data) เพราะ IPO cycle + convertible funding cycle ของ neocloud เต็มไปด้วย tail-risk ที่ยังไม่เคยผ่านการทดสอบใน downturn

## 3. Crusoe abandons $1.25B Boom turbine plan

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เปิดบทเรียนเรื่อง energy strategy สำหรับ AI infrastructure — ทำไม 42-MW natural gas turbines ที่เคยเป็นตัวเลือกอันดับหนึ่งของ AI data center กลับกลายเป็น "not primary" ในเวลาไม่ถึงปี ให้อภิปรายเรื่อง capital lock-in vs option value และ energy transition
**ผู้เชี่ยวชาญด้าน AI:** สาระหลักคือ AI data center strategy กำลังเปลี่ยนจาก "commit gigawatt-scale power ล่วงหน้าหลายปี" ไป "modular + multi-source (wind/solar/battery/grid) + short lead time" การตัดสินใจแบบนี้ของ Crusoe แสดงว่า workload assumption กำลัง shift — training run ขนาดใหญ่ที่ต้อง 24/7 baseload อาจไม่ใช่ shape เดียวของ demand อีกต่อไป inference workload มี variability สูงกว่าและเข้ากับ renewable + battery ได้ดีกว่า
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณ deploy AI workload บน multi-region cloud อยู่ ให้เริ่ม instrument **energy source per region** ใน telemetry เพราะภายใน 12-24 เดือน SLA/pricing ของ cloud AI compute จะเริ่มแยกตาม primary power mix ของ region ทีมที่ optimize สำหรับ region ที่มี renewable + battery จะได้ราคาถูกกว่า และในบางเวลาของวัน quota compute อาจต่างกัน

## 4. Google DeepMind talent exodus fuels startup boom

**อาจารย์ (มหาวิทยาลัย):** เคสตัวอย่าง organizational dynamics ในยุค AI — เมื่อ power center ย้ายจาก London ไป California นักวิจัยรุ่นเก๋าเลือกออกไปสร้าง startup แทนที่จะ relocate ใช้อธิบายเรื่อง talent geography, principal-agent problem ใน corporate R&D, และ opportunity cost ของ "big lab" กับ "small lab" ในช่วงเวลาที่ VC ยินดีจ่ายเงินระดับหลายสิบล้านให้ทีม 3-5 คน
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่เด่นกว่าตัวเลขคือ *direction* — Metis Reasoning ตั้งใจไปทาง non-LLM reasoning + self-training system นี่คือ signal ว่านักวิจัย tier-1 หลายคนเชื่อว่า LLM scaling อย่างเดียวไม่พาไป AGI ต้องมี architectural bet ใหม่ ผู้ที่ตาม frontier ควรจับตา paper ที่ทีมเหล่านี้ปล่อยในอีก 6-12 เดือน
**โปรแกรมเมอร์มืออาชีพ:** ในระยะสั้นสิ่งที่กระทบทีม engineer คือ *tool volatility* — เมื่อ ex-DeepMind ตั้ง startup ใหม่ 5-10 เจ้าในปีเดียว จะมี framework/inference-runtime/reasoning-API ใหม่ออกมาถล่มตลาด อย่ารีบ lock-in กับ vendor ใหม่จน API ยังไม่มี v1.0 stable; ถ้าจำเป็นให้ทดสอบผ่าน adapter layer เท่านั้น

## 5. Microsoft ทิ้งแบรนด์ Copilot+ PC จาก Surface 2026

**อาจารย์ (มหาวิทยาลัย):** เคสตัวอย่าง product marketing ที่น่าสอน — สเปคเดิม (NPU, on-device AI) แต่ทิ้งชื่อแบรนด์ เพราะแบรนด์กลายเป็น *liability* จาก launch ปี 2024 ที่มี Recall controversy + performance ที่ไม่ตรงคำโฆษณา สอนเรื่องความสำคัญของ brand equity vs technical capability
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นสำคัญคือ Microsoft ไม่ได้เลิก AI PC — แค่เลิกใช้ชื่อ "Copilot+" นั่นคือยอมรับว่า **positioning ผิด**: ผู้บริโภคจำ Copilot+ กับ Recall / on-device search ที่ยัง underdeliver ถ้าตลาด edge-AI ยังโตต่อ Microsoft ต้องหา category name ใหม่ที่ไม่ผูกกับ scandal ครั้งก่อน
**โปรแกรมเมอร์มืออาชีพ:** สำหรับนักพัฒนาที่ทำแอปพึ่งพา NPU บน Windows — code path ยังทำงานเหมือนเดิม (API surface, driver stack ไม่เปลี่ยน) แต่ marketing collateral ต้องปรับ; อย่าอ้างอิงตราสินค้า "Copilot+ PC" ใน onboarding flow ของแอปคุณอีก ให้อ้างอิงเป็น "AI-accelerated Windows PC with NPU" แทนเพื่อรอดูว่า Microsoft ตั้งชื่อใหม่ว่าอะไร
