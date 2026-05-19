# Perspectives — 2026-05-19

## 1. ลูกขุนยกฟ้อง Musk vs OpenAI

**อาจารย์ (มหาวิทยาลัย):** เคสนี้ใช้สอน statute of limitations ในวิชา corporate law ได้ตรง ๆ — ศาลไม่ได้ตัดสินว่า "OpenAI ทำผิดหรือเปล่า" เพียงแค่ตัดสินว่า "Musk ฟ้องช้าเกินไป" สองอย่างนี้คนละเรื่องและคนทั่วไปมักสับสน
**ผู้เชี่ยวชาญด้าน AI:** สิ่งที่ผลคดีนี้ปลดออกจริงไม่ใช่ "ความเห็นเชิงจริยธรรม" แต่คือ legal optionality ของฝ่ายที่ต้องการบล็อก for-profit conversion ของ OpenAI — เส้นทาง IPO/restructuring ของ OpenAI เปิดกว้างขึ้นทันที และนั่นกระทบ valuation ของ frontier-lab ทุกเจ้าโดยปริยาย
**โปรแกรมเมอร์มืออาชีพ:** สำหรับคนที่สร้าง product บน OpenAI API — risk ทาง corporate-restructuring ที่ค้างมา 2 ปีถูกลดลงไปหนึ่งชั้น แต่ Musk บอกจะอุทธรณ์อยู่ดี ความเสี่ยงเชิงสัญญา/ความต่อเนื่องของ pricing tier ยังควรอยู่ใน risk register ของทีม

## 2. Google I/O 2026 เปิดวันนี้

**อาจารย์ (มหาวิทยาลัย):** keynote ของ tech vendor เป็น primary source ชั้นดีสำหรับ teaching technology adoption — แต่ต้องระวัง marketing layer; การให้ student เปรียบเทียบ pre-event preview (เช่นชิ้นนี้ของ MIT Tech Review) กับสิ่งที่ประกาศจริงในวันที่ 19 ฝึก critical reading ได้ดีกว่าอ่าน press release ตรง ๆ
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณที่น่าจับตาไม่ใช่ชื่อรุ่น Gemini ใหม่ (จะ 3.x หรือ 4) แต่คือ (1) Gemini Intelligence บน Android ที่ขยายจาก S26/Pixel 10 → ทุก flagship และ (2) Gemma 4 open-weights ที่จะกำหนด open-source baseline ของปลายปี 2026 — สองอย่างหลังเปลี่ยน developer surface area มากกว่า frontier model
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทำงาน Android/Chrome dev ให้ดู AppFunctions API + Gemini Intelligence integration เป็นอันดับแรก — มันคือจุดที่ app ของคุณจะถูก agent ของ Google เรียกโดยตรง อย่ารอประกาศแล้วค่อยรีบ ดู doc ตอน keynote จบทันที

## 3. Anduril × Meta — Smart Glasses สำหรับสมรภูมิรบ

**อาจารย์ (มหาวิทยาลัย):** เคสนี้สอน dual-use technology ได้สมบูรณ์ — บริษัทที่เรารู้จักในฐานะ consumer XR (Meta) จับมือกับ defense prime (Anduril) ทำให้เส้นแบ่งระหว่าง civilian และ military AI ในงาน computer-vision เริ่มลบเลือน คำถามจริยธรรมในวิชา tech-ethics เปลี่ยนจาก "ควร build หรือไม่" เป็น "ใครคุมการใช้งาน"
**ผู้เชี่ยวชาญด้าน AI:** เทคนิคที่ขับ smart glasses ฝั่งทหารคือ on-device perception + low-latency multi-modal model — เป็นโดเมนเดียวที่ Meta มี comparative advantage ทั้ง Llama / SAM stack และ Anduril มี deployment surface; น่าสนใจว่า model ของ Meta จะถูก fine-tune/distill ขนาดไหนเพื่อรันบน optics edge
**โปรแกรมเมอร์มืออาชีพ:** สาย defense-tech เปิดงาน edge inference ระดับ optics สูงขึ้น และ vendor ใหญ่ของ commercial AI กำลังเข้ามาแข่ง — ใครทำ TensorRT, vLLM, edge optimization จะเริ่มเห็นโอกาสที่ pay scale ต่างจาก consumer SaaS ชัดเจน

## 4. Pope Leo XIV — Encyclical แรกเรื่อง AI

**อาจารย์ (มหาวิทยาลัย):** encyclical เป็น "เอกสารระดับสูงสุด" ของศาสนจักรคาทอลิก การที่ Vatican ออกชิ้นนี้ และเชิญ co-founder ของ Anthropic ร่วมเวที สะท้อนว่า AI ethics กำลังเลื่อนจาก academic + tech-policy เข้าสู่ public moral discourse ระดับสถาบันศาสนาแล้ว — น่าใส่ในคอร์ส tech-ethics ปีนี้
**ผู้เชี่ยวชาญด้าน AI:** การเลือก Christopher Olah (interpretability lead เดิมของ Anthropic) ไม่ใช่บังเอิญ — Vatican เลือกเสียงจากฝั่ง "alignment + interpretability" มากกว่าฝั่ง commercial/CEO ซึ่งเป็น framing signal ว่า encyclical น่าจะเอนไปทาง "ทำให้ AI เข้าใจได้และควบคุมได้" มากกว่าทาง "ห้าม"
**โปรแกรมเมอร์มืออาชีพ:** ไม่กระทบเทคนิคโดยตรง แต่เป็น narrative signal สำคัญต่อ buyer-side compliance — องค์กรที่ตอบ regulator/ภาคประชาสังคมเรื่อง AI usage ปีหน้าน่าจะอ้าง encyclical นี้ ทีม policy/legal ของคุณควรอ่านวันที่ 25 พ.ค.

## 5. Huang × Dell — Agentic AI, Memory, China

**อาจารย์ (มหาวิทยาลัย):** การที่ CEO ของ chip designer + system integrator คุยกันบน sideline งาน enterprise เป็น primary source สำหรับ "current bottleneck ของ AI infrastructure" — ปีนี้ keyword คือ memory bandwidth และ China access ไม่ใช่ FLOPS อย่างที่ตำราเขียนไว้ 2 ปีก่อน
**ผู้เชี่ยวชาญด้าน AI:** ที่ Huang บอกว่าตลาด AI semiconductor จีน "จะถูกเปิด" เป็น corporate diplomacy ไม่ใช่ technical forecast — แต่ถ้าเกิดจริงจะเปลี่ยน supply-demand ของ HBM และ training capacity ทั่วโลก เพราะ demand ฝั่งจีนถูก suppress มา 3 ปี
**โปรแกรมเมอร์มืออาชีพ:** สอง take-away: (1) ดีไซน์ inference stack ให้ memory-bandwidth-aware ไม่ใช่ compute-aware อย่างเดียว — quantization + KV-cache compression + speculative decoding กลับมามีค่ามาก (2) ถ้าทำงานกับ vendor จีน (ByteDance, Alibaba Cloud, MoonShot) จับตา policy ของ US ปลายปี — supply chain อาจปลดล็อก
