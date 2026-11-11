---
name: usability-evaluation
description: Lập kế hoạch, chuẩn bị công cụ và phân tích kết quả cho một buổi đánh giá usability có điều phối (moderated, think-aloud) trên một luồng end-to-end với 7 người thật — kế hoạch 9 phần Rubin, kịch bản dạng mục tiêu, SUS/UEQ-S, phiếu quan sát, câu hỏi mở, tính điểm SUS, tổng hợp pain point và xếp mức độ. Dùng khi người dùng nói "làm usability test cho luồng X", "soạn kịch bản usability", "tính SUS", "tổng hợp kết quả phiên usability" (HW03 Task 2).
---

# Usability evaluation (HW03 Task 2)

AI chỉ hỗ trợ **chuẩn bị** và **phân tích**. Tuyển người, chạy phiên, quan sát, ghi chú là việc của sinh viên với người thật. AI **không bao giờ** tạo người tham gia, câu trả lời SUS, trích lời nói hay số liệu phiên.

## Đầu vào cần hỏi
1. Mã luồng và các bước (ví dụ `FL-10 Mobile: Đăng ký → Đăng nhập → Cập nhật hồ sơ`), FR liên quan.
2. Nền tảng chạy (Expo Go trên điện thoại thật, web...), cách reset dữ liệu.
3. Hồ sơ người dùng mục tiêu, thời gian dự kiến mỗi phiên.

## Phase 1: Lập kế hoạch và chuẩn bị (dừng sau mỗi mục cho sinh viên duyệt)

1. **Đọc đặc tả + mã nguồn của luồng** → liệt kê màn hình, nhãn, thông báo, quy tắc kiểm tra. Ghi các điểm có thể gây vướng thành **giả thuyết** (không phải kết quả).
2. **Kế hoạch 9 phần (Rubin):** mục đích · phát biểu vấn đề (câu hỏi cụ thể, gắn với giả thuyết) · mục tiêu và tác vụ · hồ sơ người dùng · phương pháp (moderated, think-aloud, 1 phiên/người, pilot) · môi trường/thiết bị · vai trò người điều phối · số đo (hoàn thành, thời gian, lỗi, sai đường, trợ giúp, SUS) · nội dung báo cáo.
3. **Kịch bản dạng mục tiêu**, không chỉ từng bước; mỗi tác vụ có trạng thái ban đầu, tiêu chí thành công kiểm được (giao diện + DB), benchmark thời gian, điều kiện can thiệp. Có phiếu thông tin thử nghiệm để người tham gia không nhập dữ liệu thật.
4. **Công cụ:** lời mở đầu (test sản phẩm không test người, think-aloud, xin phép quay màn hình/ghi âm/được gọi xác minh) · phiếu quan sát (mốc thời gian, tác vụ, loại sự kiện D/S/E/R/H/F/P/X, lời nói, mức Nielsen 0–4) · SUS 10 câu tiếng Việt giữ thứ tự chẵn/lẻ · câu hỏi mở về độ rõ ràng, sửa lỗi, tốc độ, độ tin cậy · checklist chuẩn bị phiên.
5. **Mẫu bảng người tham gia** (mã P1–P7, họ tên, liên hệ che 4 số giữa, nghề, tuổi, ngày giờ, đồng ý) để **trống** cho sinh viên điền; chỉ nằm trong repo cá nhân.
6. **File Excel tính SUS** với công thức: câu lẻ (điểm − 1), câu chẵn (5 − điểm), tổng × 2.5; trung bình, trung vị, min, max, độ lệch chuẩn, so với mốc 68.

## Phase 2: Trong khi sinh viên chạy phiên
- Nhắc checklist chuẩn bị trước mỗi phiên; sau mỗi phiên nhắc commit `[T2][P<n>] Record session P<n> notes and SUS answers`.
- Có thể giúp chép phiếu quan sát viết tay thành Markdown **đúng nguyên văn** sinh viên cung cấp; không thêm sự kiện.

## Phase 3: Phân tích (chỉ khi đã có dữ liệu thật của 7 phiên)
1. Tính SUS từng người và thống kê; tính tỉ lệ hoàn thành, thời gian (trung bình, trung vị, khoảng), số lỗi mỗi tác vụ.
2. Gom pain point giống nhau: vấn đề · phiên gặp · số người gặp · trích lời nói (lấy từ ghi chú của sinh viên).
3. Tách **bug** (sai đặc tả / chặn người dùng → GitHub Issues label `task: T2 usability`, ảnh không lộ người tham gia, ghi mã phiên + mốc thời gian video) và **vấn đề thiết kế** (chỉ ghi trong báo cáo).
4. Xếp mức độ = nghiêm trọng (Nielsen 0–4) × tần suất (số người gặp / 7); blocker trước.
5. Khuyến nghị có ưu tiên, trả lời từng câu hỏi nghiên cứu ở Phase 1.

## Quy tắc trung thực
- Nếu chưa có dữ liệu thật: ghi rõ trạng thái "chưa chạy phiên" trong báo cáo, để trống bảng; không ước lượng hay mô phỏng kết quả.
- Không gửi thông tin cá nhân của người tham gia cho AI.
