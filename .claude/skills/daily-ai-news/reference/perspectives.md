# Perspectives — 2026-07-24

## 1. Microsoft ถอด OpenAI image models ออกจาก PowerPoint/Bing แทนด้วย MAI-Image-2.5-Pro

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เป็นวัสดุคลาส strategy ที่ชัดว่า "vertical integration" กลับมาสำคัญเมื่อ dependency ทาง infrastructure กลายเป็น cost line ระดับพันล้าน — Microsoft ไม่ได้เลิก partnership กับ OpenAI แต่กำลังลด single-vendor dependency ก่อน renegotiation รอบใหม่.
**ผู้เชี่ยวชาญด้าน AI:** ตัวเลข GPU cost ลด 84% เทียบ GPT-Image-2 คือ signal ว่า Microsoft optimize architecture เพื่อ workload เฉพาะ (image, retention-focused) แทนที่จะพึ่ง general-purpose model — ทิศทางนี้บอกว่า inference cost curve จะแยกย่อยเป็น task-specific model economy ในอีก 12 เดือน.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณเรียก image-generation endpoint ผ่าน Microsoft Graph, Copilot, หรือ Bing API อยู่ ต้องคาดว่า output distribution จะเปลี่ยน — เตรียม regression suite สำหรับ image tasks และตรวจ prompt-response contract ก่อนที่ MAI-Image-2.5-Pro จะ roll out เต็มระบบ.

## 2. สหรัฐฯ กล่าวหา Moonshot ใช้ Claude Fable กลั่นเป็น Kimi K3 — ฝึกด้วยชิป GB300 ในไทย

**อาจารย์ (มหาวิทยาลัย):** ประเด็นนี้เปิดคลาส AI policy ได้ทั้งเทอม — ต้องแยก 3 layer ให้ชัด: (1) allegation จากฝ่ายบริหารสหรัฐฯ (2) หลักฐานที่ยัง unshared และ (3) technical reality ที่ผู้เชี่ยวชาญหลายคนบอกว่า distillation อธิบายไม่ได้ทั้งหมด; วัสดุ debate ที่ดีคือ "การกล่าวหาโดยไม่เปิดหลักฐานถือเป็น policy tool ที่ชอบธรรมหรือไม่".
**ผู้เชี่ยวชาญด้าน AI:** distillation จาก closed-source model ทำได้จริงในทางเทคนิค แต่ผู้ที่เข้าใจ post-training pipeline รู้ว่าการไปถึง frontier-tier ต้องมี data curation + RL infrastructure + eval loop ที่ซับซ้อน ไม่ใช่แค่ query API เอา output; ประเด็นน่าจับตากว่า distillation เอง คือการอ้าง GB300 อยู่ในไทย — export-control regime ตอนนี้พึ่ง end-user certification ที่ตรวจสอบยาก.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าองค์กรคุณใช้ Kimi K3 / Moonshot models บน production workflow — เตรียม contingency plan: (1) abstraction layer ที่ swap ไป Qwen/GLM/US API ได้ในไม่กี่ชั่วโมง (2) audit ว่ามี data ที่ส่งผ่านโมเดลจีนแล้วมี risk regulatory/contractual (3) ถ้าอยู่ในไทยและใช้ compute infrastructure จาก vendor ที่ไม่โปร่งใส คาดว่ามี regulatory scrutiny เพิ่มในไตรมาสหน้า.

## 3. Etched ระดม $300M รอบ Series C ที่มูลค่า $10.3B — ท้าทาย NVIDIA ในตลาด inference

**อาจารย์ (มหาวิทยาลัย):** เคสนี้พาเข้าคลาส hardware economics — เทียบราคาต่อ token ที่ ASIC เฉพาะ transformer ทำได้ vs general-purpose GPU; วัสดุที่ดีคือให้นักเรียนคำนวณ break-even ระหว่าง capex ASIC กับ opex GPU cloud ที่ throughput เท่ากัน แล้ว debate ว่า vertical-integrator (hyperscaler) จะบุก ASIC เอง หรือปล่อยให้ specialist ทำ.
**ผู้เชี่ยวชาญด้าน AI:** $1B orders booked ก่อน mass production คือ signal ว่า enterprise inference demand ล้น GPU supply จริง — differentiation ของ Etched คือ Sohu chip ที่ hard-wire transformer architecture, ให้ throughput สูงกว่า GPU 10x ในโจทย์เฉพาะ; ความเสี่ยงคือถ้า architecture รุ่นถัดไปเปลี่ยน (เช่น hybrid state-space model หรือ MoE ที่ต้อง flexibility มากขึ้น) hardware ที่ specialize ไปแล้วจะ obsolete เร็ว.
**โปรแกรมเมอร์มืออาชีพ:** ในระยะสั้น (12 เดือน) ไม่ต้อง port workload — Etched ยังไม่ open ให้ทั่วไปเข้าถึง; แต่ควรออกแบบ inference layer ให้ backend-agnostic (vLLM, TGI, หรือ abstraction ผ่าน LiteLLM/OpenRouter) เพราะปี 2027 น่าจะได้เห็น inference provider หลายรายเสนอ Sohu-backed endpoint ราคาถูกกว่า NVIDIA-hosted อย่างมีนัย.

## 4. Runway เปิด Media Router — API ที่ auto-select โมเดล image/video/audio ตาม priority

**อาจารย์ (มหาวิทยาลัย):** Media Router เป็นเคสสอน platform strategy — Runway เลิกแข่งเป็น model provider เดี่ยว แล้วขยับไปเป็น aggregator/router; นี่คือ playbook เดียวกับ OpenRouter หรือ LiteLLM ที่นำมาใช้กับ generative media แทน text; วัสดุคลาส digital business ที่น่า debate: aggregator layer จะ commoditize model provider หรือกลายเป็น middleman ที่ margin หด.
**ผู้เชี่ยวชาญด้าน AI:** technical hard problem ของ media router คือ (1) benchmark cross-model quality อย่างเป็นระบบเพราะ output subjective — ต้องมี latent-space similarity metric + human eval loop (2) latency budget ต่างกันหลายเท่าระหว่างโมเดล ทำให้ routing policy ต้อง real-time-aware; ถ้าทำได้ดี Runway มี moat ที่ไม่ใช่โมเดลเอง แต่คือ routing logic + evaluation infra.
**โปรแกรมเมอร์มืออาชีพ:** ทีมที่สร้าง creative tools หรือ marketing automation — Media Router ลด vendor-lock-in ได้จริง คุ้มที่จะทดลอง; แต่ตรวจ pricing structure ให้ดี เพราะ router layer ใส่ margin เพิ่ม (ปกติ 10–20%); ทางเลือกคือ implement routing เองด้วย spec เดิมของ vendor แต่ละราย ถ้า volume มากพอที่ตัด middleman จะคุ้มกว่า.

## 5. Magnificent 7 หายไป $797B ในวันเดียว — biggest one-day drop ตั้งแต่ เม.ย. 2025

**อาจารย์ (มหาวิทยาลัย):** เคสนี้พาเข้าคลาส market psychology ที่แข็งแรง — เทียบ narrative "AI capex race" ของสัปดาห์ที่แล้ว (Alphabet ขึ้น guidance) กับ reaction "AI skeptics dumping" ในวันเดียวกัน; ให้นักเรียนวิเคราะห์ว่า market price อยู่ในระยะ "believe-and-buy" หรือ "prove-it-first" และเมื่อไหร่ investor จะเริ่มต้องการเห็น ROI ที่วัดเป็นตัวเลข.
**ผู้เชี่ยวชาญด้าน AI:** stock reaction ไม่ใช่ signal เชิงเทคนิคของ AI capability แต่คือ signal ว่า "cost curve หน้าตาไม่ค่อยดี" — infrastructure spend ก่อน revenue ที่ชัด; ประเด็นเชิงเทคนิคที่ตลาด priced-in ยังไม่ครบ คือถ้า inference cost ยังลงเดือนละ 30–50% เหมือน 12 เดือนที่ผ่านมา revenue-per-token ก็จะโดนกดตามไปด้วย ทำให้ payback period ที่ investor คำนวณอยู่ตอนนี้อาจสั้นเกินจริง.
**โปรแกรมเมอร์มืออาชีพ:** ในทางปฏิบัติสำหรับ engineer ไม่มีอะไรเปลี่ยนวันนี้ แต่ระวัง 2 อย่าง: (1) ถ้า startup ที่คุณอยู่ pitch VC ในไตรมาสนี้ term sheet จะแข็งขึ้น ต้อง prove unit economics ชัดกว่า 6 เดือนก่อน (2) ถ้าอยู่บริษัทใหญ่ที่พึ่ง reserved GPU capacity — ใช้ moment ตลาดกลัวเพื่อ renegotiate discount กับ cloud vendor เพราะ pipeline capacity ปีหน้าอาจถูกกดดันให้ระบาย.
