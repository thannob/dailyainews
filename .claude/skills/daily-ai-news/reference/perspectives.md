# Perspectives — 2026-06-05

## 1. WWDC 2026 — Siri's Gemini-powered revamp (TechCrunch)

**อาจารย์ (มหาวิทยาลัย):** เคสคลาสสิกของ "build vs. buy" — Apple ใช้เวลา 3 ปีพยายาม build LLM in-house แล้วท้ายที่สุดเลือก partner กับคู่แข่งโดยตรงเพื่อรักษา product timeline; ใช้สอน strategic flexibility และ vertical-integration limits ในวิชา corporate strategy ได้ทันที
**ผู้เชี่ยวชาญด้าน AI:** "Gemini under the hood" หมายความว่า Apple Intelligence layer (privacy framing, on-device routing) คือ surface — model brain คือของ Google สิ่งที่น่าจับตาคือ Apple ปรับแต่ง Gemini แค่ไหน และ Private Cloud Compute จะ host model weight เองหรือ proxy ไป Google Cloud
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมพัฒนา iOS app ที่ integrate กับ Siri Shortcuts / App Intents ต้องเตรียม redesign intent schema สำหรับ "multi-step / conversational" ภายในไตรมาส 3 — และ standalone Siri app ที่รับ document upload จะกลายเป็นช่อง distribution ใหม่สำหรับ App Intent-based feature

## 2. Microsoft AI Chief — Anthropic models too expensive (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** Public framing "supplier เราแพง" เป็น vertical-integration signaling — ใช้สอน buyer power และ make-vs-buy economics ตำรา Porter; Microsoft กำลังลดความเสี่ยง supplier dependency หลังจาก lock-in กับ OpenAI/Anthropic เกือบ 3 ปี
**ผู้เชี่ยวชาญด้าน AI:** "Too expensive" จาก Suleyman = signal ว่า MAI family (เปิดตัวที่ Build 2026 เมื่อ 2-3 มิ.ย.) จะถูก position เป็น default model ของ Copilot stack; เป้าหมาย "absolute frontier by 2027" ต้องการ training compute ที่ดูจะมาจาก self-built cluster ไม่ใช่ Azure shared capacity
**โปรแกรมเมอร์มืออาชีพ:** ถ้าใช้ Claude ผ่าน Azure AI Foundry/AI Services — เตรียม pricing change ภายใน 2-3 ไตรมาส; ถ้าทีม build agent บน Copilot Studio ให้ทดสอบ MAI-Thinking-1 ทันทีที่ private preview เปิด เพราะ default model picker จะ shift

## 3. Cerebras — works with everyone except Nvidia (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** Strategic positioning ของ challenger ที่เลือก "ไม่เป็นมิตรกับเจ้าตลาด" เพื่อ define identity — ใช้สอน blue-ocean strategy + competitive positioning; เทียบกับ AMD ที่เลือก co-exist กับ Intel ในยุค 2000
**ผู้เชี่ยวชาญด้าน AI:** ดีล 750 MW ของ OpenAI-Cerebras เป็น datapoint ใหญ่ — ที่ inference workload (ไม่ใช่ training) ของ frontier model กำลัง diversify ออกจาก H100/H200/B200 architecture; wafer-scale engine ของ Cerebras (CS-3) เหมาะกับ token throughput ที่ต้องการ low-latency ของ reasoning model
**โปรแกรมเมอร์มืออาชีพ:** ถ้า serve model production ผ่าน OpenAI API อาจไม่เห็นความต่างโดยตรง แต่ latency profile + cost-per-token ของ reasoning model อาจ shift เมื่อ traffic routed ไป Cerebras — ติดตาม API response header `openai-organization-routing` หรือเทียบ TTFT (time-to-first-token) ก่อน-หลัง

## 4. Verizon CEO — AI will replace many customer service roles (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** Public CEO statement ว่า AI จะแทน "large percentage" ของ CS workforce เป็น empirical milestone สำหรับ labor economics — ใช้สอน skill-biased technological change + Acemoglu/Restrepo framework; ปี 2024-25 เป็น "AI augmentation" rhetoric, 2026 เริ่มเห็น "AI substitution" rhetoric ชัดเจน
**ผู้เชี่ยวชาญด้าน AI:** "easy queries (password recovery, billing) → AI; complex → human + agent" คือ classic two-tier routing pattern ที่ทุก enterprise contact center จะ adopt — สิ่งที่ Verizon ไม่บอกคือ accuracy threshold + fallback rate ที่จะตัดสินใจ when to escalate
**โปรแกรมเมอร์มืออาชีพ:** ถ้า build agent stack สำหรับ contact center — ลงทุนใน orchestration layer (router + fallback + escalation) มากกว่า single best-model; SLA สำคัญคือ "false-confidence rate" ของ agent (ไม่ใช่แค่ accuracy) — agent ที่ตอบผิดอย่างมั่นใจคือ liability ใหญ่กว่า agent ที่ขอ escalate

## 5. AI Market Boom underwritten by Anthropic/OpenAI/SpaceX IPO trillions (Bloomberg)

**อาจารย์ (มหาวิทยาลัย):** Concentration risk ของ market rally ที่ค้ำด้วย IPO valuation ระดับ ~$1T ของ 2 บริษัทที่ revenue ยังต่ำกว่า valuation มาก — ใช้สอนเป็น contemporary case ของ dot-com analogy (กับ caveat ว่า revenue/compute spend จริง vs. 1999)
**ผู้เชี่ยวชาญด้าน AI:** ถ้า OpenAI + Anthropic ขึ้น public market ใน 2026 H2 → quarterly earnings disclosure จะ force ทั้งคู่ disclose unit economics (cost per training run, gross margin per token); สิ่งที่ AI research community รอคอยมาตลอด finally จะเห็น เพราะตอนนี้ทุก vendor ปกปิดด้วย "private company"
**โปรแกรมเมอร์มืออาชีพ:** ภายในปีนี้คาด vendor pricing จะ "rationalize" ขึ้น (เพื่อ improve quarterly margin) — ลด surprise cost shock โดย cache prompt aggressively, ใช้ batch API, ทดสอบ smaller-tier model ก่อน lock-in flagship; ติดตาม S-1 filing ของ Anthropic + OpenAI เมื่อ public เพราะจะมี roadmap hints ที่ vendor ไม่เคยเปิดเผยมาก่อน
