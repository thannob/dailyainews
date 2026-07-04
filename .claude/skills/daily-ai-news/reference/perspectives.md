# Perspectives — 2026-07-04

## 1. Microsoft × Nine Entertainment — first Copilot journalism licensing deal in Asia-Pacific

**อาจารย์ (มหาวิทยาลัย):** ให้อ่านคู่กับดีล Microsoft × Nine ปี 2024 (Copilot จ่ายผู้พิมพ์) และ Cloudflare "AI-must-pay" policy จาก 1 ก.ค. — นี่คือช่วงที่ **economic layer** ของอินเทอร์เน็ตกำลังจัดโครงสร้างใหม่รอบ retrieval-augmented generation. คำถามใน class: ถ้า attribution + traffic กลับไปที่ต้นทางเป็น payment ในตัวเอง อุตสาหกรรมข่าวเปลี่ยน model จาก ad → licensing แล้วอะไรจะเปลี่ยนตาม (คุณภาพข่าว, brand power ของ masthead, ราคาที่จ่าย per publisher)?

**ผู้เชี่ยวชาญด้าน AI:** ทางเทคนิคนี่คือ RAG-with-attribution ที่ทำ **grounding** จากคลังข่าวคุณภาพสูงของ Nine ลด hallucination บนคำถามข่าวสารเฉพาะประเทศ (ออสเตรเลีย/AU-Pacific). คำถามเปิดคือ **freshness SLO**: การ index เข้าคลัง grounding นานแค่ไหน (นาที? ชั่วโมง?) และ Copilot จะแยก breaking-news query กับ evergreen-fact query อย่างไร. อีกจุด — pattern การจ่ายเงินต่อ **outbound click** เทียบกับ per-token-referenced ยังเป็นตัวแปรที่โมเดล pricing ระหว่าง publisher/AI vendor จะแยกกันชัดในอีก 2-3 quarter ข้างหน้า.

**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่สร้าง **content-heavy AI product**: บทเรียนคือ *plan for licensing before scaling retrieval*. อย่ารอให้ growth ดึงความสนใจจาก legal ของ publisher; ออกแบบ pipeline ให้มี clean split ระหว่าง **licensed corpus** (มี attribution + click-through) กับ **open crawl** (มี fallback + user-visible source label) ตั้งแต่วันแรก. เก็บ event สำหรับ outbound click จาก AI answer เพื่อใช้เป็น evidence ในการเจรจา licensing ในอนาคต — ตัวเลขนี้จะเป็น bargaining chip.

## 2. Bloomberg — Allianz's Subran: AI productivity hopes show "exuberance"

**อาจารย์ (มหาวิทยาลัย):** เชื่อมกับ Robert Solow "productivity paradox" ของยุค 1987 ("computers everywhere except in the productivity statistics") ให้ตรงๆ — Subran กำลังพูดในกรอบเดียวกันแค่เปลี่ยนเทคโนโลยี. โจทย์ class: หา 3 mechanism ที่ทำให้ AI productivity ไม่กระจายเท่ากันข้าม sector/ประเทศ (skill complementarity, capital intensity, regulatory drag) — แล้วเทียบกับกรอบ Brynjolfsson-Rock-Syverson (2018) "productivity J-curve" ว่า J-curve ของ AI จะสั้นหรือยาวกว่ารอบ ICT-1990s.

**ผู้เชี่ยวชาญด้าน AI:** สังเกตว่าเสียงเตือนแบบนี้มาจาก **ฝั่ง insurer/asset manager** ที่ pricing risk เป็นอาชีพ ไม่ใช่ tech skeptic ปกติ — สัญญาณว่า market participant ที่มี balance sheet exposure เริ่มไม่สบายใจกับ valuation ที่ pricing productivity gain ล่วงหน้า. ทางเทคนิค คำถามคือ **inference cost curve** จะไปเจอ **useful-work-per-dollar** curve ที่จุดไหน — ถ้า marginal cost ของ token ลดเร็วกว่าที่ enterprise ดูดซับได้ก็ยิ่งเสริม "exuberance"; ถ้าลดช้ากว่า, Uber/Tesla-style token rationing จะเป็น new normal.

**โปรแกรมเมอร์มืออาชีพ:** ผลตรงต่อทีม product: ผู้บริหารเริ่มถามหา **ROI per AI feature** ในรอบ budget ครึ่งปีหลัง. เตรียม dashboard 3 ตัวก่อนโดนถาม — (1) cost per successful task ของ AI feature, (2) latency-adjusted user engagement เทียบก่อน-หลังเปิด AI, (3) refund/complaint delta ที่ผูกกับ AI. ถ้าตัวเลขไม่ดี อย่ารอ CFO ปิด — เสนอ scope-down/model-downgrade เข้าไปเองก่อน; เจ้าของโปรเจกต์ที่ใช้ตัวเลขเปิดใน review ได้เปรียบเจ้าของโปรเจกต์ที่ปกป้อง scope ด้วย narrative.

## 3. TechCrunch — "The only AI glossary you'll need this year"

**อาจารย์ (มหาวิทยาลัย):** ใช้เป็น **anchor artifact** ในหลักสูตร AI literacy ต้นเทอมนี้ — บทเรียนคือคำใหม่จำนวนมาก (RAG, RLHF, hallucination, agentic, MoE, tool-use) กลายเป็น **ศัพท์อาชีพ** ที่ผู้ไม่ใช่นักวิทยาการคอมยังต้องเข้าใจเพื่อทำงาน. โจทย์ class: ให้แต่ละคนเลือก 3 คำ ทำ 1-slide "used-vs-misused-in-the-wild" — บังคับให้แยก definition กับ marketing framing ของแต่ละคำ.

**ผู้เชี่ยวชาญด้าน AI:** glossary แบบนี้มีคุณค่าที่มัน **freeze definition** ในจุดเวลาหนึ่ง — คำอย่าง "agent" หรือ "reasoning" ความหมายเลื่อนทุก quarter ตาม vendor. จับ delta จาก glossary ปีต่อปีเป็นสัญญาณว่าอุตสาหกรรมตกลงเรื่องอะไรได้ (LLM = โมเดล transformer, RAG = retrieval+generation) และเรื่องไหนยังไม่ตกลง ("agentic" ยัง overload อย่างชัดเจน). สำหรับ practitioner ประโยชน์รอบสองคือใช้เป็น **checklist ของ concept** ที่ต้องรู้เมื่อออกแบบระบบ.

**โปรแกรมเมอร์มืออาชีพ:** ปฏิบัติการ — ตั้ง **team glossary** ในภาษาของทีมเอง (Confluence/Notion/README) ใช้ glossary นี้เป็นจุดเริ่มต้น แล้วเพิ่มคอลัมน์ "ใช้ในโค้ดเราที่ไหน" กับ "ตัวชี้วัดคือ metric ตัวไหน". ประโยชน์เห็นชัดในการ onboard เพื่อนใหม่และในการ code review — คำเดียวกันในหมู่ ML researcher กับ backend engineer มักตีความไม่ตรงกัน ทำให้เกิด bug ที่ผู้จัดการมองไม่เห็น.

## 4. TechCrunch — AI browser wars: the fight shifts from search to who acts inside the browser

**อาจารย์ (มหาวิทยาลัย):** เคสสอน **platform substitution** ระดับ classical — ผู้ครองพื้นที่เดิม (Google) ถือ browser ที่กลายเป็น distribution channel; ผู้ท้าชิงจากด้านโมเดล (OpenAI, Perplexity, Anthropic ผ่าน partner) พยายามทำให้ browser เป็น interface ของ agent ตัวเอง. โจทย์: ถ้าประวัติศาสตร์ IE→Firefox→Chrome ใช้เวลา ~5 ปี ต่อ substitution รอบ, รอบ AI-browser จะเร็วหรือช้ากว่า และ **switching cost** ตอนนี้อยู่ที่ปัจจัยไหน (bookmarks? password manager? sign-in? agent memory?)

**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่น่าจับตาไม่ใช่ browser ตัวใด แต่คือ **agent-web protocol** ที่แต่ละค่ายกำลังยัดผ่าน browser ของตัวเอง (Model Context Protocol ของ Anthropic, computer-use APIs ของ OpenAI, Gemini action bridge ของ Google). ถ้าฝั่งใดครองเกม **credential/session delegation** แบบมาตรฐาน จะเป็น analog ของ TCP/IP รอบใหม่. คำถามเปิด: **security posture** — agent ที่กด click แทนคน หมายความว่า phishing surface, session-hijack risk, และ regulatory liability (ใครรับผิด เมื่อ agent กด "confirm purchase" ผิด?) ยังไม่มีคำตอบมาตรฐาน.

**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ทำเว็บ product: (1) เริ่ม **audit UI ของตัวเอง** ว่า agent-friendly หรือไม่ — semantic HTML, accessible labels, stable selectors เป็นสิ่งที่ทั้ง screen-reader และ AI agent ต้องการเหมือนกัน; (2) วางแผน **rate-limit + bot-detection strategy** ที่แยก legit AI agent (User-Agent claim + verifiable signature) จาก scrape bot ก่อนที่ traffic pattern จะแตก; (3) เตรียม **agent-API surface** (structured intent endpoint) ให้ agent ทำงานตรงแทนที่จะ scrape UI — ทั้งประหยัด token ให้ user ปลายทางและควบคุม UX ของตัวเองได้.
