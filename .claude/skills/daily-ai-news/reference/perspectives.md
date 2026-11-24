# Perspectives — 2026-11-24

## 1. NVIDIA คืนตำแหน่งซีอีโอให้ Jensen Huang หลังบอร์ดลงมติเอกฉันท์

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็นตัวอย่างสดของเรื่องที่สอนในคลาส Corporate Governance — บริษัทที่มี founder-led culture กับบอร์ดที่พึ่งพาผู้ก่อตั้งมากจะต้องสมดุล "risk จากตัวบุคคล" กับ "มูลค่าที่ผู้ก่อตั้งสร้างให้องค์กร" อย่างไร นักเรียนควรเทียบกับเคสของ Steve Jobs ที่ Apple และดูว่าเงื่อนไขการกลับมา (ต้องร่วมมือกับคณะกรรมการอิสระ, มีการหารือกับรัฐบาลสหรัฐ) ต่างจากกรณี Apple อย่างไร
**ผู้เชี่ยวชาญด้าน AI:** สิ่งสำคัญไม่ใช่ตัว Huang แต่คือสัญญาณว่าความเสี่ยงด้าน geopolitics (chip export control, การสอบสวนคนในบริษัทที่อาจถูกใช้เป็นสายลับ) กลายเป็นปัจจัยหลักของ AI supply chain ไปแล้ว ความมั่นคงของ Nvidia สำคัญกับทุก lab เพราะเกือบทุกโมเดลใหม่ยังต้องการ H100/B200 ในการ train
**โปรแกรมเมอร์มืออาชีพ:** ผลต่อ day-to-day คือลด uncertainty เรื่อง roadmap ของ CUDA และ driver — ถ้าซีอีโอเปลี่ยน ทีมในบริษัทอาจชะลอการประกาศเครื่องมือใหม่ การกลับมาของ Huang น่าจะทำให้จังหวะ release ของ cuDNN, Triton, TensorRT กลับไปเร็วเหมือนเดิมภายในไม่กี่ไตรมาส

## 2. Anthropic เปิดตัว Claude Ship — AI agent ที่รีวิว, แก้, และ approve PR ได้

**อาจารย์ (มหาวิทยาลัย):** น่าสนใจที่จะใช้สอน Software Engineering ว่า code review ซึ่งเคยถูกถือเป็น "social activity" ของทีมเริ่มถูก automate แล้ว นักเรียนควรทดลองเทียบ feedback ของ Claude Ship กับของเพื่อนในทีม และวิเคราะห์ว่ามิติไหนที่ agent ยังแทนไม่ได้ (เช่น การเข้าใจ constraint ทางธุรกิจที่ไม่อยู่ใน spec)
**ผู้เชี่ยวชาญด้าน AI:** Claude Ship ประกอบด้วยสามส่วน — Code Review (GA), PR Steward (beta), Claude Approvals (beta) — ความสำคัญอยู่ที่ "Approvals" เพราะหมายถึง agent มีสิทธิ์ merge code ได้จริงในขอบเขตที่กำหนด นี่คือ step สำคัญจาก "advisory agent" ไปสู่ "agent with authority" ต้องจับตา policy layer ว่าทีมจะกำหนดขอบเขตได้ปลอดภัยแค่ไหน
**โปรแกรมเมอร์มืออาชีพ:** สำหรับทีมที่ใช้ GitHub + Claude Team/Enterprise อยู่แล้ว ลองเปิด Code Review ก่อนเพราะเป็น GA และ risk ต่ำ ส่วน Approvals ควรเริ่มจาก repo ที่มี CI ครบ test coverage สูง และกำหนด path allowlist ก่อน อย่าให้ agent approve PR ที่แตะ migrations หรือไฟล์ security

## 3. Amazon ซื้อ Decart 7.5B — เร่งขาย Trainium ชนกับ Nvidia

**อาจารย์ (มหาวิทยาลัย):** ดีลนี้สอน "vertical integration" ชัดเจน — AWS ไม่ได้ซื้อ Decart เพราะอยากได้โมเดล แต่ได้ optimization stack ที่ทำให้ Trainium ใช้คุ้มขึ้น การซื้อทีมและเทคโนโลยีควบ 7.5 พันล้านเหรียญ คือ bet ว่าการแข่งขันระดับ hyperscaler ตัดสินกันที่ compute efficiency ไม่ใช่โมเดลที่ดีที่สุด
**ผู้เชี่ยวชาญด้าน AI:** จุดที่ต้องจับตาคือ Decart มีงาน distillation และ sparsity ที่ช่วยลดต้นทุน inference ลงได้มาก ถ้า Amazon เอามา bake เข้า Trainium 2/3 ได้ ก็เป็นครั้งแรกที่มี realistic alternative ต่อ CUDA ecosystem ในระดับ production — ไม่ใช่แค่ benchmark แต่ TCO
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีม inference อยู่บน AWS อยู่แล้ว ปีหน้าควร monitor Neuron SDK updates ให้ใกล้ชิด — ถ้า Decart stack ลง Trainium ได้จริง การ port workload จาก A100/H100 มา Trainium อาจประหยัด 30-50% โดยไม่ต้อง re-architect หนัก คุ้มที่จะ budget evaluation sprint ไว้ล่วงหน้า

## 4. OpenAI เสนอ perplexity เป็นมาตรวัดกลางของ AI progress

**อาจารย์ (มหาวิทยาลัย):** น่าสอนเพราะมันคือการยอมรับกลาย ๆ ว่า benchmark ที่ใช้กันอยู่ (MMLU, HumanEval, ARC) กำลัง saturate หรือถูก train-on-test จนไม่สะท้อนความสามารถจริง perplexity เป็น metric เก่าแก่ที่ทุกคนรู้จักแต่ใช้เปรียบเทียบข้าม lab ได้ยาก — ประเด็นที่ควรให้นักเรียนถกคือ "ทำไมสาขานี้ถึงต้องกลับไปใช้ของเก่า"
**ผู้เชี่ยวชาญด้าน AI:** ปัญหาคือ perplexity ขึ้นกับ reference model และ tokenizer อย่างมาก การเปรียบเทียบข้ามโมเดลที่ใช้ tokenizer ต่างกันแทบไม่มีความหมาย นอกจากนี้ perplexity ไม่ได้ correlate กับ downstream task performance เสมอ ข้อเสนอนี้จึงมีค่าในฐานะ "guard rail กันการ overclaim ว่า saturate benchmark แล้ว" มากกว่าในฐานะมาตรวัดเดี่ยว
**โปรแกรมเมอร์มืออาชีพ:** สำหรับ practitioner ที่ต้องเลือกโมเดลให้ทีม อย่าเพิ่งเปลี่ยนไปใช้ perplexity เป็นเกณฑ์หลัก ยังคงควรวัดด้วย task-specific eval ที่ทีมสร้างเอง (golden set + LLM-as-judge) — perplexity ช่วยในการ sanity-check ว่าโมเดลใหม่ไม่ได้ regress เรื่องพื้นฐาน แต่ไม่ควรใช้ตัดสิน production decision

## 5. Megaspeed เตรียมถูกใส่ blacklist สหรัฐ — บทต่อของดราม่า Huang / Nvidia

**อาจารย์ (มหาวิทยาลัย):** กรณีศึกษา export control ที่สดที่สุดในตอนนี้ นักเรียนสายกฎหมาย/นโยบายควรวิเคราะห์ว่า Entity List ของ Commerce Department ต่างจาก SDN List ของ Treasury อย่างไร และผลต่อ downstream supply chain (บริษัทที่ค้าขายกับ Megaspeed ทางอ้อม) จะเป็นอย่างไร
**ผู้เชี่ยวชาญด้าน AI:** Megaspeed ถูกกล่าวหาว่าทำหน้าที่ reseller ส่ง H-series chip ไปจีน การใส่ blacklist สะท้อนว่า US government กำลังเปลี่ยนโหมดจาก "ควบคุมที่ผู้ผลิต" (Nvidia) ไปสู่ "ควบคุมที่ reseller channel" — รวมถึง data center ในสิงคโปร์/มาเลเซีย/ไทย/อินโดนีเซีย/บราซิลด้วย ที่น่าจับตาคือ Thailand อยู่ในลิสต์
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมใช้ compute capacity ที่เช่าจาก provider ในภูมิภาคเอเชียตะวันออกเฉียงใต้ ปีหน้าอาจต้องรับมือ compliance paperwork เพิ่มขึ้น (end-use certification, re-export license) ควรถาม provider ว่าชิปอยู่ภายใต้การควบคุม category ไหน และ workload ประเภทไหนที่อาจถูก restrict ก่อนเริ่ม project ใหม่
