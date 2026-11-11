# Task 2 · Phase 1: Kế hoạch đánh giá usability (FL-10 Mobile)

> **Trạng thái (11/11/2026):** Đã hoàn thành Phase 1 phần tài liệu (kế hoạch, kịch bản, công cụ, mẫu bảng người tham gia). **Chưa tuyển người, chưa chạy phiên pilot và 7 phiên, chưa có dữ liệu SUS** vì không kịp thời hạn nộp. Không có số liệu nào trong thư mục này được tạo ra thay cho dữ liệu thật.

Kế hoạch theo cấu trúc 9 phần của Rubin & Chisnell (*Handbook of Usability Testing*), như slide S13.

## 1. Mục đích

Đánh giá mức độ một người lần đầu dùng ứng dụng EShop Mobile có thể **tự tạo tài khoản, đăng nhập và cập nhật thông tin nhận hàng** mà không cần trợ giúp. Kết quả dùng để tìm điểm nghẽn trong luồng FL-10 và đề xuất sửa trước khi mở cho người dùng thật.

## 2. Phát biểu vấn đề (câu hỏi nghiên cứu)

| # | Câu hỏi | Vì sao đặt câu hỏi này (giả thuyết từ việc đọc đặc tả và mã nguồn, chưa kiểm chứng với người dùng) |
|---|---|---|
| Q1 | Người dùng có tạo được mật khẩu đạt yêu cầu ngay lần đầu không? Nếu bị từ chối, họ có hiểu vì sao và tự sửa được không? | Quy tắc mật khẩu mạnh (FR-01) chỉ có một dòng gợi ý dưới ô; lỗi báo bằng hộp đỏ ở đầu form, xa ô mật khẩu |
| Q2 | Người dùng có nhận ra mình đã đăng ký thành công và cần làm gì tiếp theo không? | Sau khi đăng ký app hiện hộp thoại "Thành công" rồi chuyển sang màn Đăng nhập |
| Q3 | Màn Đăng nhập có gây nhầm lẫn không? | Nhãn ô email là "Username", nút là "Sign In" (tiếng Anh) trong khi phần còn lại tiếng Việt |
| Q4 | Người dùng có tìm được nơi cập nhật hồ sơ không? | Hồ sơ nằm chung màn với lịch sử đơn hàng; cần biết người dùng tìm theo đường nào |
| Q5 | Người dùng có lưu được số điện thoại thật dạng `09xxxxxxxx` không, và có biết đã lưu thành công không? | Mã nguồn kiểm số điện thoại bằng `^[1-9][0-9]{8,9}$` (từ chối số bắt đầu bằng 0), trái với FR-04 và với ví dụ "VD: 0912345678" ngay trong ô → **dự đoán là điểm chặn** |
| Q6 | Người dùng có tin rằng dữ liệu đã được lưu đúng không? | Không có trạng thái đang xử lý; thông báo lỗi chung chung ("Lỗi cập nhật") |

## 3. Mục tiêu và tác vụ

| Tác vụ | Mục tiêu người dùng | FR liên quan | Tiêu chí thành công | Benchmark |
|---|---|---|---|---|
| T1 Đăng ký | Tạo tài khoản EShop mới | FR-01 | Tài khoản được tạo (có trong DB) và người dùng đứng ở màn Đăng nhập | ≤ 2 phút |
| T2 Đăng nhập | Vào được tài khoản vừa tạo | FR-02 | Vào được trang chủ ở trạng thái đã đăng nhập | ≤ 45 giây |
| T3 Cập nhật hồ sơ | Lưu số điện thoại và địa chỉ nhận hàng | FR-04 | Họ tên, SĐT, địa chỉ trong DB khớp phiếu thông tin thử nghiệm | ≤ 2 phút |

Chi tiết kịch bản ở [02-task-scenario.md](02-task-scenario.md).

## 4. Hồ sơ người dùng (người tham gia)

- 7 người, **ngoài lớp đang học HW03**; ưu tiên người không làm IT/kiểm thử.
- 18–45 tuổi, dùng smartphone Android hằng ngày, đã từng mua hàng online ít nhất 1 lần trong 6 tháng.
- Chưa từng dùng EShop.
- Có liên hệ xác minh được (Zalo/SĐT/email, che 4 số giữa) vì TA có thể gọi 2 người bất kỳ.
- Cơ cấu mong muốn: ít nhất 2 người trên 30 tuổi, ít nhất 3 người không học/làm ngành CNTT.

## 5. Phương pháp

- **Moderated, trực tiếp**, 1 người/phiên, khoảng 20 phút/phiên (5 phút giới thiệu, 10 phút làm tác vụ, 5 phút SUS + câu hỏi mở).
- **Think-aloud đồng thời**: người tham gia nói to điều họ đang nghĩ.
- Mọi người làm cùng 3 tác vụ theo cùng thứ tự (T1 → T2 → T3 là luồng phụ thuộc nhau nên không đảo thứ tự).
- Người điều phối không gợi ý; chỉ can thiệp khi người tham gia **bế tắc quá 2 phút** hoặc tự đề nghị bỏ cuộc → ghi "có trợ giúp".
- Trước 7 phiên chính: **1 phiên pilot** với 1 người (không tính vào 7) để kiểm tra kịch bản, thời gian và thiết lập.
- Reset DB trước mỗi phiên; mỗi người dùng một email thử nghiệm riêng.

## 6. Môi trường và thiết bị

| Hạng mục | Thiết lập |
|---|---|
| Thiết bị | Điện thoại Android của người điều phối (không dùng máy của người tham gia để tránh lộ dữ liệu cá nhân); dự phòng: máy ảo Pixel 6 |
| App | EShop Mobile (Expo SDK 54) chạy trong **Expo Go**, commit SUT `85af3ba`; `API_URL` trỏ IP LAN của laptop chạy backend |
| Mạng | Laptop và điện thoại chung Wi-Fi; kiểm tra trước bằng 1 lần đăng nhập thử |
| Ghi hình | Quay màn hình điện thoại (trình quay màn hình Android) + ghi âm nếu được đồng ý; không quay mặt |
| Dữ liệu | Phiếu thông tin thử nghiệm (họ tên, SĐT, địa chỉ giả), không dùng thông tin thật của người tham gia |

## 7. Vai trò người điều phối

Sinh viên Trần Thanh An (23120017) vừa là người điều phối vừa là người ghi chú. Nhiệm vụ: đọc lời mở đầu, đưa kịch bản, quan sát trung lập, bấm giờ, ghi phiếu quan sát, phát phiếu SUS và hỏi câu hỏi mở. Không giải thích giao diện trong khi người tham gia đang làm.

## 8. Số đo

| Loại | Số đo | Cách thu |
|---|---|---|
| Hiệu quả | Tỉ lệ hoàn thành mỗi tác vụ: tự hoàn thành / hoàn thành có trợ giúp / thất bại | Phiếu quan sát + kiểm DB |
| Hiệu suất | Thời gian làm mỗi tác vụ (từ khi đọc xong kịch bản đến khi đạt tiêu chí) | Đồng hồ + mốc thời gian video |
| Lỗi | Số lỗi (thao tác dẫn tới thông báo lỗi), số lần đi sai đường, số lần do dự > 5 giây | Phiếu quan sát |
| Trợ giúp | Số lần người điều phối phải can thiệp | Phiếu quan sát |
| Hài lòng | **SUS** 10 câu (thang 1–5), quy đổi 0–100; so với mốc 68 | Phiếu SUS ([03-instruments.md](03-instruments.md)) |
| Định tính | Trích lời nói, câu trả lời câu hỏi mở về độ rõ ràng, sửa lỗi, tốc độ, độ tin cậy | Ghi âm + ghi chú |

Cách tính SUS: câu lẻ (điểm − 1), câu chẵn (5 − điểm), cộng 10 câu rồi × 2.5. Báo cáo trung bình, trung vị, min, max, độ lệch chuẩn của 7 người. File tính sẵn công thức: [23120017_HW03_SUS.xlsx](23120017_HW03_SUS.xlsx).

## 9. Nội dung báo cáo

1. Tóm tắt kết quả và điểm SUS trung bình.
2. Bảng kết quả từng tác vụ × 7 người (hoàn thành, thời gian, lỗi, trợ giúp).
3. Tổng hợp pain point: vấn đề · phiên gặp · số người gặp · trích lời nói.
4. Tách **bug** (sai đặc tả, báo lên GitHub Issues với label `task: T2 usability`) và **vấn đề thiết kế** (chỉ ghi trong báo cáo).
5. Xếp mức độ theo thang Nielsen 0–4 (nghiêm trọng × tần suất), blocker trước.
6. Khuyến nghị có ưu tiên, trả lời Q1–Q6 ở mục 2.
