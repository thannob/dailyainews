# Perspectives — 2026-11-21

## 1. ทรัมป์ขู่เก็บภาษีบริษัทสหรัฐฯ ที่สร้างศูนย์ข้อมูล AI ในต่างประเทศ

**อาจารย์ (มหาวิทยาลัย):** เหมาะเป็นเคสในชั้นเรียน IR / นโยบายสาธารณะ เรื่อง "techno-nationalism" — ให้นักเรียนเปรียบเทียบกับ chip export control ปี 2022 และถามว่ามาตรการภาษีศูนย์ข้อมูลครั้งนี้ตั้งอยู่บนฐานอำนาจกฎหมายฉบับใด (IEEPA, Section 232, กฎหมายใหม่) และ enforcement จะทำได้จริงหรือไม่ในยุคที่ hyperscaler กระจาย capacity ข้ามภูมิภาค
**ผู้เชี่ยวชาญด้าน AI:** ถ้า compute ต้อง onshore ทั้งหมด latency และต้นทุนพลังงานจะพุ่งขึ้น — ประเด็นเปิดคือมาตรการจะครอบคลุมเฉพาะ training หรือรวม inference ด้วย ผลกระทบต่อ edge inference ที่ serve user EU/APAC จะต่างกันสุดขั้ว ขึ้นกับคำจำกัดความนี้
**โปรแกรมเมอร์มืออาชีพ:** ตรวจสัญญา cloud ปัจจุบันเรื่อง force majeure และ data residency clause ทันที วาง dual-vendor plan สำหรับ workload sensitive ด้านเวลา และเตรียม failover ไปยัง provider ที่ไม่ใช่สหรัฐฯ ถ้า user base อยู่นอกสหรัฐฯ

## 2. Anthropic หุ้นร่วง 8.5%, Nasdaq เข้า correction

**อาจารย์ (มหาวิทยาลัย):** กรณีคลาสสิก post-IPO mean reversion (+17% วันแรก → -8.5% วันถัดไป) ใช้สอน behavioral finance ได้ทันที — ให้นักเรียนคำนวณ loss ของ buy-at-pop investor และเปรียบเทียบกับ Facebook, Rivian, Snowflake post-IPO
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณที่น่ากังวลกว่าหุ้น Anthropic คือ Nasdaq เข้า correction + ชิปร่วง >13% ถ้า hyperscaler capex ชะลอตัว (free cash flow Amazon/Alphabet ติดลบติดต่อกัน) การเทรน frontier model รุ่นถัดไปอาจ delay 6–12 เดือน
**โปรแกรมเมอร์มืออาชีพ:** Anthropic หลัง IPO + หุ้นร่วงจะต้องโชว์ margin ให้ WS — pricing tier อาจขยับในสัปดาห์หน้า เตรียม abstraction layer สลับ provider (OpenAI, Google, open weights) ให้พร้อม ถ้ายังไม่ได้ทำก็ไม่ใช่ premature optimization แล้ว — เป็น insurance

## 3. AI + Claude อ้างพิสูจน์สมมติฐานรีมันน์ด้วย Lean

**อาจารย์ (มหาวิทยาลัย):** โอกาสดีสอนเรื่อง formal verification ให้ปริญญาตรี — เปรียบเทียบกับ Fermat's Last Theorem ปี 1993 (ใช้เวลา peer review หลายเดือน) กับกรณีนี้ที่ Lean file ตรวจได้อัตโนมัติ เน้นว่า "โพสต์ Lean file" ≠ "proof ได้รับการยอมรับ"
**ผู้เชี่ยวชาญด้าน AI:** ไม่ใช่ "Claude พิสูจน์เอง" แต่คือ human-in-the-loop workflow — ต้องรู้สัดส่วน scaffolding ของมนุษย์ vs. machine ประเด็นสำคัญคือ generalize ไป GRH ได้จริงหรือเป็น corollary ที่คนรู้อยู่แล้ว ต้องรอ community mathematicians review Lean file (อาจใช้สัปดาห์ถึงเดือน)
**โปรแกรมเมอร์มืออาชีพ:** pattern "LLM proposes, compiler disposes" เริ่มใช้ได้ระดับ bounded task — น่าสนใจสำหรับทีมที่สร้าง critical software (crypto library, verification kernel) economics ยังเป็นคำถาม: Claude Opus หลายวันต่อหนึ่ง proof อาจแพงกว่า dedicated AlphaProof instance

## 4. OpenAI เตือนพนักงานเรื่อง honey-trap espionage

**อาจารย์ (มหาวิทยาลัย):** เคสคลาสสิกสำหรับ security studies — เปรียบเทียบ Robert Hanssen, Aldrich Ames กับยุค AI frontier labs ให้นักเรียนออกแบบ counterintelligence program สำหรับบริษัท 2,500 คน (training cadence, access tier, travel/device policy)
**ผู้เชี่ยวชาญด้าน AI:** attack asymmetry หนักขึ้นเพราะ attacker ใช้ AI สร้าง fake profile และ voice call เร็วกว่า defender ตรวจของปลอม การเตือนพนักงานเป็น social engineering defense ขั้นต่ำ แต่ไม่พอ — model weights ต้องการ technical control ชั้น compute cluster (hardware-backed access, audit log, offline air-gap)
**โปรแกรมเมอร์มืออาชีพ:** แม้ทีมเล็กก็โดนเป้า ถ้ามี API key หรือ fine-tune pipeline — บังคับ phishing-resistant 2FA (Yubikey/passkey), ห้าม commit secret ลง repo, offboarding checklist เพิกถอน access ภายใน 1 ชั่วโมง, ขยาย security awareness ไปครอบคลุม social engineering นอก email

## 5. หลัง Jensen Huang ออกจาก Nvidia — คำถามสไตล์การบริหาร

**อาจารย์ (มหาวิทยาลัย):** กรณี founder-CEO exit ระดับ market cap หลายล้านล้านเทียบได้กับ Steve Jobs (Apple 1985), Travis Kalanick (Uber), Jack Dorsey (Twitter) ใช้สอน leadership transition / organizational culture
**ผู้เชี่ยวชาญด้าน AI:** Nvidia คือ stack ทั้งหมด — CUDA + cuDNN + TensorRT + NeMo + NIM + ความสัมพันธ์ส่วนตัวกับ hyperscaler ผูกกับ Huang มายาวนาน timing เปลี่ยน CEO ตรงกับ AMD MI350 + Google TPU v7 ที่ไล่ตาม — ถ้า execution ตก Nvidia เสี่ยงเสีย narrative leadership
**โปรแกรมเมอร์มืออาชีพ:** CUDA roadmap ไม่หยุดในระยะสั้น แต่ควรเริ่ม evaluate backend alternative (ROCm, PyTorch XLA, MLX) สำหรับ workload ที่ portable ได้ ใน 18 เดือนข้างหน้าถ้า developer relations ของ Nvidia แผ่วลง ecosystem alternative อาจได้ที่ยืนขึ้น
