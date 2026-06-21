# Perspectives — 2026-06-21

## 1. In the Weights — เว็บใหม่ที่ให้คุณค้นหา "ตัวเอง" ในน้ำหนักของโมเดล AI

**อาจารย์ (มหาวิทยาลัย):** เป็นเครื่องมือสอนแนวคิด "model parametrization" ที่ดีมาก — นักศึกษาเห็นรูปธรรมว่า "ความรู้" ของ LLM ฝังอยู่ในน้ำหนักของโมเดล และน้ำหนักนั้นไม่ใช่ตัวสะท้อนเป็นกลางของโลก แต่เป็นการเลือกว่าใคร/อะไร "สำคัญพอ" จะถูกเก็บเข้าไป
**ผู้เชี่ยวชาญด้าน AI:** ตัวเครื่องมือไม่ใช่ benchmark วิจัย เพราะวัดได้เฉพาะ recall โดยห้าม web search ซึ่งจะถูกบดบังด้วย post-training และ guardrail; แต่สิ่งที่น่าสนใจคือมันเปิดดีเบตเชิงนโยบายเรื่อง "training-data provenance" ออกสู่สาธารณะอย่างเข้าใจง่ายเป็นครั้งแรก
**โปรแกรมเมอร์มืออาชีพ:** มีค่าทันทีในงาน SEO / brand monitoring ยุคหลัง Google — ถ้าเว็บไซต์ของบริษัทไม่อยู่ใน weight ของโมเดลใหญ่ การ "ถูกเจอ" บน ChatGPT/Claude/Gemini จะลดลงเป็นกอบเป็นกำ ควรเริ่มทำ checklist "ปรากฏใน LLM ตามชื่อแบรนด์/สินค้า" คู่กับ SEO traditional ภายในไตรมาสนี้

## 2. Meredith Whittaker (Signal): "AI chatbot ไม่ใช่เพื่อนของคุณ"

**อาจารย์ (มหาวิทยาลัย):** เป็น primary source ที่ดีมากในการสอนวิชา critical AI literacy — ผู้บริหารบริษัท messaging ที่เน้น privacy สุดขั้ว ออกมาพูดตรงๆ ว่าตัวเองไม่ "คุย" กับ chatbot ใช้ประกอบกับ research เรื่อง parasocial bond ที่ผู้ใช้พัฒนากับ AI ได้
**ผู้เชี่ยวชาญด้าน AI:** ประเด็น "backdoor" ที่ Whittaker หยิบมาตรงจุด — agent ที่มี broad permissions บน device/account ของผู้ใช้ก็คือ trojan ที่ถูกอนุญาตล่วงหน้า การออกแบบ permission scope ของ AI agent ใน 12 เดือนข้างหน้าคือสนามรบนโยบายความเป็นส่วนตัวใหญ่กว่ายุค mobile app เยอะ
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมกำลัง build product ที่ใช้ AI assistant ฝังในเวิร์กโฟลว์ผู้ใช้ ต้อง audit permission model ของตัวเองตามมาตรฐาน OAuth scope ขั้นต่ำ — และเปิดให้ user เห็นว่า agent ของคุณ "ทำอะไรในนามของเขา" ไม่งั้นรอบ regulatory ครั้งต่อไป (โดยเฉพาะ EU) จะมาเร็วกว่าที่คิด

## 3. Founders Fund นำ Series A ให้ Shinkei Systems — หุ่นยนต์ AI เชือดปลาด้วย ike jime แบบญี่ปุ่น

**อาจารย์ (มหาวิทยาลัย):** เป็น case study คลาสสิกของ "AI + tradition" — เทคโนโลยี computer vision ทันสมัยมาเสริมเทคนิคโบราณ ike jime ของญี่ปุ่นที่มีมาหลายร้อยปี ทำให้เห็นว่าการ deploy AI ในงานกายภาพ (physical world AI) ต้องมีความเข้าใจ domain ลึก ไม่ใช่แค่โมเดล CV เก่ง
**ผู้เชี่ยวชาญด้าน AI:** น่าสนใจมากในแง่ระบบ — เป็นการ ship edge AI บนเรือ (ไม่มีอินเทอร์เน็ตเสถียร) ที่ต้องทำ inference real-time, ระบุ species จากปลาดิ้น, หา anatomical landmark สำหรับ ike jime ภายในวินาที — งานนี้บังคับให้เลือก specialized model + custom hardware ไม่ใช่ general-purpose API
**โปรแกรมเมอร์มืออาชีพ:** บทเรียน business model สำคัญ — Shinkei ไม่ขายซอฟต์แวร์ ไม่ขายฮาร์ดแวร์ แต่ติดตั้งฟรีและซื้อปลากลับในราคาพรีเมียม (revenue alignment กับ end product) สำหรับนักพัฒนา B2B vertical AI ที่กำลังคิดว่า "ขายเป็น SaaS หรือ license" อาจต้องคิดใหม่ — ถ้า unit economics ลูกค้าปลายทางคุมได้ revenue share/take-rate อาจ scale ดีกว่า subscription fee
