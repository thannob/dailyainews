# Perspectives — 2026-06-10

## 1. Anthropic เปิดตัว Claude Fable 5 (Mythos-class) ให้ใช้สาธารณะ

**อาจารย์ (มหาวิทยาลัย):** เป็นเคสสดของ "tiered access AI safety" — model ตัวเดียวกันถูกแบ่ง surface ตามความเสี่ยง (Fable = public; Mythos = approved partners) และในตัว Fable เองยังมี **internal fallback** ไป Opus 4.8 เมื่อเข้า cybersecurity / biology / chemistry / distillation; ใช้สอนนักศึกษา AI policy ว่า safety boundary ไม่จำเป็นต้องเป็น "ปล่อย" หรือ "ไม่ปล่อย" — มี layer ระหว่างได้
**ผู้เชี่ยวชาญด้าน AI:** ราคา $10/M input + $50/M output คือ 2× ของ Opus 4.8 — Anthropic ตีราคา frontier capability ที่ premium ชัดเจน; ตัวเลข "≥95% sessions วิ่งบน Fable เอง" หมายความว่า fallback ไป Opus 4.8 เกิดน้อย — แต่ Mythos 5 ที่เปิดให้พาร์ตเนอร์ Glasswing (รวม Apple) คือสัญญาณว่า frontier model สำหรับลูกค้า enterprise ระดับสูง ยัง gate ไว้แน่นกว่า
**โปรแกรมเมอร์มืออาชีพ:** snippet เน้นว่า Fable 5 "excels at software engineering" — ทีมที่ใช้ Claude ใน coding agent / IDE assistant ต้อง benchmark Fable 5 vs. Opus 4.8 vs. Sonnet 4.6 ก่อน **22 มิ.ย.** (วันสุดท้ายที่ Fable ฟรีในแพ็กเกจ Pro/Max/Team/Enterprise); หลัง 23 มิ.ย. ต้องซื้อ credits — เปลี่ยน unit economics ของ coding workflow ที่เคย "เปิดยิงไม่อั้น"

## 2. OpenAI launches Economic Research Exchange

**อาจารย์ (มหาวิทยาลัย):** เป็น template ใหม่ของ industry-academia collaboration ในยุค AI — vendor ปล่อย privacy-protected access ให้นักวิจัยตอบคำถามเศรษฐศาสตร์ที่ vendor ตอบเองไม่น่าเชื่อ; เคสนี้เปิดบทอ่านวิจัย labor economics + AI สำหรับนักศึกษา econ / public policy — และตั้งคำถามว่าใครเป็นผู้กำหนด research agenda เมื่อ data ทั้งหมดผ่าน gatekeeper เดียว
**ผู้เชี่ยวชาญด้าน AI:** การเปิด structured project-based exchange ต่อยอดจาก OpenAI Signals แสดงว่า OpenAI เริ่มลงทุนใน **measurement layer** ของผลกระทบจริง ไม่ใช่แค่ capability benchmark — สำคัญสำหรับการ defend policy position ต่อรัฐบาล/regulator; แต่ระวัง selection bias: นักวิจัยที่ถูกเลือกย่อม optimistic ต่อ AI มากกว่าค่าเฉลี่ย
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมงานมี data scientist / economist ที่สนใจ AI labor impact — deadline สมัคร **5 ก.ค. 2026** เป็นช่องเข้าถึง privacy-protected OpenAI tools ที่ปกติไม่เปิดให้นอกองค์กร; ส่วนคนที่ทำ HR analytics ใน enterprise ควรจับตา publication ของ Exchange เพราะจะเป็น primary data ที่ใช้ defense กับ board ในการ headcount planning ปีหน้า

## 3. Sandstone ปิด $30M Series A — Legal AI สำหรับ in-house

**อาจารย์ (มหาวิทยาลัย):** เคสที่สอนการเลือก niche ในตลาดอิ่มตัว — legal AI มีผู้เล่นใหญ่ในฝั่ง law firm (Harvey, Spellbook, etc.) แต่ในฝั่ง **in-house legal team** ขององค์กรกลับยัง underserved; ใช้สอนนักศึกษา MBA / strategy ว่า "tangle of overlapping tasks" ก็เป็น moat ได้ถ้าเข้าใจ workflow จริง ไม่ใช่ทำซ้ำ law-firm UX
**ผู้เชี่ยวชาญด้าน AI:** Series A $30M สำหรับ vertical-specific agent ที่จับ workflow เฉพาะกลุ่ม (contract review + compliance + policy) เป็น signal ว่า VC เริ่มเชื่อใน **vertical agent thesis** มากกว่า horizontal copilot — แต่ moat จริงจะอยู่ที่ integration กับ contract repository / CLM / policy database ของลูกค้า ไม่ใช่ LLM ที่ใช้
**โปรแกรมเมอร์มืออาชีพ:** ทีม engineer ที่ทำ enterprise SaaS — ดูเคสนี้แล้วเช็คว่า in-house function ของลูกค้าตัวเอง (legal / procurement / compliance / risk) มีจุดที่ workflow แตกระหว่าง 3-5 tool หรือไม่; ถ้ามี — นั่นคือ wedge ที่ LLM agent เข้าไปแทรกได้ และคู่แข่ง 2 ปีข้างหน้ายังไม่ทันสร้าง

## 4. GM กระโดดเข้าตลาด battery สำหรับ AI data center + grid

**อาจารย์ (มหาวิทยาลัย):** เคสน่าสนใจของ **capability adjacency** — automaker ที่สะสมเทคโนโลยี battery จากธุรกิจ EV หันมาขายเข้าตลาดใหม่ที่ demand แทบไม่จำกัด (AI data center + grid); ใช้สอน corporate strategy ว่า EV slowdown ที่ปะทะตลาดอยู่ตอนนี้ ไม่จำเป็นต้องเป็นจุดจบของ capex battery — ถ้ามี adjacent market ที่หิวกว่า
**ผู้เชี่ยวชาญด้าน AI:** AI training cluster ระดับ multi-gigawatt + inference fleet ทั่วประเทศ กำลังทำให้ **grid-scale storage** กลายเป็น constraint ที่หนักกว่า chip supply ในบางพื้นที่ — เพราะ data center peak load ไม่ matched กับ generation profile (โดยเฉพาะ renewable-heavy grid); GM เข้ามาในจังหวะที่ NVIDIA + hyperscaler หา energy partner เร่งด่วน
**โปรแกรมเมอร์มืออาชีพ:** ไม่ใช่ข่าวที่กระทบ daily coding workflow โดยตรง แต่กระทบ unit economics ของ inference indirectly — ถ้า energy storage cost ลงในอีก 12-24 เดือน, hyperscaler จะ pass-through ราคา inference ที่ถูกลง; ทีมที่ทำ cost forecasting สำหรับ LLM-heavy product ใน 2027-2028 ควร flag GM-class entrant เป็น variable ที่อาจ shift baseline

## 5. TechCrunch: อุตสาหกรรม AI กำลังเริ่มทดสอบสมมติฐาน "bigger = better"

**อาจารย์ (มหาวิทยาลัย):** เคสคลาสสิกของ paradigm shift ใน technology economics — สมมติฐาน "scale wins" ที่ครองยุคของ frontier model 2022-2025 กำลังถูกท้าทาย; ใช้สอน history of technology — เปรียบกับยุค "bigger CPU clock = better" ที่จบลงเมื่อ multi-core มา และยุค "more transistors per die" ที่จบลงเมื่อ chiplet มา
**ผู้เชี่ยวชาญด้าน AI:** snippet ไม่ได้บอกว่าใคร / โมเดลไหนเป็นหลักฐานว่าสมมติฐานแตก — แต่บริบทตลาดสนับสนุน: DeepSeek-class open model, Microsoft MAI family, distilled domain model — ทั้งหมดชี้ว่า "right-sized model + good data + good post-training" อาจดีกว่า "bigger" ในหลาย use case; การที่ Anthropic ตั้งราคา Fable 5 ที่ 2× Opus 4.8 ก็คือคนละ direction กับ trend ที่ TechCrunch กำลังพูดถึง
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่จ่ายค่า inference เดือนละ 5 หลัก USD+ ควรเริ่ม PoC routing layer — ส่ง easy / structured query ไป small model (Haiku 4.5 / GPT-4o-mini / open-source 7B-14B class) แล้วเก็บ frontier model ไว้ใช้ตอน edge case จริง; ROI ของ effort นี้สูงขึ้นทุกไตรมาส เพราะ small model เก่งขึ้นเร็วกว่า big model
