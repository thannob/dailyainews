# Perspectives — 2026-05-10

## 1. Nvidia has already committed $40B to equity AI deals this year — TechCrunch

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข $40B ใน ~4 เดือนเป็นเคสคลาสสิกของ "vertical integration via equity" — ใช้สอน corporate finance และ industrial organization ได้ดี เพราะ Nvidia ไม่ได้แค่ขายชิป แต่ลงทุนใน customer ของตัวเองเพื่อให้แน่ใจว่ามี demand ฝั่งปลายทาง นักศึกษาควรเทียบกับเคส Intel-McAfee ทศวรรษก่อนเพื่อดูว่า strategy นี้สำเร็จหรือล้มในระยะยาว
**ผู้เชี่ยวชาญด้าน AI:** จุดที่น่ากลัวคือ "circular financing" risk — Nvidia ลงทุนใน OpenAI, IREN, Lumentum แล้ว revenue ที่บริษัทเหล่านี้สร้างกลับมาวนซื้อชิป Nvidia อีกที; ถ้า frontier AI demand ชะลอ valuation ของพอร์ตจะร่วงพร้อมกับยอดขายชิป — ความเสี่ยงไม่ใช่ uncorrelated เลย
**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบทางตรงคือ optionality ของ compute supplier กำลังหดตัว — Nvidia ถือ equity ใน OpenAI, IREN, Coherent, Lumentum หมายความว่าทุก hyperscaler / inference provider จะถูกดันให้ใช้ stack ของ Nvidia เป็น default มากขึ้น; ทีมที่อยากหลบ vendor lock-in ต้องเริ่มทดลอง alternative (TPU, AMD MI400, Cerebras) จริงจังตั้งแต่วันนี้

## 2. บลูมเบิร์กเผย สหรัฐฯ สงสัยไทยเป็นทางผ่านลักลอบส่งชิป Nvidia ให้ Alibaba ในจีน — Thairath

**อาจารย์ (มหาวิทยาลัย):** เคสนี้คือ "policy collision" ระหว่างนโยบาย AI sovereignty ของไทย (ผ่าน Siam AI / NCP) กับ export control ของสหรัฐฯ — ใช้สอน geoeconomics ได้ในชั้น undergrad รัฐศาสตร์/เศรษฐศาสตร์; ประเด็นชั้นลึกคือบริษัทตัวกลางที่อยู่ใน supply chain ของ "national champion" สามารถเป็น single point of failure ของยุทธศาสตร์ระดับชาติได้เพียงข้อกล่าวหาเดียว
**ผู้เชี่ยวชาญด้าน AI:** ผลทางเทคนิคที่ต้องจับตาคือ chip availability ของ data center ในไทย — ถ้าสหรัฐฯ ตอบโต้ด้วย entity-level export ban (เคยมีข่าวร่างกฎหมายจำกัดส่งออกชิป AI ไปไทย/มาเลเซีย) จะกระทบ training capacity ของทีม AI ในประเทศโดยตรง; ทีมที่วางแผนใช้ NCP ของไทยควร ressurvey แผนสำรอง compute ในสิงคโปร์/ญี่ปุ่นทันที
**โปรแกรมเมอร์มืออาชีพ:** ระยะสั้น ราคา GPU instance ในไทยอาจไม่ได้ถูกขึ้นทันที แต่ availability ของรุ่นแรง (H100/H200/B200) ใน Siam AI Cloud จะหายากขึ้นเรื่อยๆ; ทีมที่รัน fine-tune หรือ RAG indexing ขนาดใหญ่ในไทยควรล็อก capacity quarter หน้าไว้ก่อน และเริ่มทำ benchmark ข้าม region เพื่อเทียบ price/perf ก่อนตัดสินใจ migration
