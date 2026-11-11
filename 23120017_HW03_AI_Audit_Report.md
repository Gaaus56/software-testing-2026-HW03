# AI Audit Report (mẫu AI-02, FIT@HCMUS)

## 1. Thông tin sinh viên

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa) | TRẦN THANH AN |
| MSSV | 23120017 |
| Lớp / Khoá | CQ2023/3 |
| Mã bài tập | HW03 – GUI & Usability |
| Ngày làm bài | 09/11/2026 → 11/11/2026 |
| Công cụ AI đã dùng | [x] Có  [ ] Không — Claude Code (model Claude Opus 5.5) trong VS Code, gồm 1 subagent đánh giá Task 1 |

**Khai báo (đề bài §9):** *I use AI tools for the following tasks,* liệt kê đầy đủ ở mục 2 (mỗi lần tương tác: tên công cụ, ngày giờ, prompt nguyên văn, output). Log nguyên văn toàn bộ prompt và câu trả lời của AI: [23120017_HW03_AI_Prompt_Log.md](23120017_HW03_AI_Prompt_Log.md) (xuất tự động từ file phiên `.jsonl` bằng skill `skills/ai-audit-log`).

## 2. Danh sách tương tác với AI (27 lượt)

Prompt chép nguyên văn từ file phiên (chỉ bỏ thẻ do IDE/hệ thống tự chèn). Cột Output là tóm tắt; nguyên văn output ở log.

| # | Công cụ | Thời gian (UTC+7) | Prompt (nguyên văn) | Output (tóm tắt) |
|---|---|---|---|---|
| 01 | Claude Code (Claude Opus 5.5) | 14:12 09/11/2026 | Đọc cây thư mục và file yêu cầu D:\codeStudy\test\Homeworks\HW03\docs\2026.HW03.GUI Usability_En.pdf sau đó giải thích bài tập môn kiểm thử phần mềm tuần này cho tôi. Nếu cần thêm file nào hãy thông báo | Giải thích đề HW03: 4 task, IA-01→04, yêu cầu bắt buộc, file cần thêm. [log #01](23120017_HW03_AI_Prompt_Log.md) |
| 02 | Claude Code (Claude Opus 5.5) | 14:26 09/11/2026 | tôi vừa thêm vào repo nhóm và tạo repo cá nhân và slide. Đọc qua sau đó khởi tạo repo  cá nhân theo đúng yêu cầu của thầy, không tự tạo những thứ dư thừa. không commit kèm claude trong đó | Khởi tạo repo cá nhân theo quy ước README nhóm (README, cấu trúc tối thiểu), commit không kèm tên AI. [log #02](23120017_HW03_AI_Prompt_Log.md) |
| 03 | Claude Code (Claude Opus 5.5) | 14:33 09/11/2026 | tôi vừa thêm file excel chọn feature của nhóm, đọc và gợi ý chọn <br>_(kèm 1 ảnh)_ | Đọc file Excel chọn feature của nhóm, gợi ý Gói 2: A-05 chính, A-02/A-03 phụ, FL-10 Mobile. [log #03](23120017_HW03_AI_Prompt_Log.md) |
| 04 | Claude Code (Claude Opus 5.5) | 14:43 09/11/2026 | sửa và trong repo nhóm và cá nhân, sau đó đưa lệnh tôi tự commit | Sửa README nhóm và cá nhân theo lựa chọn, đưa lệnh commit để sinh viên tự chạy. [log #04](23120017_HW03_AI_Prompt_Log.md) |
| 05 | Claude Code (Claude Opus 5.5) | 14:51 09/11/2026 | lập file plan hoàn thành từng bước bài tập và checklist trong docs | Lập docs/PLAN.md: kế hoạch từng bước 4 task + checklist + tên commit. [log #05](23120017_HW03_AI_Prompt_Log.md) |
| 06 | Claude Code (Claude Opus 5.5) | 15:07 09/11/2026 | Bắt đầu xuất prompt gốc chính xác từ file JSON. Tôi chạy mobile bằng máy ảo pixel 6 trong lap. Hãy setup chạy cho tôi | Viết export_prompts.py xuất prompt từ JSONL; cài và chạy app Mobile trên máy ảo Pixel 6 (API 10.0.2.2). [log #06](23120017_HW03_AI_Prompt_Log.md) |
| 07 | Claude Code (Claude Opus 5.5) | 15:20 09/11/2026 | giao tiếp bằng tiếng việt | Ghi nhớ: trả lời bằng tiếng Việt. [log #07](23120017_HW03_AI_Prompt_Log.md) |
| 08 | Claude Code (Claude Opus 5.5) | 15:25 09/11/2026 | lỗi chạy backend | Chẩn đoán lỗi backend: cổng 3000 đang bị chiếm (EADDRINUSE). [log #08](23120017_HW03_AI_Prompt_Log.md) |
| 09 | Claude Code (Claude Opus 5.5) | 15:26 09/11/2026 | thêm lệnh chạy chi tiết mobile vào plan và tắt hết để tôi tự chạy | Thêm lệnh chạy Mobile chi tiết vào PLAN, tắt toàn bộ tiến trình. [log #09](23120017_HW03_AI_Prompt_Log.md) |
| 10 | Claude Code (Claude Opus 5.5) | 15:29 09/11/2026 | chạy backend lỗi | Hướng dẫn chạy backend. [log #10](23120017_HW03_AI_Prompt_Log.md) |
| 11 | Claude Code (Claude Opus 5.5) | 15:30 09/11/2026 | [Nội dung dán vào] (base) PS D:\codeStudy\test\Homeworks\HW03\eshop-sut> node database.js<br>node:internal/modules/cjs/loader:1433<br>  throw err;<br>  ^<br><br>Error: Cannot find module 'D:\codeStudy\test\Homeworks\HW03\eshop-sut\database.js'<br>    at Function._resolveFilename (node:internal/modules/cjs/loader:1430:15)<br>    at defaultResolveImpl (node:internal/modules/cjs/loader:1040:19)<br>    at resolveForCJSWithHooks (node:internal/modules/cjs/loader:1045:22)<br>    at Function._load (node:internal/modules/cjs/loader:1216:25)<br>    at wrapModuleLoad (node:internal/modules/cjs/loader:254:19)<br>    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:171:5)     <br>    at node:internal/main/run_main_module:36:49 {<br>  code: 'MODULE_NOT_FOUND',<br>  requireStack: []<br>}<br><br>Node.js v22.23.2<br>(base) PS D:\codeStudy\test\Homeworks\HW03\eshop-sut> | Chỉ ra lỗi chạy `node database.js` sai thư mục (phải ở backend/). [log #11](23120017_HW03_AI_Prompt_Log.md) |
| 12 | Claude Code (Claude Opus 5.5) | 15:32 09/11/2026 | lệnh chạy frontend đâu | Thêm lệnh chạy Web Admin vào PLAN. [log #12](23120017_HW03_AI_Prompt_Log.md) |
| 13 | Claude Code (Claude Opus 5.5) | 15:58 09/11/2026 | mobile che mất header của app <br>_(kèm 1 ảnh)_ | Phân tích: status bar che header là bug thật của SUT (SafeAreaView chỉ có tác dụng trên iOS), khuyên không sửa SUT. [log #13](23120017_HW03_AI_Prompt_Log.md) |
| 14 | Claude Code (Claude Opus 5.5) | 00:35 11/11/2026 | hoàn thành chi tiết và hoàn hảo task 1, tự kiểm tra kĩ | Thực hiện toàn bộ Task 1: khảo sát DOM, oracle, danh sách 54 mục, review, bổ sung 26 mục, script Playwright chạy 72 mục, Excel, ảnh, bug report. [log #14](23120017_HW03_AI_Prompt_Log.md) |
| 15 | Claude Code (Claude Opus 5.5) | 01:50 11/11/2026 | trong repo cá nhân chỉ để các file cần thiết nộp bài đầy đủ theo yêu cầu. không để file dư, các file dư thì để ra docs | Dọn repo chỉ giữ file nộp; chuyển file quy trình ra docs, gộp thành báo cáo chính. [log #15](23120017_HW03_AI_Prompt_Log.md) |
| 16 | Claude Code (Claude Opus 5.5) | 01:58 11/11/2026 | - Đảm bảo đặt tên file đúng yêu cầu<br>- Gọi subagent đánh giá task 1<br>- Rà lại Task 1 và hoàn thành đầy đủ, commit không dính claude<br>- Báo lại chi tiết công việc task 1 cho tôi, phần đẫ hoàn thành, phần cần tôi làm nếu có | Gọi subagent chấm Task 1 (~17/30), sửa theo góp ý: khai báo trung thực quy trình, sửa trích FR-24, chạy lại CL-18/21/55/38/53, tách bug, áp quy tắc severity; commit. [log #16](23120017_HW03_AI_Prompt_Log.md) |
| 17 | Claude Code (Claude Opus 5.5) | 08:15 11/11/2026 | xác nhận trong báo cáo nào | Chỉ vị trí bảng xác nhận của sinh viên (cuối mục 1.5). [log #17](23120017_HW03_AI_Prompt_Log.md) |
| 18 | Claude Code (Claude Opus 5.5) | 08:27 11/11/2026 | - Đã kiểm tra xong, đổi lại (chưa làm)<br>- Giờ tôi tạo issue, tạo file hướng dẫn chi tiết, điền sẵn form và link, hướng dẫn chụp ảnh... <br>_(kèm 2 ảnh)_ | Ghi xác nhận review của sinh viên; đổi tiêu đề issue theo dạng nhóm; tạo trang hướng dẫn tạo issue có link form điền sẵn; phát hiện BUG-06 trùng issue #66. [log #18](23120017_HW03_AI_Prompt_Log.md) |
| 19 | Claude Code (Claude Opus 5.5) | 08:40 11/11/2026 | file hướng dẫn tạo issue đâu <br>_(kèm 1 ảnh)_ | Chỉ đường dẫn trang hướng dẫn; xác nhận 67 issue cũ không trùng màn Admin trừ #66. [log #19](23120017_HW03_AI_Prompt_Log.md) |
| 20 | Claude Code (Claude Opus 5.5) | 08:45 11/11/2026 | tôi chưa hiểu hướng dẫn, giải thích dễ hiểu mở form xong làm gì <br>_(kèm 2 ảnh)_ | Giải thích các bước điền form; sửa trang hướng dẫn vì dropdown không điền sẵn được. [log #20](23120017_HW03_AI_Prompt_Log.md) |
| 21 | Claude Code (Claude Opus 5.5) | 08:51 11/11/2026 | có cần chụp lại ảnh issue như vầy không <br>_(kèm 1 ảnh)_ | Trả lời: không cần chụp từng issue, chỉ chụp danh sách issue. [log #21](23120017_HW03_AI_Prompt_Log.md) |
| 22 | Claude Code (Claude Opus 5.5) | 09:04 11/11/2026 | issue bug06 chỉ cần như vầy thôi đúng không <br>_(kèm 1 ảnh)_ | Góp ý comment BUG-06: thêm dòng mô tả tái hiện, không bấm Close. [log #22](23120017_HW03_AI_Prompt_Log.md) |
| 23 | Claude Code (Claude Opus 5.5) | 09:31 11/11/2026 | đã tạo xong issue:<br><br>[Nội dung dán vào] BUG-01 = #68<br>BUG-02 = #69<br>BUG-03 = #70<br>BUG-04 = #71<br>BUG-05 = #72<br>BUG-06 = #66<br>BUG-07 = #73<br>BUG-08 = #74<br>BUG-09 = #75<br>BUG-10 = #76<br>BUG-11 = #77<br>BUG-12 = #78<br>BUG-13 = #79<br>BUG-14 = #80<br>BUG-15 = #81<br>BUG-16 = #82<br>BUG-17 = #83<br>BUG-18 = #84<br>BUG-19 = #85<br>BUG-20 = #86<br>BUG-21 = #87<br>BUG-22 = #88<br>BUG-23 = #89<br>BUG-24 = #90<br>BUG-25 = #91<br>BUG-26 = #92<br>BUG-27 = #93<br>BUG-28 = #94<br>BUG-29 = #95<br>BUG-30 = #96<br>BUG-31 = #97<br>BUG-32 = #98<br>BUG-33 = #99<br>BUG-34 = #100<br>BUG-35 = #101<br>BUG-36 = #102 | Điền số issue #68–#102 và Related #66 vào bug report, Excel, README; commit. [log #23](23120017_HW03_AI_Prompt_Log.md) |
| 24 | Claude Code (Claude Opus 5.5) | 09:42 11/11/2026 | ảnh CL-09 là sao. chụp 3 ảnh à <br>_(kèm 1 ảnh)_ | Giải thích 3 ảnh cần chụp lại (CL-09 tab title, CL-41/62 alert). [log #24](23120017_HW03_AI_Prompt_Log.md) |
| 25 | Claude Code (Claude Opus 5.5) | 09:57 11/11/2026 | tôi đã chụp lại và sửa xong, commit và push.<br>Ta còn cần làm gì để hoàn thành bài tập | Phát hiện ảnh chưa commit và repo chưa push; xem lại ảnh, thay CL-62, commit và push; liệt kê phần còn lại. [log #25](23120017_HW03_AI_Prompt_Log.md) |
| 26 | Claude Code (Claude Opus 5.5) | 10:22 11/11/2026 | bỏ qua phần chạy với người khác vì đã sắp đến giờ nộp bài tập. Hoàn thành luôn các phần còn lại có thể. Xuất prompt log chuẩn thực tế theo file JSON. Thêm đầy đủ tài liệu đề yêu cầu. Tự chấm điểm đúng thực tế. | Làm Task 3 (Chrome, Firefox, Android Chrome; lớp chữ đè; bảng so sánh), tài liệu Task 2 Phase 1 (không bịa phiên), 3 Agent Skills, prompt log, AI Audit Report, AI Critique, README tự chấm, PDF, git log, zip. [log #26](23120017_HW03_AI_Prompt_Log.md) |
| 27 | Claude Code (Claude Opus 5.5) | 11:17 11/11/2026 | issue 103<br>Lớp CQ2023/3<br>Giảng viên Lâm Quang Vũ<br>Clean repo sau khi sửa xong và đảm bảo đúng đủ để tôi tự zip nộp <br>_(kèm 1 ảnh)_ | Điền số issue Task 3 (#103), lớp và giảng viên vào Audit Report; dựng lại báo cáo, PDF, git log; dọn repo để sinh viên tự nén nộp. [log #27](23120017_HW03_AI_Prompt_Log.md) |

## 3. Bảng audit (1 hàng / artifact do AI sinh)

Ký hiệu verdict: **VALID** đúng, dùng nguyên · **INVALID** sai, loại bỏ/viết lại · **INCOMPLETE** chấp nhận sau khi sửa. Cột (5) ghi rõ ai sửa: phần lớn bản sửa do AI thực hiện **theo kết quả review** (subagent đánh giá, sinh viên chỉ ra, hoặc đối chiếu trên SUT thật), sinh viên duyệt lại.

| # | (1) Prompt + Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB / slide) | (5) Bản sửa |
|---|---|---|---|---|---|
| 1 | Claude Code · 11/11/2026 00:35 · log #14: "hoàn thành chi tiết và hoàn hảo task 1, tự kiểm tra kĩ" | Script `survey.js` trích DOM 3 màn A-02/A-03/A-05 (control, placeholder, required, màu) + ảnh khảo sát (báo cáo mục 1.1) | VALID | Đúng thực tế khi đối chiếu ảnh và mã `App.jsx`; là đầu vào cho checklist-based testing (ISTQB FL v4.0 §4.4.3) | Dùng nguyên |
| 2 | như #1 | Bảng oracle IA-01→04 (mục 1.2), ban đầu trích FR-24 như thể áp dụng cho Admin | INCOMPLETE | FR-24 chỉ nói về giỏ hàng/xóa sản phẩm của Web; dùng sai oracle làm kết quả mong đợi không có căn cứ (ISTQB Glossary: test oracle phải là nguồn xác định đúng kết quả mong đợi của đối tượng kiểm thử) | Sửa sau review của subagent (log #16): trích đúng nguyên văn, các mục CL-57→60 đổi nguồn sang Nielsen/Shneiderman và ghi "suy rộng" |
| 3 | như #1 | Danh sách 54 mục "chỉ dựa trên đặc tả" (mục 1.3) | INCOMPLETE | 7 mục chép yêu cầu của màn Web, 1 mục không đo được ("giao diện đẹp"), 1 trùng; nhiều mục mơ hồ, không có tiêu chí Pass/Fail (slide S13: mục checklist phải kiểm được) | Review (mục 1.4): Giữ 35 · Sửa 8 · Gộp 2 · Bỏ 9 |
| 4 | như #1 | Đoạn mô tả quy trình Task 1 trong báo cáo bản đầu: "AI sinh vòng 1 với đầu vào giới hạn → sinh viên review" | **INVALID** | Không đúng thực tế: chỉ có 1 prompt, AI đã đọc mã nguồn trước, review cũng do AI. Vi phạm yêu cầu trung thực của đề §2, §11 | Viết lại hoàn toàn (log #16): khai báo trung thực ở mục 1.3, bảng xác nhận của sinh viên ở cuối mục 1.5 |
| 5 | như #1 | 26 mục bổ sung + cột "Lý do AI bỏ sót" (mục 1.5) | INCOMPLETE | Một số lý do mâu thuẫn với đầu vào đã khai; CL-20 phân loại sai nhóm (đề §6 Task 1 yêu cầu giải thích vì sao AI bỏ sót) | Định nghĩa lại đầu vào của danh sách mốc (chỉ tên + loại control), viết lại lý do, phân loại lại CL-20 |
| 6 | như #1 | Script `exec.js` chạy 72 mục + kết quả Passed/Failed | INCOMPLETE | CL-18, CL-21, CL-55 bị chấm Passed nhầm (tiêu chí script quá lỏng); CL-38 gán giá trị bằng JavaScript thay vì gõ phím; CL-53 dùng lịch sử about:blank không thực tế (ISTQB FL §1.3: kết quả kiểm thử phải tái lập được) | Sửa tiêu chí và chạy lại (log #16): 3 mục thành Failed; CL-38 kiểm bằng bàn phím vẫn Passed; CL-53 dùng lịch sử thật. Kết quả cuối 24 Passed / 48 Failed |
| 7 | như #1 | 50 ảnh chụp mục Failed | INCOMPLETE | Playwright không chụp được hộp thoại `alert()` và thanh tab → ảnh CL-09, CL-41, CL-62 không chứng minh được lỗi | **Sinh viên** chụp tay cả cửa sổ Chrome (log #24, #25), dán vào issue #94, #77, #76 |
| 8 | như #1 và log #18 | Bug report 36 bug, severity, tiêu đề/label issue | INCOMPLETE | Gộp nhầm 2 cặp lỗi khác nguyên nhân; severity/ưu tiên không theo quy tắc nhóm; tiêu đề nhiều màn hình dùng "/" khác quy ước nhóm; BUG-06 trùng issue #66 (ISTQB FL §5.5 defect report: không báo trùng) | Tách bug, tính severity bằng quy tắc (mức cao nhất của mục), đổi tiêu đề sang "A-02, A-03"; BUG-06 không tạo issue mới mà comment vào #66. **Sinh viên** tạo 35 issue #68–#102 |
| 9 | Claude Code · 11/11/2026 10:22 · log #26: "bỏ qua phần chạy với người khác ... Hoàn thành luôn các phần còn lại có thể..." | Kết quả Task 3 trên Android Chrome lần chạy đầu | INCOMPLETE | 4 mục Error do giới hạn công cụ/script (bấm tọa độ ngoài màn hình 411px, khung chú thích che nút); 14 ảnh bị tooltip Chrome che lớp chữ đè; các mục hover/zoom không áp dụng trên thiết bị cảm ứng | Sửa script riêng cho Android và chạy lại CL-48, CL-59 (Failed như desktop); chạy lại 14 ảnh; 5 mục ghi N/A có lý do (xem Task 3 mục 4) |
| 10 | như #9 | Tài liệu Task 2 Phase 1: kế hoạch 9 phần, kịch bản, SUS tiếng Việt, phiếu quan sát, câu hỏi mở, file Excel tính SUS | INCOMPLETE | Chưa được kiểm chứng bằng phiên pilot với người thật (slide S13: pilot để phát hiện kịch bản không rõ, sai thời lượng) | Giữ nguyên, đánh dấu "chưa pilot"; bảng người tham gia để trống, không bịa |
| 11 | như #9 | 3 Agent Skills (`gui-checklist`, `usability-evaluation`, `ai-audit-log`) | VALID | Mô tả đúng quy trình đã thực hiện thật trong bài; có quy tắc trung thực | Dùng nguyên; chưa có video demo |
| 12 | Claude Code · log #06 và #26 | Script `export_prompts.py` xuất prompt từ file `.jsonl` | INCOMPLETE | Bản đầu lẫn thông báo hệ thống `<task-notification>` thành một "prompt" của sinh viên, không ghi công cụ AI đã gọi | Lọc thẻ hệ thống, thêm thống kê công cụ mỗi lượt; số lượt prompt đúng bằng số tin nhắn thật của sinh viên |

## 4. Tổng kết độ chính xác của AI

| Chỉ số | Số lượng | Tỉ lệ |
|---|---|---|
| Tổng artifact AI sinh đã audit | 12 | 100% |
| VALID (đúng, dùng nguyên) | 2 | 16.7% |
| INVALID (sai; loại bỏ/viết lại) | 1 | 8.3% |
| INCOMPLETE (chấp nhận sau khi sửa) | 9 | 75.0% |

Ở mức mục checklist: 54 mục danh sách mốc → 35 giữ nguyên (64.8%), 8 sửa, 2 gộp, 9 bỏ (16.7%); 26 mục phải bổ sung; 3/72 kết quả chạy bị chấm sai trước khi review (4.2%).

## 5. Kết luận: khi nào nên / không nên dùng AI?

AI mạnh ở phần lặp và đo đạc: trích DOM, viết script Playwright chạy lại cùng 72 mục trên 3 nền tảng, tính tỉ lệ tương phản, lập Excel bằng công thức, soạn bug report đồng nhất. AI sai ở những chỗ cần phán đoán và trung thực: mô tả quy trình đẹp hơn thực tế, trích đặc tả của màn hình khác làm oracle, tin vào số đo DOM trong khi ảnh không chứng minh được lỗi, và ghi lỗi của script thành lỗi của sản phẩm. Khi AI tự review kết quả của chính nó trong cùng phiên, các lỗi này không lộ ra; chỉ lộ khi có người review độc lập (subagent, sinh viên) và khi đối chiếu ảnh/SUT thật. Khuyến nghị: dùng AI để sinh và chạy, nhưng mỗi bước phải có tiêu chí Pass/Fail rõ, bằng chứng nhìn thấy được và người review không phải là chính AI đó. Không dùng AI cho phần cần con người thật (người tham gia usability).

## 6. Mandatory Disclosure

"Checklist GUI (72 mục), script kiểm thử, kết quả chạy trên 3 nền tảng, bug report 36 bug, tài liệu chuẩn bị usability và báo cáo này được sinh phiên bản đầu bởi Claude Code (model Claude Opus 5.5); tôi đã rà soát lại 72 mục, tự thao tác lại 4 bug High trên Chrome, xem lại ảnh, phát hiện lỗi status bar che header của app Mobile, chụp lại 3 ảnh hộp thoại/tiêu đề tab, tạo 35 GitHub issue Task 1 (#68–#102), 1 issue Task 3 (#103) và comment issue trùng #66; phần lựa chọn phạm vi (Gói 2), việc tạo issue và chụp ảnh thủ công do tôi tự làm. Task 2 chưa chạy phiên với người thật nên không có dữ liệu người tham gia, SUS hay phân tích. AI Audit Report chi tiết đính kèm ở file này và log nguyên văn 23120017_HW03_AI_Prompt_Log.md. Tôi cam đoan không dùng AI để sinh bất kỳ artifact nào thuộc danh mục bị cấm (danh sách người tham gia, ảnh cross-platform giả)."

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa) | TRẦN THANH AN |
| MSSV | 23120017 |
| Lớp / Khoá | CQ2023/3 |
| Môn học | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên | Lâm Quang Vũ |
| Ngày | 11/11/2026 |
| Chữ ký | *(sinh viên ký)* |

## Tham khảo
- Kharbach, M. (2026). *AI Use Policy Templates for Higher Education*. CC BY-NC-SA 4.0 (mẫu AI-02 của FIT@HCMUS).
- ISTQB Certified Tester Foundation Level Syllabus v4.0: §1.3 nguyên tắc kiểm thử, §4.2.2 phân tích giá trị biên, §4.4.3 checklist-based testing, §5.5 quản lý lỗi.
- Slide S13 – GUI Testing & Usability Testing (môn Kiểm chứng Phần mềm).
