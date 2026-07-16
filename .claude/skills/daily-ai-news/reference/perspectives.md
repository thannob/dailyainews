# Perspectives — 2026-07-16

## 1. Thinking Machines เปิดตัว Inkling (MoE 975B open-weight)

**อาจารย์ (มหาวิทยาลัย):** สอนคลาส LLM architecture ครั้งต่อไปให้ใช้คู่ตัวเลข "975B params vs. 41B active" นี้เป็นตัวอย่างเปิด — อธิบายว่าทำไม MoE เปลี่ยนวิธีอ่านตัวเลข "ขนาดโมเดล" ที่นักข่าวชอบพาดหัว และเปิดคำถามให้นักเรียนเทียบกับ dense model รุ่นเดียวกัน.
**ผู้เชี่ยวชาญด้าน AI:** จุดน่าสนใจของ Inkling ไม่ใช่ SOTA (Thinking Machines ประกาศเองว่าไม่ใช่) แต่คือ open-weight + multimodal 4-modal native ที่ยัง customizable ระดับนี้ — ถ้า routing/serving stack ทำได้จริง เป็นแนวรบใหม่กับ Qwen/DeepSeek ทันที.
**โปรแกรมเมอร์มืออาชีพ:** ก่อนตัดสินใจ swap production workload ให้ benchmark cost-per-1M tokens เทียบ Claude/GPT ที่ใช้อยู่ — MoE ประหยัดในทฤษฎี แต่ latency variance + memory footprint มักทำ TCO จริงไม่เป็นดังคาด.

## 2. Anthropic + Blackstone Ode ($1.5B enterprise implementation)

**อาจารย์ (มหาวิทยาลัย):** เอาไปสอน business strategy — บริษัทเทคที่เชื่อ "product-led growth" หันมาเล่น services-heavy ครั้งใหญ่; นี่คือ moment ที่ AI-as-service model ถูกยอมรับอย่างเป็นทางการโดย frontier lab.
**ผู้เชี่ยวชาญด้าน AI:** trillion-dollar target ของ Chris Taylor ไม่ใช่ hype เดี่ยว — Fortune 500 CFO กำลังต่อรอง discount API ก็จริง แต่ต้องจ่าย $300–500/ชม. ให้ engineer มา spec workload; Ode คือ arbitrage ระหว่างสองราคานี้.
**โปรแกรมเมอร์มืออาชีพ:** ทักษะที่ตลาด AI-implementation ต้องการเร็ว ๆ นี้ = การเขียน eval harness + observability + prompt-migration script — ไม่ใช่ prompt-engineering โชว์เดี่ยว; ถ้าคุณ ship stuff แบบนี้ให้ enterprise ได้ resume จะ liquid.

## 3. Apple Intelligence จีนไฟเขียว (Qwen หลัก, Baidu เสริม)

**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษา sovereign AI stack — สอนตอนพูดเรื่อง trade policy + technology localization; ค่า "one model for the whole world" ที่เคยเป็น default assumption ของนักเรียน 2 ปีก่อน กำลังจบลงเงียบ ๆ.
**ผู้เชี่ยวชาญด้าน AI:** interesting engineering — Apple ต้อง route foundation model calls ไปให้ Qwen ในภูมิภาคจีน แต่ยังคง on-device model เดิม; UX consistency ระหว่าง 2 backend เป็นโจทย์ที่ยากกว่า launch ปกติ.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ product ที่ต้อง ship CN/UAE/RU: อย่า hard-code single AI backend — ออกแบบ interface layer + prompt-portability tests ตั้งแต่ sprint แรก แม้ตอนนี้ยังไม่ต้อง.

## 4. Microsoft Patch Tuesday 570 flaws (MDASH AI-assisted)

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข "570 vs 137 ปีก่อน" คือ empirical evidence ที่จับต้องได้ที่สุดในปีนี้ว่า AI เปลี่ยน software security economy จริง — เอามาสอน SecOps + software engineering ethics คู่กัน.
**ผู้เชี่ยวชาญด้าน AI:** MDASH ที่ Microsoft ปล่อยชื่อออกมาเป็น bet เชิง defender scaling — แต่ attacker ก็ใช้ AI patch-diff เพื่อ reverse-engineer 1-day exploit ได้เร็วเท่ากัน; net effect ต่อ risk window ยังไม่ชัดว่าดีขึ้นสำหรับ end-user หรือไม่.
**โปรแกรมเมอร์มืออาชีพ:** เร่ง patch cycle ทันที — โดยเฉพาะ AD FS (CVE-2026-56155) และ SharePoint (CVE-2026-56164) ที่ zero-day ถูก exploit จริง; อย่ารอ monthly maintenance window ปกติ.

## 5. Suno hack เปิดโปง training data ที่ scrape จาก YouTube/Deezer/Genius

**อาจารย์ (มหาวิทยาลัย):** perfect case study สำหรับ data-ethics คลาส — training corpus 113,879 ชม. YouTube Music ที่ระบุใน source code แสดงให้เห็นว่า "โมเดลที่มี clean provenance" คือ minority ในตลาดจริง.
**ผู้เชี่ยวชาญด้าน AI:** DMCA circumvention เป็นข้อกล่าวหาที่หนักกว่า copyright infringement เดี่ยว ๆ — คดี Suno ครั้งนี้เป็น test case ว่าค่ายเพลงจะได้ injunction ระงับใช้โมเดลได้ทันหรือไม่.
**โปรแกรมเมอร์มืออาชีพ:** enforce data lineage tracking บน training pipeline (source URL, license, consent status) เดี๋ยวนี้ — enterprise CFO/legal จะถาม audit ภายในปีนี้ และไม่มีคำตอบ = ปิดดีลไม่ได้.
