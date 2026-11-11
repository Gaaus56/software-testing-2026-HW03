---
name: gui-checklist
description: Thiết kế, review và chạy GUI checklist (> 40 mục, phủ IA-01 Chuẩn chung, IA-02 Form, IA-03 Điều hướng, IA-04 Phản hồi/trạng thái) cho một hoặc nhiều màn hình web, rồi xuất Excel, chụp ảnh mục Failed và soạn bug report theo template GitHub Issues của nhóm. Dùng khi người dùng nói "làm GUI checklist cho màn hình X", "kiểm thử giao diện màn X", "chạy lại checklist trên Firefox/Android" (Task 1, Task 3 của HW03).
---

# GUI checklist (HW03 Task 1, Task 3)

Mục tiêu: dẫn AI đi **từng bước của kỹ thuật GUI checklist như đã học** (khảo sát → oracle → sinh mục theo IA → review → bổ sung mục AI bỏ sót → chạy → báo bug), không dùng một prompt chung chung. Sau mỗi bước phải dừng lại cho sinh viên duyệt.

## Đầu vào cần hỏi trước khi bắt đầu

1. Mã và tên màn hình (ví dụ `A-05 Quản lý mã giảm giá`), URL chạy local, tài khoản đăng nhập.
2. Đặc tả: đường dẫn README của SUT; các FR liên quan và FR-21 → FR-24 (IA-01 → IA-04).
3. Nền tảng chạy (mặc định Chrome Windows 1366×768, locale vi-VN).
4. Thang severity và quy ước issue của nhóm (README repo nhóm mục 4).

## Quy trình (dừng sau mỗi bước, đưa kết quả cho sinh viên duyệt)

### Bước 1. Khảo sát màn hình
- Mở màn hình bằng Playwright, trích DOM: mọi control (loại, nhãn, placeholder, `required`/`min`/`maxLength`, màu, kích thước), tiêu đề, landmark, `lang`, `title`.
- Chụp ảnh toàn màn hình, ghi hành vi khi thao tác thử (submit rỗng, nhập sai, xóa).
- Đầu ra: bảng control × thuộc tính + danh sách hành vi đáng chú ý.

### Bước 2. Oracle
- Trích **nguyên văn** câu đặc tả cho từng IA và FR của màn hình. Câu nào không có trong đặc tả mà suy ra từ FR của màn khác thì ghi rõ "suy rộng".
- Bổ sung nguồn ngoài đặc tả: Nielsen 10, Norman 6, Shneiderman 8, checklist Waghmare (slide môn), WCAG 2.2 A/AA.

### Bước 3. Sinh mục theo từng IA (mỗi IA một prompt)
Prompt mẫu (thay biến):
```
Bạn là tester GUI. Chỉ dùng đặc tả sau và danh sách control (tên + loại) của màn {SCREEN}.
Sinh các mục kiểm tra cho {IA} ({IA_NAME}). Mỗi mục: control, điều kiện kiểm, kết quả mong đợi đo được (Pass/Fail rõ ràng), nguồn (FR/heuristic/WCAG).
Không sinh mục cho màn hình khác. Không sinh mục mơ hồ kiểu "giao diện đẹp".
Đặc tả: {ORACLE_IA}
Control: {CONTROLS}
```
Lưu nguyên văn danh sách sinh ra (làm "vòng 1") để so sánh.

### Bước 4. Review từng mục
Với mỗi mục hỏi 4 câu: kiểm được không (có tiêu chí Pass/Fail)? đúng phạm vi màn hình không? trùng không? đủ cụ thể (control, dữ liệu, kết quả) không? → quyết định **Giữ / Sửa / Gộp / Bỏ** kèm lý do. Đầu ra: bảng review + tổng số mỗi loại.

### Bước 5. Bổ sung mục AI bỏ sót
- Dò theo các nhóm AI hay bỏ sót: khả năng truy cập (label, tên truy cập, bàn phím, focus, tương phản, zoom 200%/400%), dark mode, RTL, trạng thái loading/lỗi mạng/phiên hết hạn, nút Back/F5, nhấp đúp, dữ liệu biên (rỗng, khoảng trắng, rất dài, âm, 0, ngày quá khứ), định dạng theo locale.
- Mỗi mục thêm **bắt buộc** có cột "Lý do AI bỏ sót", phân loại: Chất lượng đầu vào / Giới hạn của mô hình / Đặc thù giao diện.

### Bước 6. Lập Excel
Sheet `Checklist` 16 cột: ID · IA · Màn hình · Control · Mục kiểm tra · Kết quả mong đợi · Nguồn · Ưu tiên · Mức nghiêm trọng (1–4) · Nguồn gốc (AI / AI-sửa / Bổ sung) · Lý do AI bỏ sót · Kết quả · Notes · Ảnh · Bug ID · Issue #. Sheet `Tổng kết` chỉ dùng công thức COUNTIF/COUNTIFS. Quy tắc:
- Ưu tiên = Bắt buộc nếu nguồn là FR/SEC hoặc WCAG A/AA (không tính nguồn "suy rộng"), còn lại Tùy chọn.
- Mức nghiêm trọng theo thang nhóm: 1 Critical, 2 High, 3 Medium, 4 Low; sai đặc tả nhưng chỉ về hiển thị/câu chữ/màu → 4.

### Bước 7. Chạy checklist
- Viết mỗi mục thành một hàm Playwright trả về Passed/Failed + Notes; reset DB trước mục cần dữ liệu sạch.
- Thao tác như người dùng thật (gõ bàn phím, bấm nút), không gán giá trị bằng JavaScript.
- Chỉ chụp ảnh mục Failed; ảnh có khung chú thích chỉ đúng chỗ lỗi. Lỗi nằm ngoài nội dung trang (alert, tiêu đề tab) thì yêu cầu sinh viên chụp tay cả cửa sổ trình duyệt.
- Sau khi chạy: sinh viên **tự thao tác lại** các mục High/Critical và xem toàn bộ ảnh trước khi kết luận.

### Bước 8. Bug report
- Gom các mục Failed cùng nguyên nhân thành 1 bug; severity bug = mức cao nhất của các mục.
- Kiểm trùng trên repo nhóm (issue cùng màn/thành phần dùng chung → comment `Related #n`, không tạo mới; trùng HW02 → ghi `Related <repo>#n`).
- Soạn cho mỗi bug: tiêu đề `[MSSV][T1][Mã màn hình][Nền tảng] Mô tả`, label (severity, platform, task, ia), điều kiện, các bước, mong đợi (trích FR), thực tế, ảnh. Sinh link `issues/new?template=bug_report.yml&title=...&labels=...` điền sẵn các ô chữ để sinh viên tạo issue; dropdown phải chọn tay.

### Bước 9 (Task 3). Chạy lại trên nền tảng khác
- Dùng **đúng bộ mục** của Bước 7, chạy lần lượt trên ≥ 3 nền tảng (ví dụ Chrome Windows, Firefox Windows, Android Chrome qua `adb reverse` + Playwright `_android`).
- Mọi ảnh có lớp chữ đè: MSSV · họ tên · email sinh viên · trình duyệt/OS/thiết bị · URL localhost.
- Mục không áp dụng trên nền tảng (hover trên cảm ứng, zoom trên thiết bị) ghi **N/A** kèm lý do; lỗi do script (tọa độ ngoài màn hình, phần tử bị che) phải sửa script và chạy lại, không ghi thành Failed.
- Lập bảng mục × nền tảng; bug chỉ xuất hiện trên một số nền tảng → issue label `task: T3 cross-platform`.

## Quy tắc trung thực
- Không bịa kết quả, ảnh hay số issue. Không ghi "sinh viên đã review" khi sinh viên chưa làm.
- Ghi rõ trong báo cáo phần nào AI làm, phần nào sinh viên làm; giữ nguyên prompt và output cho AI Audit Report.
