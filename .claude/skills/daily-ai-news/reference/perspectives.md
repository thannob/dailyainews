# Perspectives — 2026-05-17

## 1. The haves and have nots of the AI gold rush (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้คือเคสคลาสสิกของ winner-take-most economy ในอุตสาหกรรมที่ network effects + compute moat รวมศูนย์ — ตัวเลข "~10,000 คน เกิน US$20M" สอนวิชา labor economics ได้ดีกว่าตำราเรียน เพราะมันแสดง wealth concentration ที่ระดับ workforce ไม่ใช่แค่ระดับ shareholder
**ผู้เชี่ยวชาญด้าน AI:** น่าจับตาว่าวลี "vibes อยู่ในจุดแย่ที่สุด" ของ Deedy Das ไม่ใช่เรื่อง bubble — แต่เป็นเรื่อง opportunity asymmetry ที่ talent ไหลไปอยู่ 3 บริษัทเดียว ทำให้บริษัทเล็กแย่งทีมยากขึ้นและ R&D นอกวง frontier ช้าลง
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ dev ที่ไม่ได้อยู่ใน frontier lab ข้อสรุปไม่ใช่ "จะรวยหรือไม่รวย" แต่คือ "อย่าเทียบ comp กับเพื่อนที่อยู่ใน frontier lab" — focus กลับไปที่งานที่ value ของเราถูกวัดจาก deliverable จริง ไม่ใช่ paper wealth ของหุ้น pre-IPO

## 2. Cerebras IPO US$60B (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ดีสำหรับสอนวิชา hardware-software co-design — wafer-scale chip คือ bet ว่า memory bandwidth คือคอขวดจริงของ inference ไม่ใช่ FLOPS ทฤษฎีนี้ถูกพิสูจน์ตลาดในวันที่ Cerebras IPO ทะลุ US$60B
**ผู้เชี่ยวชาญด้าน AI:** การที่ Cerebras ขายชิปให้ OpenAI และ AWS แปลว่า inference ที่ใหญ่จริงๆ ในตลาดเริ่มแยกออกจาก training stack แล้ว — NVIDIA ยังครอง training แต่ inference เริ่ม fragmented Cerebras + Groq + Trainium ฯลฯ แข่งกันใน latency/throughput per dollar
**โปรแกรมเมอร์มืออาชีพ:** ผลตรงกับงานเราคือ "vendor neutrality ที่ inference layer" จะเริ่มจ่ายคืน — ถ้าทีมเรา hard-code OpenAI API ไว้ทั่วระบบ ตอนนี้คือเวลาเริ่ม abstract ผ่าน LiteLLM/OpenRouter/vLLM-compatible เพื่อจะสลับไปยัง inference provider ที่ Cerebras-powered ได้เมื่อราคาเหมาะ

## 3. Greg Brockman คุม product strategy ที่ OpenAI (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** การที่ผู้ร่วมก่อตั้งกลับมาคุม product ช่วงที่ CEO of AGI Deployment ลาป่วย เป็นกรณีศึกษา succession risk ของบริษัทที่ valuation พึ่ง key person สูงมาก — นักศึกษา MBA ควรใช้เคสนี้ดู governance ของบริษัท frontier AI
**ผู้เชี่ยวชาญด้าน AI:** Brockman เป็น engineer-founder ที่เคยขับ product direction ของ GPT-3/4 era — การที่เขาย้อนกลับมาคุม product strategy ในช่วงที่ OpenAI กำลังขยายไปทาง consulting/finance/agents บอกว่าทิศของ product อาจจะ rebalance กลับไปทาง core API/model มากกว่า vertical SaaS
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมคุณ ship feature ที่อ้างอิง roadmap ของ OpenAI (เช่น Codex CLI, Operator, Agents API) — เตรียม diff scenarios เพราะ product direction ใต้ leadership ใหม่อาจปรับ priority และ deprecation timeline ในไตรมาสหน้า

## 4. arXiv จะ ban นักเขียนที่ปล่อยให้ AI ทำทั้งหมด (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** นี่คือ policy ที่ใกล้กับห้องเรียนที่สุดในรายการวันนี้ — arXiv ไม่ได้แบน LLM ในงานเขียน แต่แบน "ปล่อยให้ AI ทำทั้งหมด" ขีดเส้นแบบนี้ใช้เป็น template ให้มหาวิทยาลัยร่าง policy ของตัวเองได้: ห้ามแบบ blanket จะ unenforceable; ห้ามที่ "no human substantive contribution" ปฏิบัติได้จริงกว่า
**ผู้เชี่ยวชาญด้าน AI:** ปัญหาทาง technical คือการ detect "AI ทำทั้งหมด" ทำได้ยากเมื่อ paraphrasing tool เก่งขึ้น — arXiv น่าจะใช้ moderation signal หลายชั้น (referee report, statistical fingerprint, author behavior) มากกว่า detector ตัวเดียว เป็น case study ดีของ AI governance ที่อาศัย process ไม่ใช่ tool
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ใช้ LLM ช่วยเขียน technical doc/RFC/PR description — บทเรียนคือ keep your fingerprint บนงาน: structure ที่เป็นของเรา, ตัวอย่างจาก codebase จริง, decision log ที่ traceable ถ้า output ของคุณ "AI-only" ก็แปลว่ามูลค่าของคุณคือ prompt ไม่ใช่ knowledge — ตำแหน่งเสี่ยงต่อ replacement สูงสุด

## 5. Stripe John Collison: Agentic Commerce จะเปลี่ยน e-commerce (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** ครั้งแรกที่ผู้บริหาร payments-infra ระดับ Stripe พูดเปิดเผยว่า "keyword search อาจไม่ใช่วิธีหาของอีกต่อไป" — ใช้สอนวิชา business model evolution: ถ้า discovery layer ของ commerce เปลี่ยนจาก SEO เป็น agent-to-agent บทบาทของ retailer/ad network/aggregator จะถูก rewrite ทั้งหมด
**ผู้เชี่ยวชาญด้าน AI:** ใจกลางของ agentic commerce คือ AI agent ต้อง authenticate, authorize, และ pay แทนผู้ใช้ — Stripe เป็นบริษัทเดียวที่มี infrastructure ครบทั้ง 3 ชั้นในวันนี้ การที่ Collison พูดเองแปลว่า Stripe กำลัง position ตัวเองเป็น "Plaid ของ agent payments"
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่ทำ e-commerce/marketplace ต้องเริ่มเปิด structured product feed (schema.org/Product + price/availability ที่ machine-readable) เพราะ agent shopping จะใช้ feed ก่อน HTML scrape เรื่อง checkout ฝั่ง backend ต้องเตรียม idempotency key + agent-friendly OAuth scope เพื่อรองรับ payment flow ที่ trigger โดย agent ไม่ใช่ human click
