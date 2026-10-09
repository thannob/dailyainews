# Perspectives — 2026-10-09

## 1. Google brings agentic AI to Gemini, starting with businesses

**อาจารย์ (มหาวิทยาลัย):** สิ่งที่ควรสอนในห้องเรียนตอนนี้คือการแยกระดับของ "agent" ให้ชัด Gemini agent ไม่ใช่แค่ chatbot ที่ตอบเร็วขึ้น แต่คือการที่ provider เริ่มขายโมเดลที่ทำงานต่อเนื่องข้ามวัน สร้าง sub-agents และตัดสินใจเอง นักเรียนควรเข้าใจทั้งข้อดี (ลด overhead ของการสั่งงานซ้ำ) และข้อจำกัด (ปัญหาเรื่อง accountability เมื่อ agent สร้าง agent)

**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่ใหม่จริงในวันนี้ไม่ใช่ "มี agent" เพราะ Vertex AI มี agent มาก่อน สิ่งที่ใหม่คือการ positioning agent เป็น "universal agent for work" ที่ cross-platform (Workspace + third-party) และการเปิดให้ sub-agents เป็น primitive ที่ตั้งใจไว้ตั้งแต่ต้น ไม่ใช่ workaround การที่ Google ประกาศว่า agent สามารถเรียกใช้ Claude ของ Anthropic ได้ด้วย สะท้อนว่า vendor lock-in ไม่ใช่กลยุทธ์หลักอีกต่อไป — การเป็น runtime ที่ควบคุม context กลายเป็นเป้าหมายใหม่

**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมเราใช้ Workspace หรือ Gemini อยู่แล้ว ควรเริ่มทดลองสร้าง agent จาก task ที่ซ้ำๆ ก่อน เช่น การสรุปอีเมล หรือ onboarding checklist แต่ไม่ควรพึ่ง sub-agents สำหรับงานที่มี side effects ภายนอกจนกว่า Google จะชี้แจง IAM และ audit log ของ sub-agent ให้ชัด เพราะในปัจจุบัน early access ยังไม่มีเอกสาร governance ที่ครบ
