# Perspectives — 2026-05-27

## 1. DuckDuckGo installs +30% as users reject Google's AI Search

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้คือ live experiment ของ Hirschman's *Exit, Voice, and Loyalty* — ผู้ใช้ที่ไม่ชอบ AI Search ของ Google ไม่ออกมา voice ในแบบสอบถาม แต่ exit ด้วยเท้า (install คู่แข่ง) ซึ่งวัดผลได้แน่นกว่ามาก น่าหยิบไปสอนวิชา product strategy / consumer behavior ว่าเหตุใด default-on AI feature จึงเสี่ยงต่อ brand เมื่อไม่มี opt-out
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข noai.duckduckgo.com +22.7% WoW น่าสนใจกว่าตัวเลขรวม — มันบอกว่าผู้ใช้กลุ่มหนึ่งต้องการ search ที่ "ปิด AI by default" ไม่ใช่แค่เปลี่ยน vendor นี่คือ market signal ว่ามี non-trivial segment ที่ AI summarization ทำให้คุณภาพการค้นหาแย่ลงสำหรับงานของเขา (เช่น verification, primary-source hunting)
**โปรแกรมเมอร์มืออาชีพ:** ผู้พัฒนาที่พึ่ง organic search ในการกระจาย docs/blog content ควรเฝ้าดู referral traffic จาก Google ใน 30 วันข้างหน้า — AI agents ของ Google I/O 2026 อาจตอบคำถามจาก content ของคุณโดยไม่ส่ง click กลับมา ถ้าเห็น drop เกิน 20% ต้อง diversify ช่องทาง (newsletter, Hacker News, DuckDuckGo SEO, RSS) ตั้งแต่ตอนนี้

## 2. Human Archive — India's gig economy training the world's robots

**อาจารย์ (มหาวิทยาลัย):** ตำแหน่งของ Human Archive อยู่ใน geography of AI labor ที่ Mary L. Gray เรียกว่า *ghost work* — งานที่ทำให้ AI ทำงานได้ แต่ถูกซ่อนจากผู้ใช้ปลายทาง น่าใช้เป็น case study คู่กับ Scale AI/Sama เพื่อสอนว่า supply chain ของ frontier AI ไม่ใช่แค่ compute และ data center แต่รวมถึงแรงงานในประเทศกำลังพัฒนา และตั้งคำถามเรื่องการกระจายผลตอบแทน
**ผู้เชี่ยวชาญด้าน AI:** จุดเทคนิคที่น่าสนใจคือการ synchronize headset RGB-D + force feedback + full-body mocap + chest/wrist video พร้อมกัน — modality alignment ใน physical AI เป็น bottleneck จริง การมี dataset multi-modal sync ขนาดใหญ่จาก scenarios ที่ฝึกในแล็บไม่ได้ (เช่น แม่บ้าน, คนทำอาหาร, ช่างซ่อม) จะเป็น input ที่ humanoid foundation models ใช้งานได้จริง คำถามที่ยังไม่มีคำตอบคือ data licensing — บริษัทใดเป็นเจ้าของหลังจากนำไปเทรน
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำงานสาย robotics / embodied AI ตัวเลขนี้บอกว่า real-world data ราคา ~$15/ชม. ในอินเดียถูกกว่าหลายเท่าเทียบกับ synthetic data ระดับเดียวกัน — แต่ก็เป็นสัญญาณว่ายุค "synthetic everything" ของ frontier robotics กำลังจบ และ pipeline ที่ผสม real + sim จะกลายเป็นมาตรฐาน ใครออกแบบ data infra อยู่ ควรเริ่มคิดเรื่อง ingestion ของ multi-sensor real-world stream ตั้งแต่ตอนนี้

## 3. UMG–TikTok renew, with AI music protections at the center

**อาจารย์ (มหาวิทยาลัย):** ปี 2024 UMG ดึงเพลงทั้งหมดออกจาก TikTok ในข้อพิพาทเรื่อง royalty + AI; ปี 2026 กลับมา renew พร้อมเงื่อนไข AI ที่ชัด — นี่คือ pattern คลาสสิกของ collective bargaining ในอุตสาหกรรมความรู้: ฝ่ายเจ้าของ IP ใช้การ "ถอนของ" เป็น leverage จนแพลตฟอร์มยอมเจรจาเงื่อนไขใหม่ น่าเทียบกับการเจรจา WGA-AMPTP เรื่อง AI ใน Hollywood
**ผู้เชี่ยวชาญด้าน AI:** ดีลนี้ทำให้ AI music กลายเป็น *licensing problem* แทน *litigation problem* — ซึ่งสำคัญเพราะ litigation ต้องการนิยาม "training infringes" ที่ศาลยังไม่ตกลงกัน ส่วน licensing ทำงานได้ทันทีถ้าทั้งสองฝ่ายตกลงนิยาม "unauthorized AI music" และเครื่องมือ detection — งาน detection ที่ TikTok ต้อง implement คือ MIR (music information retrieval) ขนาดใหญ่ มี false-positive risk สำหรับศิลปินที่ใช้ AI tool legitimately
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้าง AI music tools (Suno, Udio, open-source models) ต้องเตรียม artist-attribution metadata และ provenance signature ตั้งแต่ขั้น generation — เพราะแพลตฟอร์มใหญ่อย่าง TikTok จะเริ่มใช้ provenance check เป็นเงื่อนไข upload ถ้าไม่ฝัง watermark/metadata มาตั้งแต่ต้น content ของผู้ใช้จะถูก takedown แบบไม่มีคำเตือน
