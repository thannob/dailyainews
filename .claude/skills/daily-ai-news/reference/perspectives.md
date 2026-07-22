# Perspectives — 2026-07-22

## 1. Google releases Gemini 3.6 Flash + 3.5 Flash-Lite + 3.5 Flash Cyber

**อาจารย์ (มหาวิทยาลัย):** เคสตัวอย่างที่ดีของ product-line segmentation — Google แตก Flash tier ออกเป็น 3 แขนง (workhorse / cheapest / cyber-specialised) ใน launch เดียว; ให้นักศึกษาถกว่าเมื่อไรควรมีหลาย SKU และเมื่อไรกลายเป็น cannibalisation.
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข "17% fewer output tokens" น่าสนใจกว่าราคา — สื่อว่า Google กำลัง compress reasoning trace ให้สั้นลงโดยไม่ลด quality; ถ้าจริง นี่คือ efficiency win ที่ transfer ไปยัง Gemini 4 (ซึ่งเริ่ม pre-training แล้ว) ได้ ประเด็นที่ต้องระวังคือ 3.5 Pro ยัง delay — ช่องว่างระหว่าง Flash และ Pro tier เริ่มกว้างขึ้น.
**โปรแกรมเมอร์มืออาชีพ:** ราคาลงจาก $9 → $7.50 ต่อ 1M output token ช่วยลด bill ทันทีสำหรับ agent workflow ที่หมุน tool-call เยอะ; ให้ swap 3.5 Flash → 3.6 Flash ใน eval harness ภายในสัปดาห์นี้ก่อน promote to production — 17% token saving คูณ volume จริงคือประหยัดจริง ไม่ใช่แค่ marketing.

## 2. OpenAI Codex + ChatGPT Work agents reach 10M users

**อาจารย์ (มหาวิทยาลัย):** เป็น datapoint สอน metric literacy ได้ตรง — "10M users" ที่ไม่ระบุ DAU/WAU/point-in-time คือ metric ที่ audit ไม่ได้; ให้นักศึกษาลิสต์คำถามที่ analyst ควรถามก่อน quote ตัวเลขต่อ.
**ผู้เชี่ยวชาญด้าน AI:** การรวม Codex + ChatGPT Work เป็น "agents" ก้อนเดียวสะท้อน OpenAI internal roadmap — agent เป็น business line ใหญ่พอที่จะ report แยก; แต่ 10M ในเวลา ~2 สัปดาห์หลัง ChatGPT Work launch (9 ก.ค.) บ่งบอก enterprise seat push มากกว่า organic adoption.
**โปรแกรมเมอร์มืออาชีพ:** ตัวเลขนี้ไม่ใช่ signal ให้ commit vendor lock-in — แต่คือ signal ว่า agent workflow กำลัง cross chasm ในองค์กร; ทีมที่ยังไม่ได้วาง governance (audit log, permission scope, cost cap ต่อ agent-run) ควรวางภายในไตรมาสนี้ก่อน seat expansion จะ outpace controls.

## 3. Nvidia Vera Rubin shipping to customers

**อาจารย์ (มหาวิทยาลัย):** เคสสอน supply-chain concentration ระดับ classic — 1 vendor + ~5 hyperscaler customer + สถาปัตยกรรม 1.3M ส่วนประกอบจาก 20 ประเทศ; ใช้เปิดคำถามใน operations/strategy ว่า geopolitical risk บน chip supply chain ใหญ่แค่ไหน.
**ผู้เชี่ยวชาญด้าน AI:** "10× token throughput ของ NVL72 rack" ต้องอ่านด้วยความระวัง — เป็น CoreWeave-side claim ที่ยังไม่มี independent bench; แต่ถ้าใกล้จริง คือ 1 order of magnitude ใน inference cost ต่อ token ที่จะ compress margin ของทุก inference-heavy startup ในปีหน้า.
**โปรแกรมเมอร์มืออาชีพ:** ระยะสั้น (Q3-Q4 2026) ควรคาดว่า inference latency + คิว availability บน serverless GPU provider จะดีขึ้นสำหรับ large-context workload; แต่อย่ารีบ redesign architecture จน hyperscaler ปล่อย Rubin-backed instance ราคาจริง — cost curve ต้องเห็นก่อน commit.

## 4. US threatens sanctions on Chinese AI models over IP theft

**อาจารย์ (มหาวิทยาลัย):** เคสเชื่อม policy + ML — คำถามสอนที่แหลม: "IP theft ของ model weights" หมายถึงอะไร (training data? distilled outputs? architecture?); ต่างจาก IP บน silicon อย่างไร; และ enforceable แค่ไหนเมื่อ weights เป็นไฟล์ที่ mirror ได้ทันที.
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณสำคัญคือรัฐกำลัง frame open-weight model จีนเป็น national-security asset — ต่อจาก Moonshot K3 wave; ผลจริงต่อ research community คือ US lab จะยิ่งลังเลปล่อย open-weight (fear ของ downstream sanctions), และ community จะแบ่งขั้วเร็วขึ้น.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าใช้ Kimi K3 หรือ Qwen/GLM ใน production ให้เตรียมนโยบายและ dual-vendor plan วันนี้ — sanctions ยังไม่เกิด แต่ risk ของการ enforce (host takedown, API cut-off, downstream user list requirement) พอที่จะไม่ควรพึ่ง single Chinese provider สำหรับ mission-critical path.

## 5. Jack Dorsey launches Buzz (Block) — chat + AI agents, model-neutral, open-source

**อาจารย์ (มหาวิทยาลัย):** เคสสอน platform strategy ที่ตรงข้ามกับ vendor-first launch ทั่วไป — "model-neutral, decentralised, self-sovereign, open source" คือการเดินสวนกระแส walled-garden ของ Slack/Teams; ให้นักศึกษาเปรียบเทียบว่า business model ไหน sustainable กว่าใน 3 ปี.
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่ใหม่ไม่ใช่ Slack-clone แต่คือ "agents เป็น first-class participant ในห้อง" — เปลี่ยน chat จาก human-to-human channel เป็น multi-agent coordination surface; ถ้า protocol เปิด agent จาก vendor ต่างกันจะเจอกันในห้องเดียวได้ (ใกล้กับที่ MCP กำลังทำใน tool layer).
**โปรแกรมเมอร์มืออาชีพ:** ยัง "early stage" ตามที่ Buzz เองประกาศ — ยังไม่ควรย้ายทีมจาก Slack วันนี้; แต่ควร clone repo และรันดู UX ว่า agent-in-channel model จะ fit workflow ของทีมไหม; ถ้า Buzz protocol ได้แรง ผู้ชนะจะเป็นทีมที่ push agent-adapter ตัวแรกๆ ให้ครอบคลุม ecosystem ของตัวเอง.
