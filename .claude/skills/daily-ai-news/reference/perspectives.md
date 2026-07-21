# Perspectives — 2026-07-21

## 1. Google "Frozen v2" chip for Gemini

**อาจารย์ (มหาวิทยาลัย):** เคสสอนคลาส systems / computer architecture ได้ดี — Google เลือก "แช่แข็ง" (freeze) โมเดล-specific ops เข้าซิลิคอนแลกกับความยืดหยุ่น เพื่อลด token-per-watt ให้ต่ำลงหลายเท่า; ให้นักศึกษาถกเปรียบ ASIC/TPU generation กับ GPGPU ในมิติ flexibility vs efficiency.

**ผู้เชี่ยวชาญด้าน AI:** 6–10× efficiency เทียบกับ TPU ปัจจุบันเป็นตัวเลข The Information — ยังไม่มี independent bench, และการฝัง architecture ลง silicon แปลว่า chip ล็อกกับ Gemini generation ที่ตายตัว; ถ้า Gemini architecture ปรับใหญ่ใน 2 ปี Frozen v2 อาจไม่คุ้มก่อนที่จะออก 2028.

**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบระยะสั้นยังไม่มี — chip มาปี 2028 — แต่ signal สำหรับทีม infrastructure คือ Google Cloud ยังตึงเรื่อง compute จนต้องปฏิเสธลูกค้าภายนอก; ทีมที่ผูกกับ Vertex/Gemini API ต้องมี fallback vendor และประเมิน rate-limit / quota shock ในระยะ 12–18 เดือน.

## 2. MCP 2026-07-28 spec update

**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างที่สอน distributed-systems 101 — จาก sticky-session ที่ตัดขวาง horizontal scale ไปสู่ stateless HTTP + client-side caching; MCP กำลังทำสิ่งที่ REST เคยทำในยุค 2000s ให้ agent tooling. ใช้เป็นเคสสอน API design + protocol evolution ได้ตรง.

**ผู้เชี่ยวชาญด้าน AI:** ประเด็นจริงไม่ใช่ session token — แต่คือ MCP เริ่มยอมรับว่ามันคือ standard ระดับโปรดักชัน ต้องรองรับ OAuth/OIDC, deprecation policy, extensions (Apps, Tasks); เท่ากับปิด gap ให้ enterprise adopt ได้จริงหลังจาก 12 เดือนของการทดลองในสาย OSS.

**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมรัน MCP server ใน production วางแผน migration ก่อน 28 ก.ค. — plain round-robin load balancer + `Mcp-Method` routing แทน sticky session, `tools/list` cacheable ตาม `ttlMs` ที่ server ส่ง; ประหยัด infra cost + ลด latency แต่ต้องทดสอบ auth flow ใหม่ที่ผูกกับ OAuth resource server.

## 3. Moonshot Kimi K3 — winners/losers ในตลาด

**อาจารย์ (มหาวิทยาลัย):** เคสสอน finance + strategy คู่กับ Bloomberg เมื่อวานเรื่อง Moonshot IPO — ตอนนี้เห็น "second-order effect" ของ K3 ผ่าน market repricing: memory-chip vendor (SK Hynix, Samsung) ได้อานิสงส์เพราะการแข่งโมเดลต้อง HBM มากขึ้น, IBM ที่เน้น enterprise software โดน sell-off ตามสมมติฐาน disruption; ให้นักศึกษาลิสต์ transmission channel 3 ชั้น (model → chip demand → equity).

**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข $314B wiped จาก valuation ของสองบริษัท US AI ไม่ใช่ fundamental — เป็น analyst-model repricing บน narrative; แต่การที่ SMIC เด้ง 5.4% ในวันเดียวสะท้อนว่า market เชื่อว่า China frontier lab จะเร่ง localise supply chain แล้วเสริม indigenous foundry — ผลกระทบภูมิรัฐศาสตร์ใหญ่กว่า benchmark.

**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ evaluate vendor cost ตอนนี้เป็นเวลาที่ Kimi K3 API "ราคาต่อผลลัพธ์" น่าดึงเข้าห้อง lab: benchmark กับ workload จริง (agent, coding, RAG) ก่อนสิ้นเดือน; แต่ระวังว่า Moonshot กำลังชนกำแพง GPU capacity (จากรายงานอื่นวันเดียวกัน) — ถ้าจะพึ่งพา ให้ mux กับ vendor ที่ SLA ยั่งยืน.

## 4. Natural — $30M Series A สำหรับ payment rail ของ AI agent

**อาจารย์ (มหาวิทยาลัย):** เปิดคำถาม "AI agent จะจ่ายเงินอย่างไรโดยไม่ต้องให้มนุษย์เซ็น" — เชื่อมโยงกับ payment law, KYC/AML, principal-agent theory; นักศึกษาที่เรียน fintech ควรอ่านคู่กับ AP2 (Agent Payments Protocol) ที่ Visa/Stripe/Google ประกาศเมื่อ 16 ก.ค. เพื่อเห็น standard war กำลังก่อตัว.

**ผู้เชี่ยวชาญด้าน AI:** เดิมพันของ Natural คือ "reinvent payment rail from scratch for agents" — เป็นเดิมพันสูง เพราะ Stripe ก็ทำอยู่ + Visa/Mastercard มีบัญชีทุกใบในโลก; ข้อได้เปรียบเดียวคือ speed ของ startup 193 วัน แต่ payment rail ที่ scale ต้องผ่าน compliance ที่ startup ไม่มี moat มาก่อน.

**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมกำลังสร้าง agent ที่ต้องซื้อของ / จ้าง service — วันนี้ยังยากที่จะให้ agent จ่ายเงินโดยไม่ผ่าน human confirmation; ติดตาม Stripe Agent Payments + AP2 protocol ก่อน commit กับ vendor ใหม่ที่ยังไม่มี audit trail; วางสถาปัตยกรรม abstraction ที่แลก payment provider ได้ง่าย เพราะ 12 เดือนข้างหน้าตลาดนี้จะเดือด.

## 5. YouTube ชี้แจงนโยบาย AI slop

**อาจารย์ (มหาวิทยาลัย):** ตัวอย่างสอน content policy + platform governance — YouTube ยืนยัน "tool-agnostic" (ใช้ AI ได้ ไม่ demonetise เพราะเครื่องมือ) แต่ตัดสินที่ "authenticity + original insight"; เปิดคำถามว่าใครเป็นผู้ตัดสินและ criteria วัดอย่างไร ใช้ในคลาส media studies หรือกฎหมายเทคโนโลยีได้.

**ผู้เชี่ยวชาญด้าน AI:** 3 bucket ที่ห้าม monetise (generic/repetitive, unsatisfying/off-putting, AI persona บน health/legal/finance/political) มีแค่ bucket 3 ที่ evaluable แบบ deterministic; bucket 1 และ 2 พึ่ง classifier ที่ subjective — เป็น governance gap ใหญ่ที่ creator กลุ่ม borderline จะโดน false-positive.

**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำ product ที่ generate video ให้ creator — เพิ่ม guard rail ตั้งแต่ pipeline: ห้าม deploy AI persona อธิบาย health/finance ไม่ว่ากรณีใด, เพิ่ม "editorial layer" ให้ creator ใส่ voice/insight ก่อน publish; และเก็บ metadata (prompt, model version, edit history) เพื่อ appeal ได้ถ้า channel โดน demonetise พลาด.
