# Perspectives — 2026-09-22

## 1. OpenAI forms math advisory group as its AI resolves more than 100 open problems

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ควรใช้สอนความต่างระหว่าง "แก้โจทย์เปิด" กับ "สร้างทฤษฎีใหม่" — การได้ 100+ open problem น่าตื่นเต้น แต่ต้องดูว่าปัญหาเหล่านั้นเปิดอยู่จริงมานานแค่ไหนและมีการ peer-verify แล้วยัง ก่อนที่จะเข้าคลาสว่ามัน "แก้ได้แล้ว".
**ผู้เชี่ยวชาญด้าน AI:** การตั้ง advisory group ที่ IAS สะท้อนว่า OpenAI ต้องการ external mathematician หา failure mode ในการอ้าง proof — คำอ้าง "resolved 100 problems" ไม่มีความหมายจนกว่าจะเปิด proof/ledger ให้ตรวจแบบ Lean หรือ Coq; หมั่นถามหา verification pipeline ก่อนเชื่อสถิติ.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าจะเอา math-capable model นี้ไปใช้จริง ให้แยก use case ระหว่าง "generate candidate solution" กับ "verify solution" — pipeline ที่ต่อ formal-verifier (Lean/Coq/Z3) ต่อจาก LLM output จะปลอดภัยกว่าการเชื่อคำตอบตรงๆ.

## 2. OpenAI Urges US to Lead Global Effort on AI Safety Standards

**อาจารย์ (มหาวิทยาลัย):** ใช้เป็น case ในคาบ international relations — บริษัทที่ปกติต่อต้าน regulation กลับมาเรียกร้อง global standard เพราะกลัวการแข่งขันจากลาบูรอนาม; ให้นักศึกษาเทียบกับ Basel Accords หรือ Montreal Protocol ว่าทำไม industry sometimes wants regulation.
**ผู้เชี่ยวชาญด้าน AI:** OpenAI เสนอให้สหรัฐเป็นผู้นำ standard-setting = OpenAI ต้องการ influence เกณฑ์วัดก่อนจีน/EU กำหนดเอง; ต้องดูว่า proposed standard วัด capability หรือวัด process — ถ้าวัดแค่ process เท่ากับ regulatory capture โดย incumbent ที่ผ่าน audit ได้ง่ายกว่า.
**โปรแกรมเมอร์มืออาชีพ:** ถ้ามาตรฐานออกมาจริง ปีหน้าจะเห็น compliance stack ใหม่ (documentation, model card ที่ audit ได้, third-party eval) — เตรียม tooling ที่ export model metadata + eval logs เป็น format มาตรฐานตั้งแต่วันนี้ อย่ารอ deadline.

## 3. Meta's AI agent has been blocked from using Amazon.com

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เปิดคำถามเรื่อง "AI agent interoperability" ในคาบ digital economics — เมื่อ agent ซื้อของแทนคน ใครเป็นเจ้าของ intent? Amazon ที่บล็อกเพราะเสียโฆษณา หรือ Meta ที่พา user มา checkout? ให้ debate ทั้งมุมกฎหมาย antitrust และผู้บริโภค.
**ผู้เชี่ยวชาญด้าน AI:** Amazon กำลังส่งสัญญาณว่า "agent-friendly" ไม่ใช่ default — retailer ใหญ่จะบังคับ agent วิ่งผ่าน API ที่จ่าย fee หรือใส่ TOS ห้าม automated purchase; อย่าออกแบบ agent stack ที่ assume open web scraping จะทำงานได้ตลอด.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าโปรเจกต์ตัวเองพึ่ง browser-automation agent (Playwright + LLM) เข้าเว็บใหญ่ ต้อง plan fallback: (1) official API integration, (2) affiliate partnership, (3) graceful degrade บอกผู้ใช้เมื่อ upstream บล็อก — วิ่งชน 403/CAPTCHA แล้วปล่อย silent failure จะพัง trust.

## 4. Google's $899 Googlebook is a bet that you'll buy a new laptop for Gemini

**อาจารย์ (มหาวิทยาลัย):** ใช้ในคาบ HCI/product design เทียบ Chromebook เดิม (browser-first) กับ Googlebook (AI-first) — เมื่อ "primary input" เป็น natural language ไม่ใช่ keyboard shortcut, ทั้ง interaction pattern และ mental model ของผู้ใช้จะเปลี่ยนอย่างไร; ให้นักศึกษาออกแบบ heuristic evaluation ใหม่.
**ผู้เชี่ยวชาญด้าน AI:** AI-powered cursor + vibe-coded widget = Google กำลัง bet ว่า OS layer จะเข้าใจ context ทั้งเครื่องได้ดีกว่า app-level assistant; แต่ประสบการณ์ Apple Intelligence สอนว่า on-device inference latency + battery ยังยากมาก — ต้องรอ benchmark จริงก่อนตัดสิน.
**โปรแกรมเมอร์มืออาชีพ:** ราคา $899 คือกลุ่ม mid-range Chromebook + iPad — target คือ prosumer/educator ไม่ใช่ developer; ถ้าจะพัฒนา extension บน Googlebook ต้องรอ ChromeOS/Aluminium OS API สำหรับ Gemini action ที่ Google ประกาศตามหลัง อย่ารีบ port app จนกว่าจะเห็น SDK ที่ยั่งยืน.

## 5. Jensen Huang บอกมีโอกาส 0% ที่ AI แซงหน้ามนุษย์จนสิ้นโลกในปี 2030

**อาจารย์ (มหาวิทยาลัย):** เปิดคาบวิทยาศาสตร์กับสังคม — คำว่า "0%" ในบริบททางสถิติแปลว่าอะไร? นักวิทยาศาสตร์ปกติไม่พูด 0% เพราะเป็น absolute claim; ให้นักศึกษาวิเคราะห์คำพูดผู้บริหารเทคที่มี conflict of interest (Nvidia ขาย GPU ให้ทุกคน).
**ผู้เชี่ยวชาญด้าน AI:** Huang ประกาศ 0% หลังจากเมื่อไม่กี่สัปดาห์ก่อนสนับสนุน "Pace the Frontier" ของ Amodei = position drift ที่สะท้อน incentive มากกว่า evidence; อ่านคู่กับข่าว OpenAI push regulation จะเห็นว่า Big AI split ชัดเจนระหว่าง "safety-first" (Anthropic/OpenAI ที่ตอนนี้) และ "speed-first" (Nvidia).
**โปรแกรมเมอร์มืออาชีพ:** อย่าเอา existential-risk debate มาปนกับ operational risk วันนี้ — ระบบ production มี concrete risk (prompt injection, hallucination, data leak) ที่ต้อง mitigate ตอนนี้ ไม่ว่า P(doom) จะ 0% หรือ 25%; วาง evaluation harness + guardrail ก่อน แล้วปล่อยให้ CEO ทะเลาะกันเอง.
