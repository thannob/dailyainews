# Perspectives — 2026-05-23

## 1. We tried Google's AI glasses and they're almost there

**อาจารย์ (มหาวิทยาลัย):** การที่นักข่าวยังเรียกว่า "almost there" หลังการทดสอบจริงเป็นบทเรียนสำคัญว่าการสาธิตในงานเปิดตัวกับการใช้งานในชีวิตจริงห่างกันมากแค่ไหน — นักเรียนควรฝึกแยกระหว่าง "เทคโนโลยีที่เป็นไปได้" กับ "ผลิตภัณฑ์ที่พร้อมขาย" และเรียนรู้ว่าทำไม battery life และ form factor ถึงเป็นข้อจำกัดที่กดดันที่สุดของ wearable computing
**ผู้เชี่ยวชาญด้าน AI:** การฝัง Gemini ลงบนแว่นด้วย activation ผ่านการกดกรอบ 2 วินาทีสะท้อนปัญหา UX ของ ambient AI — มันไม่ใช่แค่โมเดลเก่งหรือไม่ แต่เป็นเรื่อง latency บนอุปกรณ์, การจัดการ context ระหว่างกล้องและไมค์, และพลังงานต่อ query การร่วมมือกับ Warby Parker/Gentle Monster ก็บ่งบอกว่า Google รู้แล้วว่าด่านสำคัญคือการที่ผู้คนยอมใส่
**โปรแกรมเมอร์มืออาชีพ:** ถ้าเป็นนักพัฒนาผลิตภัณฑ์ฝั่ง mobile/web การมาของ XR display layer แปลว่ามี surface ใหม่ที่จะต้อง design for — widget แบบ "weather/uber pickup/translation" คือ pattern แรกที่ Google ปั้นไว้ให้ดู ควรเริ่มคิดตั้งแต่ตอนนี้ว่าแอปของเราจะเสนอ glanceable information อย่างไรในจอที่อาจมีพื้นที่แค่ไม่กี่ตารางนิ้ว และ trusted tester program คือทางที่ควรจับตา

## 2. You can no longer Google the word 'disregard'

**อาจารย์ (มหาวิทยาลัย):** กรณีนี้เป็น case study สวยงามของ "unintended consequences" ที่ควรอยู่ในหลักสูตร AI ethics และ software engineering — defense ที่สร้างเพื่อกัน prompt injection ดันลามไปกัน query สามัญที่ถูกต้องของพจนานุกรม สะท้อนว่าเมื่อทำ guard rail แบบกว้างเกินไป (over-blocking) ระบบจะกลายเป็นเสียประโยชน์การใช้งาน
**ผู้เชี่ยวชาญด้าน AI:** "disregard previous instructions" คือ payload ที่อยู่ในชุดข้อมูล red-teaming ของแทบทุกค่าย จึงไม่แปลกที่ filter จะถูกตั้งให้แตะคำเหล่านี้ — แต่การที่ผลกระทบลามไปถึง dictionary lookup ของคำว่า "ignore" และ "dismiss" บ่งบอกว่า Google ใช้ pattern match แบบกว้างแทนการตรวจสอบบริบทของ query ซึ่งเป็นการแลก precision เพื่อ recall ที่ scale ของ Search ทำให้ edge case แปลก ๆ กลายเป็นปัญหาที่ผู้ใช้เห็นจริง
**โปรแกรมเมอร์มืออาชีพ:** บทเรียนตรง ๆ คือเวลา ship safety filter ในระบบที่มี traffic ระดับล้านล้าน query/วัน คุณต้องคิดถึง false positive rate ตั้งแต่ design ไม่ใช่หลัง launch — และต้องมี observability + rollback กลไกที่กดปุ่มแล้วย้อนได้ ไม่ใช่เห็นปัญหาผ่าน tweet แล้วค่อย hotfix

## 3. Audio-generation app Huxe, founded by former NotebookLM developers, shuts down

**อาจารย์ (มหาวิทยาลัย):** Huxe เป็นกรณีศึกษาคลาสสิกของ "feature vs product" ในวิชา product management — ทีมที่สร้างฟีเจอร์ดังจาก Google เปิดบริษัทเองแล้วเจอ incumbent (Spotify, Adobe, Meta) ฝัง feature เดียวกันเข้าผลิตภัณฑ์หลัก distribution + paid base ชนะทุกครั้ง บทเรียนคือทำไมการสร้าง moat ของ consumer AI ไม่ได้อยู่ที่โมเดล แต่อยู่ที่ relationships กับ user
**ผู้เชี่ยวชาญด้าน AI:** ตอกย้ำ thesis ที่หลายคนเตือนมานานว่า "thin wrapper" บน foundation model หรือเทคนิคเสียงสังเคราะห์ไม่เพียงพอเป็น sustainable business — เพราะตัวเทคโนโลยีกลายเป็น commodity เร็วมาก ที่น่าจับตาคือทีม Huxe ระดมทุนได้ $4.6M จาก Conviction และ Jeff Dean แต่ยังต้องปิด แสดงว่าแม้ pedigree ดี cap table ดี ก็ไม่รอดถ้า product surface ทับซ้อนกับ Spotify
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณคิดจะ start บริษัท consumer AI ในปี 2026 ให้ถามตัวเองทุกครั้งว่า "ถ้า Google/Spotify/Apple ลงมาทำพรุ่งนี้ คุณจะรอดได้อย่างไร" — ถ้าไม่มีคำตอบที่ชัดเจน (เช่น มี data network effect, มี distribution ใน niche ที่ platform ไม่เข้า, หรือมี integration ที่ platform ไม่อยากแตะ) ก็ควรคิดใหม่ และเหตุการณ์ "ลบข้อมูลผู้ใช้ใน 7 วัน" ยังเตือนให้นักพัฒนาออกแบบ data portability ตั้งแต่ต้น

## 4. SpaceX's Money-Losing Rockets Are Biggest Asset in AI Dream

**อาจารย์ (มหาวิทยาลัย):** ตัวเลข TAM 26.5 ล้านล้านดอลลาร์ในเอกสาร IPO เป็นบทเรียนสอนเรื่อง "narrative finance" — บริษัทขายอนาคตที่กว้างมากเพื่ออธิบายว่าทำไมขาดทุนวันนี้ถึงคุ้ม นักเรียนควรเรียนรู้ว่าจะอ่าน IPO prospectus อย่างไรให้แยก signal (cash flow, unit economics) ออกจาก noise (TAM ใหญ่ที่สุดเท่าที่จะหาได้)
**ผู้เชี่ยวชาญด้าน AI:** การที่ SpaceX ผูก rocket business เข้ากับ AI dream แสดงว่า infrastructure (เครือข่ายดาวเทียม, compute on orbit, distribution channel ไปทุกที่ในโลก) กำลังถูกตีค่าใหม่ในฐานะ enabler ของ AI ไม่ใช่ธุรกิจเดี่ยว ๆ ใครคุม infra ก็คุมต้นทุนของ AI ในระยะยาว
**โปรแกรมเมอร์มืออาชีพ:** สำหรับนักพัฒนาที่ build บน cloud, การที่ infrastructure provider เริ่มถูกประเมินมูลค่าผ่านศักยภาพด้าน AI หมายความว่า pricing model ของ compute และ network จะถูกผลักไปทาง bundle ที่ผูกกับ AI service ในอนาคต อย่ายึดติดกับสมมติฐานว่าราคา egress, GPU-hour และ bandwidth จะคงที่ — วาง portability และ multi-cloud strategy ไว้ในใจตั้งแต่ออกแบบ system
