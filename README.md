# HW03 GUI & Usability on EShop

- Sinh viên: Trần Thanh An
- MSSV: 23120017
- Email sinh viên: 23120017@student.hcmus.edu.vn
- SUT: [EShop](https://github.com/ttbhanh/eshop-sut) (commit `85af3ba`)
- Repo nhóm (GitHub Issues): [angquoc/software-testing-2026-HW03-group](https://github.com/angquoc/software-testing-2026-HW03-group)

## 1. Phạm vi

| Hạng mục | Lựa chọn |
|---|---|
| Màn hình chính (Task 1) | A-05 Admin: Quản lý mã giảm giá (CRUD) (FR-17) |
| Màn hình phụ (Task 1) | A-02 Dashboard + sidebar (FR-13), A-03 Quản lý danh mục (FR-14) |
| Luồng usability (Task 2) | FL-10 Mobile: Đăng ký → Đăng nhập → Cập nhật hồ sơ (FR-01, FR-02, FR-04) |
| Nền tảng (Task 3) | Chrome 157 (Windows 11), Firefox 132 (Windows 11), Android Chrome 145 (Pixel 6, Android Emulator) |

## 2. Nội dung nộp

| Yêu cầu (đề §14) | File |
|---|---|
| Báo cáo chính (Task 1, 2, 3) | [23120017_HW03_Report.md](23120017_HW03_Report.md) (+ PDF) |
| Bug report + ảnh | [task1-gui-checklist/bug-report.md](task1-gui-checklist/bug-report.md), [task1-gui-checklist/screenshots/](task1-gui-checklist/screenshots/) (gồm ảnh danh sách issue trên GitHub) |
| Excel checklist + test summary | [task1-gui-checklist/23120017_HW03_GUI_Checklist.xlsx](task1-gui-checklist/23120017_HW03_GUI_Checklist.xlsx) (sheet Checklist, Tổng kết, Bug, Task 3) |
| Bằng chứng usability | [task2-usability/](task2-usability/): kế hoạch, kịch bản, công cụ, mẫu bảng người tham gia, file tính SUS. **Chưa có phiên, SUS, ghi chú quan sát** |
| Ảnh cross-platform | [task3-cross-platform/](task3-cross-platform/) (chrome, firefox, android) + [cross-platform-report.md](task3-cross-platform/cross-platform-report.md) |
| AI Audit Report | [23120017_HW03_AI_Audit_Report.md](23120017_HW03_AI_Audit_Report.md) (+ PDF), log nguyên văn [23120017_HW03_AI_Prompt_Log.md](23120017_HW03_AI_Prompt_Log.md) |
| AI Critique | [23120017_HW03_AI_Critique.md](23120017_HW03_AI_Critique.md) (+ PDF) |
| Agent Skills | [skills/](skills/): `gui-checklist`, `usability-evaluation`, `ai-audit-log` |
| Git commit log | [23120017_HW03_git-log.txt](23120017_HW03_git-log.txt) |

## 3. Test Summary

| Chỉ số | Giá trị |
|---|---|
| Số màn hình đã kiểm thử | 3 (A-05 chính; A-02, A-03 phụ) |
| Số luồng đã kiểm thử | 0 (FL-10 mới có tài liệu chuẩn bị, chưa chạy phiên) |
| Số mục checklist: thiết kế | 72 (IA-01: 23, IA-02: 22, IA-03: 11, IA-04: 16) |
| Số mục checklist: đã chạy | 72 trên mỗi nền tảng (Chrome, Firefox Windows; Android Chrome có 5 mục N/A) |
| Số mục checklist: Passed | 24 (Chrome), 24 (Firefox), 21 (Android Chrome) |
| Số mục checklist: Failed | 48 (Chrome), 48 (Firefox), 46 (Android Chrome) |
| Số bug | Task 1: 36 (High 4, Medium 19, Low 13): 35 issue #68 → #102 trên repo nhóm + 1 trùng (Related #66). Task 3: 1 bug chỉ có trên Android Chrome. Chi tiết [task1-gui-checklist/bug-report.md](task1-gui-checklist/bug-report.md), [task3-cross-platform/cross-platform-report.md](task3-cross-platform/cross-platform-report.md) |
| Số người tham gia usability | 0 / 7 (chưa tuyển) |
| Điểm SUS / UEQ-S trung bình | Chưa có dữ liệu |
| Số nền tảng cross-platform | 3 |
| Video demo Agent Skill | Chưa có |

## 4. Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---|---|
| 1 | Task 1: GUI Checklist (design + execution + bug report) | 30 | 22 |
| 2 | Task 2: Usability Evaluation (task scenario + 7 sessions + analysis) | 40 | 5 |
| 3 | Task 3: Cross-Browser / Cross-Platform (≥ 3 platforms) | 20 | 13 |
| 4 | Agent Skills | 10 | 4 |
| | **Total** | **100** | **44** |

Lý do tự chấm:
- **Task 1 (22/30):** đủ 72 mục phủ 4 IA, có review, 26 mục bổ sung kèm lý do AI bỏ sót, chạy đủ, có ảnh cho mọi mục Failed, 35 issue có ảnh và label. Trừ điểm vì quy trình bắt đầu bằng một prompt giao cả task cho AI (đề §2 yêu cầu dẫn AI từng bước), danh sách "vòng 1" được soạn lại sau chứ không phải lần sinh độc lập, và phần review của sinh viên chỉ ở mức xác nhận.
- **Task 2 (5/40):** chỉ có tài liệu Phase 1 (kế hoạch, kịch bản, SUS, phiếu quan sát, câu hỏi mở). Không có người tham gia, pilot, 7 phiên, SUS, phân tích hay bug usability. Đề §17 ghi thiếu tài liệu bắt buộc có thể bị 0 điểm.
- **Task 3 (13/20):** đủ 3 nền tảng chạy cùng 72 mục, mọi ảnh có lớp chữ đè MSSV, họ tên, email, trình duyệt và URL, có bảng so sánh và 1 bug chỉ có trên Android. Trừ điểm vì không dùng BrowserStack/LambdaTest, Android là máy ảo chứ không phải thiết bị thật, Firefox là bản Playwright đóng gói, ảnh desktop chỉ chụp vùng trang (thông tin trình duyệt nằm trong lớp chữ đè, không thấy thanh địa chỉ).
- **Agent Skills (4/10):** có 3 skill mô tả đúng quy trình đã làm và 1 script xuất prompt. Chưa có video demo trên YouTube.
