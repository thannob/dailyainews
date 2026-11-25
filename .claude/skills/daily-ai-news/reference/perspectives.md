# Perspectives — 2026-11-25

## 1. Even the best AI agents struggle with everyday life

**อาจารย์ (มหาวิทยาลัย):** เคสนี้สะท้อนช่องว่างระหว่าง benchmark แบบ single-turn (MMLU, HumanEval, ARC) กับงานในชีวิตจริงที่เต็มไปด้วย state ที่เปลี่ยน, interrupt, และข้อมูลไม่ครบ ควรให้นักเรียนออกแบบ eval ของตัวเองสำหรับงานประจำ (จองร้าน, ตอบอีเมล, อัปเดต CRM) แล้ววัด end-to-end success rate ไม่ใช่แค่ step-level accuracy
**ผู้เชี่ยวชาญด้าน AI:** ผลที่ "ยังทำไม่ได้" ไม่ใช่เรื่องความฉลาดของโมเดลเดี่ยว แต่คือเรื่อง orchestration, memory, และ error recovery — ที่สถาปัตยกรรม agent ส่วนใหญ่ยังอ่อน ควรดูว่า benchmark นี้แยก failure mode (hallucinated tool call, wrong state, loop) ออกจากกันได้ไหม
**โปรแกรมเมอร์มืออาชีพ:** อย่าเพิ่ง ship AI assistant ให้ end-user ก่อนสร้าง golden set งานจริง 20–30 ตัวที่สะท้อน workflow ของกลุ่มเป้าหมาย, วัด success rate ของ agent ปัจจุบัน, และกำหนด threshold ขั้นต่ำ เช่น ≥85% ก่อนปล่อย production demo สวยหลอกได้แค่ internal

## 2. UK warns AI-driven cyberattacks are exposing years of weak security

**อาจารย์ (มหาวิทยาลัย):** เรื่องนี้สอนเรื่อง "defense in depth" ได้ชัดเจน — autonomous attacker ที่ใช้ AI ไม่ได้ invent exploit ใหม่ แต่ค้นเจอ default credential, path traversal และ SQL injection ที่ CVE scanner จับมานานแล้ว แต่ไม่มีใครแก้ ชวนนักเรียน map ว่าช่องโหว่ไหนในระบบของมหาวิทยาลัยที่ "รู้ว่ามีแต่ยังไม่แก้" คือ low-hanging fruit ของ offensive AI
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณสำคัญคือ time-to-exploit ที่หดจากหลักเดือนเหลือหลักวัน/ชั่วโมง เพราะ autonomous agent สามารถ fan-out ไปทดลองช่องโหว่หลายรูปแบบพร้อมกัน patch cycle แบบ monthly maintenance window ไม่สอดคล้องกับ threat model นี้อีกต่อไป ควรคิด auto-patching หรือ compensating controls
**โปรแกรมเมอร์มืออาชีพ:** เปิด secret scanning + Dependabot/Renovate ให้ทุก repo ที่ team ดูแลภายในสัปดาห์นี้; ตั้ง pre-commit hook สำหรับ secret detection; ลบ default credential ใน Terraform/Ansible ที่ยังหลงเหลืออยู่; และทำ internal attack surface map — ไม่ใช่งานของทีม security อย่างเดียว

## 3. Why a Crusoe investor is betting on solar and batteries to power future AI data centers

**อาจารย์ (มหาวิทยาลัย):** ใช้เป็นเคส energy + compute economics — bottleneck ของ AI ปี 2026 ไม่ใช่ GPU แล้ว แต่คือ megawatt per inference ชวนนักเรียน engineering คำนวณว่าถ้าจะ train โมเดล 1T parameter ด้วย renewable + battery storage จริง ๆ จะต้องการ panel, battery capacity และ grid interconnect ขนาดเท่าไร เทียบกับ gas peaker ที่ใช้อยู่ตอนนี้
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นเทคนิคคือ solar+battery เหมาะกับ workload ที่ bursty และ latency-insensitive (inference, batch job) มากกว่า training ที่ต้อง sustained peak power ต่อเนื่องเป็นสัปดาห์ ถ้าอุตสาหกรรมแยก training/inference ในเชิง geographic ชัดขึ้น สถาปัตยกรรมของ model (checkpointing, elastic training) ก็ต้องปรับตาม
**โปรแกรมเมอร์มืออาชีพ:** workload ที่ไม่ต้อง real-time (batch analytics, nightly fine-tune, offline embedding) เริ่มคุ้มที่จะย้ายไป region ที่มี renewable abundance เพราะ provider ใหญ่จะเริ่มกำหนดราคาสะท้อน carbon cost และ grid stress; ทีมที่ดูแล inference pipeline ควรวัด watt-per-request ไม่ใช่แค่ latency และ cost per token
