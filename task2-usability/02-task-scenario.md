# Task 2 · Phase 1: Kịch bản tác vụ (FL-10 Mobile)

Luồng FL-10: **Đăng ký → Đăng nhập → Cập nhật hồ sơ** (FR-01, FR-02, FR-04). Kịch bản viết theo **mục tiêu**, không chỉ từng bước.

## 1. Kịch bản đọc cho người tham gia

> Bạn vừa nghe bạn bè giới thiệu ứng dụng mua sắm EShop và muốn thử mua một món đồ vào tuần sau. Trước khi mua, bạn muốn **có một tài khoản của riêng mình** và **lưu sẵn số điện thoại cùng địa chỉ nhận hàng** để lần sau không phải nhập lại.
>
> Hãy dùng ứng dụng trên điện thoại này để làm việc đó. Thông tin cá nhân hãy dùng **phiếu thông tin thử nghiệm** bên dưới, không dùng thông tin thật của bạn. Mật khẩu bạn tự đặt, nhưng **đừng dùng mật khẩu thật** mà bạn đang dùng ở nơi khác.
>
> Trong lúc làm, hãy nói to những gì bạn đang nghĩ. Khi bạn thấy mình đã xong, hãy nói "Xong".

Kịch bản được đọc theo 3 phần nối tiếp để đo riêng từng tác vụ:

| Tác vụ | Câu đưa cho người tham gia | Không nói ra |
|---|---|---|
| T1 Đăng ký | "Hãy tạo cho mình một tài khoản EShop." | Vị trí nút đăng ký, quy tắc mật khẩu |
| T2 Đăng nhập | "Bây giờ hãy vào tài khoản bạn vừa tạo." | Ô nào là email |
| T3 Cập nhật hồ sơ | "Hãy lưu số điện thoại và địa chỉ nhận hàng trong phiếu vào tài khoản, để lần sau mua hàng không phải nhập lại." | Tên màn "Hồ sơ", nút "Cập nhật" |

## 2. Phiếu thông tin thử nghiệm (đưa cho người tham gia)

| Thông tin | Giá trị |
|---|---|
| Họ tên | Nguyễn Thị Thử |
| Email | `p<số phiên>.hw03@test.local` (ví dụ P3 dùng `p3.hw03@test.local`) |
| Mật khẩu | Tự đặt (không dùng mật khẩu thật) |
| Số điện thoại | 0912 345 678 |
| Địa chỉ nhận hàng | 227 Nguyễn Văn Cừ, Phường 4, Quận 5, TP.HCM |

## 3. Trạng thái ban đầu, tiêu chí thành công, benchmark

| Tác vụ | Trạng thái ban đầu | Tiêu chí thành công (kiểm bằng giao diện + DB) | Benchmark | Dừng/hỗ trợ khi |
|---|---|---|---|---|
| T1 | DB vừa reset; app mở ở trang chủ, chưa đăng nhập; email `pN.hw03@test.local` chưa tồn tại | Bảng `users` có email `pN.hw03@test.local`; người tham gia đang ở màn Đăng nhập | ≤ 2 phút | Bế tắc > 2 phút hoặc xin bỏ cuộc |
| T2 | Ngay sau T1 | Đăng nhập được, thấy trạng thái đã đăng nhập (vào được Hồ sơ) | ≤ 45 giây | Bị khóa tạm 30 giây (FR-02) → ghi lại, chờ hết khóa |
| T3 | Đã đăng nhập, đang ở trang bất kỳ | Bảng `users` của tài khoản có `phone` = 0912345678 và `shipping_address` khớp phiếu; người tham gia biết là đã lưu | ≤ 2 phút | Bế tắc > 2 phút; nếu số điện thoại bị từ chối (Q5) thì ghi lại cách người tham gia xử lý rồi mới hỗ trợ |

## 4. Lưu ý cho người điều phối

- Không đọc to tên nút, tên màn hình; nếu người tham gia hỏi "bấm đâu?" thì hỏi lại "Bạn nghĩ nên bấm đâu?".
- Mốc thời gian: bắt đầu khi đọc xong câu tác vụ, kết thúc khi đạt tiêu chí hoặc người tham gia nói "Xong" (nếu nói "Xong" mà chưa đạt tiêu chí thì ghi là **tưởng đã xong**).
- Giữ nguyên kịch bản cho cả 7 phiên; mọi thay đổi sau pilot ghi vào bảng dưới.

## 5. Thay đổi sau pilot

| # | Thay đổi | Lý do (quan sát ở pilot) |
|---|---|---|
| | *(chưa chạy pilot)* | |
