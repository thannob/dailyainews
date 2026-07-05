# Perspectives — 2026-07-05

## 1. Alibaba reportedly bans employees from using Claude Code

**อาจารย์ (มหาวิทยาลัย):** เคสนี้เป็นตำราสั้น ๆ ของ "geopolitics of tooling" — ผลิตภัณฑ์ developer tool ไม่ได้เป็นแค่เครื่องมือ แต่กลายเป็น attack surface ที่รัฐและบริษัทข้ามชาติมองต่างกัน; ให้นักเรียนเปรียบกับ Huawei/ARM/GitHub blocks รอบก่อนเพื่อดูว่ากราฟการแยกโลกซอฟต์แวร์เร่งขึ้นในระดับ **โค้ดที่โปรแกรมเมอร์พิมพ์ทุกวัน**.
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นทางเทคนิคจริงคือ **telemetry/attribution ที่ฝังใน agentic coding tool** — Claude Code รัน tool call กับ filesystem/repo, ถ้ามี logic แยก user by locale จริง ก็เป็น engineering choice ที่ควรถูก audit; นักวิจัยควรจับตา method ของนักวิจัยที่อ้าง finding นี้ให้ครบ (evidence, reproducibility) ก่อนสรุปว่าเป็น backdoor หรือแค่ locale routing.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าคุณอยู่ในทีมที่มี dev ใน CN region หรือ enterprise ที่จริงจังเรื่อง data residency — ก่อน adopt agentic CLI ตัวไหน ให้ **network-egress-audit** และ **on-device static-scan** เป็น check-list มาตรฐาน; และมี fallback plan (Qwen Coder, Copilot on-prem, local Aider + open-weight model) ที่ทีมสามารถสลับได้ใน 1 sprint.

## 2. New Google commercial imagines a Declaration of Independence written with help from AI

**อาจารย์ (มหาวิทยาลัย):** เห็น marketing move นี้เป็น *artifact ของการทำให้ AI-in-office normalize* — เมื่อ Founding Fathers ใน ad ใช้ Gemini จดประชุม, ตำรา media studies เรียกว่า **legitimation via nostalgia**; ให้นักเรียนเปรียบกับโฆษณา IBM ยุค 1980s ที่ใช้ Charlie Chaplin ปลดล็อก image ของ PC ว่า approachable.
**ผู้เชี่ยวชาญด้าน AI:** เชิงเทคนิคน้อย เชิงกลยุทธ์เยอะ — Google พยายามเปลี่ยน default association ของคำว่า "AI + งาน" จาก ChatGPT → Workspace + Gemini; สังเกตว่าโฆษณาโชว์ *"help me visualize"* กับ Gemini note-taking แทน chatbot ตัวเดียว = signal ว่า Google อยากขาย **agentic layer ผูกกับ productivity suite** ไม่ใช่โมเดลเดี่ยว.
**โปรแกรมเมอร์มืออาชีพ:** ผลกระทบตรงมาถึง developer stack คือ **Gemini ในเครื่องมือ Google (Docs, Sheets, Meet, GCP)** จะได้ deeper integration ต่อ; ถ้าทีมคุณใช้ Workspace เตรียม policy สั้น ๆ เรื่อง Gemini permission scope (email, calendar, drive) ก่อนที่ enterprise IT เปิดกว้างโดย default — sprint หน้าไม่ควรตื่นมาเจอ integration ที่ไม่ได้ vet.

## 3. Midjourney wants Hollywood studios to reveal the details of their AI usage

**อาจารย์ (มหาวิทยาลัย):** เคสตัวอย่างของ **discovery reversal** ใน IP litigation — จำเลย (Midjourney) กลับด้านให้โจทก์ (Disney/Universal/WB) ต้องเปิดเผยพฤติกรรมภายในตัวเอง; ใช้สอน strategic use of discovery ในวิชา law & tech และเปิดคำถามใหญ่ *"industry norm ของ AI use เป็นข้อต่อสู้ที่ใช้ได้ไหม?"*.
**ผู้เชี่ยวชาญด้าน AI:** ประเด็น evidentiary ที่น่าสน — ถ้า studio เปิดว่ามี *"AI-assisted production pipeline"* ใน tentpole films แม้แค่ concept art, VFX previz, หรือ script polish, มันเปลี่ยน narrative จาก "AI ขโมยงานเรา" เป็น "AI เป็นเครื่องมือของอุตสาหกรรมเราด้วย"; discovery นี้จะสร้าง corpus สาธารณะเกี่ยวกับ **ที่ทางจริงของ generative AI ในกระบวนการภาพยนตร์** ที่ตอนนี้ยังเป็นกล่องดำ.
**โปรแกรมเมอร์มืออาชีพ:** บทเรียนสำหรับทีม product ที่ทำงาน creative-adjacent — ทุก AI tool ใน pipeline ควรมี **usage log ระดับ project + shot + prompt-lineage** ตั้งแต่วันแรก; อนาคตอันใกล้ discovery อาจโดนบังคับให้เปิด และ audit log ที่ทีมเก็บไว้ = ต้นทุนถูก แต่ log ที่ต้อง reconstruct ย้อนหลัง = ต้นทุนแพงระเบิด.

## 4. Micron breaks ground on $9B Japan plant expansion — HBM for the AI stack

**อาจารย์ (มหาวิทยาลัย):** สอน supply-chain economics ของ AI — โฟกัสของสื่อไปที่ compute (GPU/TPU) แต่ **bottleneck จริงหลายครั้งคือ HBM**; ให้นักเรียนวาด value chain จาก sand → wafer → HBM stack → GPU package → data center → API endpoint แล้วชี้ว่าโรงงานใน Hiroshima อยู่จุดไหน และ **geopolitics ของ semiconductor localization** ในญี่ปุ่นกับ CHIPS Act สหรัฐฯ ต่างกันอย่างไร.
**ผู้เชี่ยวชาญด้าน AI:** สัญญาณสำคัญคือ time horizon — ship 2028 หมายความว่า industry คาด **HBM shortage ยาว 2+ ปี**; ถ้าถูก แสดงว่า inference cost ของ frontier model จะยัง sticky ต่อ, และการ optimize model architecture (MoE, quantization, KV cache, speculative decoding) ยังเป็น first-order คนดู memory bandwidth ต่อ dollar เป็น metric สำคัญกว่า FLOPS ใน 24 เดือนข้างหน้า.
**โปรแกรมเมอร์มืออาชีพ:** ผลตรงต่อทีม engineering — cloud AI price ยังไม่ collapse ในเร็ววัน; งาน optimize prompt/token/cache ยังคุ้มลงทุน, และ **capacity planning** สำหรับ product ที่พึ่ง frontier model ควรมี scenario "supply-constrained region" ที่ต้อง reroute traffic ข้าม region หรือ fallback ไปโมเดลเล็กกว่าไว้ใน architecture ตั้งแต่ตอนนี้.

## 5. China envisions AI, karaoke and coffee at cinemas

**อาจารย์ (มหาวิทยาลัย):** เห็นเป็น **policy nudge เชิง diversification** ของอุตสาหกรรมความบันเทิงเมื่อยอดขายตั๋วหนังทั่วโลกซบ; สอนใน urban economics ว่า "space ที่ under-utilized" (โรงหนัง 2/3 ของเวลาว่าง) เป็นสนามให้ policy จัด mix use ใหม่, และ AI ในบริบทนี้เป็น *venue-level experience* ไม่ใช่ back-office tool.
**ผู้เชี่ยวชาญด้าน AI:** ประเด็นเทคนิคเปิดคือ **AI agent ในพื้นที่กายภาพต้องการ stack อะไร** — ASR, TTS, spatial audio, computer vision สำหรับ crowd, voice-cloning สำหรับ karaoke; ประเทศจีนมี domestic stack ค่อนข้างครบ (Qwen, DeepSeek, MiniMax, iFlytek) ทำให้ deployment แบบนี้เกิดได้เร็วโดยไม่แตะ US models — เป็น case study ของ **vertically-integrated national AI stack** ที่ region อื่นจะเลียนแบบยาก.
**โปรแกรมเมอร์มืออาชีพ:** ถ้าทีมคุณทำ location-based app (retail, hospitality, entertainment) นี่คือ signal ว่า **on-premise AI agent + latency-sensitive UX** เป็นตลาดที่จะโตในเอเชีย; เตรียม skill (edge inference, model quantization, WebRTC + streaming ASR) และ hardware track (Jetson/Coral/Ascend) ไว้เป็น option ก่อนที่ vendor sales จะ knock on the door.
