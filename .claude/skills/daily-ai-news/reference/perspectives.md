# Perspectives — 2026-10-23

## 1. Anthropic donates Agent Skills open standard to the Agentic AI Foundation

**อาจารย์ (มหาวิทยาลัย):** การย้ายมาตรฐานออกจาก vendor ไปสู่ foundation ที่เป็นกลางเป็น case study คลาสสิกเรื่อง "governance ของมาตรฐานเปิด" ที่ควรบรรจุในวิชา software standards หรือ open-source strategy นักเรียนควรเปรียบเทียบจังหวะและเงื่อนไขของการบริจาค MCP (ธันวาคม 2025) กับ Agent Skills (ตุลาคม 2026) เพื่อเข้าใจว่าทำไมบริษัทที่สร้างมาตรฐานถึงยอมปล่อยให้คู่แข่งมีสิทธิ์ร่วมกำหนดอนาคต

**ผู้เชี่ยวชาญด้าน AI:** ประเด็นสำคัญคือการที่ Agent Skills ได้ตัวเลข 70+ platform และ 1 ล้าน skill ภายในปีเดียว แสดงว่า format นี้ตอบโจทย์จริง — เป็นชั้นที่ง่ายและเบากว่า MCP สำหรับ workflow เฉพาะงาน (ไม่ต้องรัน server) การย้ายไปอยู่กับ AAIF จะทดสอบว่า versioning policy และ security guidance จะโตเร็วพอรองรับการใช้งานขนาด 280 ล้าน install ได้ไหม โดยเฉพาะเรื่อง sandbox และ provenance ของ skill ที่ติดตั้งจากแหล่งที่ไม่ใช่ผู้ผลิตโมเดลเอง

**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ใช้ Agent Skills อยู่แล้ว ข่าวนี้ลด vendor lock-in risk ลงไปขั้นหนึ่ง — spec กับ domain `agentskills.io` ไม่ได้อยู่ใต้ Anthropic อีกต่อไป จึงปลอดภัยกว่าที่จะเขียน skill ของทีมแล้วใช้ซ้ำข้าม Claude Code, ChatGPT, Cursor, GitHub Copilot และ VS Code งานที่ควรทำสัปดาห์นี้คือ (1) อ่าน proposal กระบวนการเปลี่ยนแปลง spec ที่ foundation จะเปิดให้คอมเมนต์ และ (2) ประเมินว่า skill ที่ทีมติดตั้งจาก directory ควรต้อง sign หรือ pin version ไหม ก่อนที่ security guidance ฉบับใหม่จะออก
