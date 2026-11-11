# Task 3: Cross-Browser / Cross-Platform

Chạy lại **đúng 72 mục checklist của Task 1** (A-05 Mã giảm giá, A-02 Dashboard, A-03 Danh mục của Web Admin) trên 3 nền tảng, cùng script kiểm thử và cùng dữ liệu (reset DB trước mỗi mục cần dữ liệu sạch).

## 1. Nền tảng và cách chạy

| Nền tảng | Trình duyệt / OS / thiết bị (lấy từ trình duyệt khi chạy) | Công cụ | Thời điểm chạy (UTC+7) | Ảnh |
|---|---|---|---|---|
| Chrome (Windows) | Google Chrome 157.0.8103.39 · Windows 11 Home · cửa sổ 1366×768 | Playwright điều khiển Google Chrome đã cài trên máy | 2026-11-11 10:31 | [chrome/screenshots/](chrome/screenshots/) (50 ảnh) |
| Firefox (Windows) | Firefox 132.0 (Gecko, Playwright build) · Windows 11 Home · cửa sổ 1366×768 | Playwright Firefox (bản Gecko do Playwright đóng gói) | 2026-11-11 10:34 | [firefox/screenshots/](firefox/screenshots/) (50 ảnh) |
| Android Chrome (Pixel 6) | Android Chrome 145.0.0.0 · Android 17 · Pixel 6 (Android Emulator, sdk_gphone64_x86_64) | Máy ảo Android (Android Studio Emulator, AVD Pixel_6) + Playwright Android (adb), `adb reverse` cổng 5174 và 3000 | 2026-11-11 10:44 | [android/screenshots/](android/screenshots/) (47 ảnh) |

- **Không dùng BrowserStack/LambdaTest**: đề bài cho phép thiết bị thật thay thế; ở đây dùng 2 trình duyệt thật trên Windows và máy ảo Android chạy Chrome Android thật. Không có Safari (không có máy macOS/iOS); Android Chrome thay cho Safari theo đề bài §6.
- **Lớp chữ đè** trên mọi ảnh (góc trên bên phải): MSSV · họ tên · email sinh viên, tên trình duyệt + phiên bản + OS/thiết bị, và URL localhost đang mở. Ảnh Android chụp toàn màn hình thiết bị nên thấy cả thanh địa chỉ Chrome `localhost:5174`.
- Chỉ chụp ảnh cho mục **Failed** (giống Task 1). Mục **N/A** là mục không áp dụng được trên nền tảng đó (lý do ở bảng 4).

## 2. Tổng kết

| Nền tảng | Passed | Failed | N/A | Tổng |
|---|---|---|---|---|
| Chrome (Windows) | 24 | 48 | 0 | 72 |
| Firefox (Windows) | 24 | 48 | 0 | 72 |
| Android Chrome (Pixel 6) | 21 | 46 | 5 | 72 |

## 3. Khác biệt giữa các nền tảng

| ID | Mục | Chrome (Windows) | Firefox (Windows) | Android Chrome (Pixel 6) | Nhận xét |
|---|---|---|---|---|---|
| CL-12 | Các ô nhập cùng chiều rộng và thẳng hàng theo lưới | Passed | Passed | **Failed** [ảnh](android/screenshots/CL-12.png) | 6 ô nhập của form A-05 bị ép còn 18px (1 ô ngày 160px) do lưới 3 cột nằm trong vùng nội dung 155px; không nhập/đọc được giá trị |
| CL-17 | Bố cục không vỡ, không bị cắt ở độ phân giải 1920×1080, 1366×768 và 1024×768 | Passed | Passed | **Failed** [ảnh](android/screenshots/CL-17.png) | Màn hình điện thoại 411×785 CSS px: sidebar cố định w-64 (256px) chiếm 62% chiều ngang, vùng nội dung còn 155px; tiêu đề màn hình vỡ thành 4 dòng, ô nhập form chỉ rộng 18px (CL-12), bảng tràn ngang. Trên thiết bị không đổi được độ phân giải nên mục này đánh giá ở kích thước thật của điện thoại |

**Nhận xét:**
- Chrome và Firefox trên Windows cho kết quả **giống hệt nhau** ở cả 72 mục, và trùng với lần chạy Task 1. Các lỗi của Task 1 nằm ở mã nguồn React/Tailwind (thiếu `label`, `required`, `min`, `alert()`, `<li onClick>`...), không phụ thuộc engine trình duyệt. Khác biệt chỉ ở hình thức hiển thị không làm đổi kết quả: Firefox vẽ nút tăng/giảm trong ô số và hiển thị ô ngày dạng `31 / 12 / 2099`.
- Trên **Android Chrome**, Admin **không có bố cục cho màn hình nhỏ**: sidebar `w-64` cố định chiếm 256/411px, form 3 cột bị ép làm ô nhập chỉ còn 18px, không nhập được. Đây là lỗi chỉ xuất hiện trên điện thoại (CL-12, CL-17) → báo issue riêng với label `task: T3 cross-platform` (mục 5).
- Các lỗi còn lại xuất hiện trên cả 3 nền tảng nên không tạo issue mới (đã có issue Task 1 #68 → #102).

## 4. Mục không áp dụng (N/A)

| ID | Mục | Nền tảng | Lý do |
|---|---|---|---|
| CL-18 | Phóng to 200% vẫn đọc được và dùng được mọi chức năng | Android Chrome (Pixel 6) | Không áp dụng: không giả lập được mức phóng to trình duyệt trên Chrome Android qua Playwright. Ở kích thước thật của điện thoại, form đã không dùng được (CL-12, CL-17) |
| CL-19 | Phóng to 400% (rộng 320 CSS px) nội dung dàn lại, không phải cuộn 2 chiều | Android Chrome (Pixel 6) | Không áp dụng: không đổi được bề rộng viewport trên thiết bị. Ở bề rộng thật 411px bố cục cũng không dàn lại (CL-17) |
| CL-20 | Khi bật Dark mode, giao diện vẫn đọc được (không trộn nền tối với chữ tối) | Android Chrome (Pixel 6) | Không áp dụng: Playwright Android không tạo được context với colorScheme riêng; Admin không có chế độ tối riêng |
| CL-55 | Mục sidebar đổi màu khi rê chuột và hiện con trỏ bàn tay | Android Chrome (Pixel 6) | Không áp dụng: màn hình cảm ứng không có trạng thái rê chuột (hover) |
| CL-72 | Nút có phản hồi khi rê chuột (đổi màu nền) | Android Chrome (Pixel 6) | Không áp dụng: màn hình cảm ứng không có trạng thái rê chuột (hover) |

Ngoài ra, trên Android, 2 mục CL-48 và CL-59 lần chạy đầu bị lỗi script (bấm vào tọa độ ngoài màn hình 411px; khung chú thích che nút Xóa). Script được sửa riêng cho Android và chạy lại 2 mục này: kết quả Failed giống desktop. 14 ảnh đầu tiên của Android bị tooltip của Chrome ("Review your inactive tabs") che lớp chữ đè nên được chạy lại để chụp ảnh sạch.

## 5. Bug chỉ xuất hiện trên một số nền tảng

| Bug | Severity | Nền tảng | Tiêu đề issue | Mục | Issue # |
|---|---|---|---|---|---|
| T3-BUG-01 | High | Android Chrome | `[23120017][T3][A-02, A-03, A-05][Android Chrome] Admin không có bố cục cho điện thoại: sidebar chiếm 62% màn hình, ô nhập form chỉ rộng 18px` | CL-12, CL-17 | [#103](https://github.com/angquoc/software-testing-2026-HW03-group/issues/103) |

- **Các bước:** Trên điện thoại Android (Pixel 6, Chrome 145) mở `http://localhost:5174`, đăng nhập admin, chọn Mã Giảm Giá.
- **Mong đợi:** FR-21/IA-01 hiển thị đúng ở các kích thước màn hình; form dùng được (ô nhập đủ rộng để đọc giá trị), sidebar thu gọn thành menu.
- **Thực tế:** Sidebar 256px cố định, vùng nội dung 155px; tiêu đề vỡ 4 dòng; 5/6 ô nhập rộng 18px nên không thấy giá trị; bảng tràn ngang. Trên Chrome/Firefox Windows 1366×768 hai mục này Passed.
- **Severity High:** Quản trị viên không có cách nào dùng form tạo mã trên điện thoại (không có chế độ xem khác). Related #84 (BUG-18: phóng to 400% không dàn lại bố cục, cùng nguyên nhân thiếu responsive).
- **Ảnh:** [android/screenshots/CL-17.png](android/screenshots/CL-17.png), [android/screenshots/CL-12.png](android/screenshots/CL-12.png)

## 6. Bảng đầy đủ 72 mục × 3 nền tảng

| ID | IA | Mục kiểm tra | Chrome (Windows) | Firefox (Windows) | Android Chrome (Pixel 6) |
|---|---|---|---|---|---|
| CL-01 | IA-01 | Nhãn, tiêu đề, cột bảng, nút dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn) | **Failed** [ảnh](chrome/screenshots/CL-01.png) | **Failed** [ảnh](firefox/screenshots/CL-01.png) | **Failed** [ảnh](android/screenshots/CL-01.png) |
| CL-02 | IA-01 | Nút hành động tích cực "Tạo mã" dùng màu xanh dương | **Failed** [ảnh](chrome/screenshots/CL-02.png) | **Failed** [ảnh](firefox/screenshots/CL-02.png) | **Failed** [ảnh](android/screenshots/CL-02.png) |
| CL-03 | IA-01 | Nút hành động tích cực "Thêm mới" dùng màu xanh dương | Passed | Passed | Passed |
| CL-04 | IA-01 | Nút hành động nguy hiểm "Xóa" dùng màu đỏ | Passed | Passed | Passed |
| CL-05 | IA-01 | Số tiền hiển thị ký hiệu ₫ và phân cách hàng nghìn | Passed | Passed | Passed |
| CL-06 | IA-01 | Định dạng số tiền cố định, không thay đổi theo ngôn ngữ của trình duyệt | **Failed** [ảnh](chrome/screenshots/CL-06.png) | **Failed** [ảnh](firefox/screenshots/CL-06.png) | **Failed** [ảnh](android/screenshots/CL-69.png) |
| CL-07 | IA-01 | Tổng doanh thu hiển thị ký hiệu ₫ và phân cách hàng nghìn | Passed | Passed | Passed |
| CL-08 | IA-01 | Mỗi màn hình có đúng 1 thẻ <h1> và h1 mô tả nội dung màn hình đó | **Failed** [ảnh](chrome/screenshots/CL-08.png) | **Failed** [ảnh](firefox/screenshots/CL-08.png) | **Failed** [ảnh](android/screenshots/CL-08.png) |
| CL-09 | IA-01 | Tiêu đề tab trình duyệt mô tả ứng dụng và màn hình đang xem | **Failed** [ảnh](chrome/screenshots/CL-09.png) | **Failed** [ảnh](firefox/screenshots/CL-09.png) | **Failed** [ảnh](android/screenshots/CL-09.png) |
| CL-10 | IA-01 | Ngôn ngữ trang khai báo đúng tiếng Việt (lang="vi") | **Failed** [ảnh](chrome/screenshots/CL-10.png) | **Failed** [ảnh](firefox/screenshots/CL-10.png) | **Failed** [ảnh](android/screenshots/CL-10.png) |
| CL-11 | IA-01 | Phông chữ và cỡ chữ tiêu đề màn hình nhất quán giữa các màn hình | Passed | Passed | Passed |
| CL-12 | IA-01 | Các ô nhập cùng chiều rộng và thẳng hàng theo lưới | Passed | Passed | **Failed** [ảnh](android/screenshots/CL-12.png) |
| CL-13 | IA-01 | Định dạng ngày nhất quán giữa ô nhập và bảng | **Failed** [ảnh](chrome/screenshots/CL-13.png) | **Failed** [ảnh](firefox/screenshots/CL-13.png) | **Failed** [ảnh](android/screenshots/CL-13.png) |
| CL-14 | IA-01 | Mã đã hết hạn vẫn cho biết ngày hết hạn | **Failed** [ảnh](chrome/screenshots/CL-14.png) | **Failed** [ảnh](firefox/screenshots/CL-14.png) | **Failed** [ảnh](android/screenshots/CL-14.png) |
| CL-15 | IA-01 | Quy ước viết hoa nhất quán (viết hoa chữ đầu câu) | **Failed** [ảnh](chrome/screenshots/CL-15.png) | **Failed** [ảnh](firefox/screenshots/CL-15.png) | **Failed** [ảnh](android/screenshots/CL-15.png) |
| CL-16 | IA-01 | Văn bản đạt tỉ lệ tương phản tối thiểu 4.5:1 (chữ lớn 3:1) | **Failed** [ảnh](chrome/screenshots/CL-16.png) | **Failed** [ảnh](firefox/screenshots/CL-16.png) | **Failed** [ảnh](android/screenshots/CL-16.png) |
| CL-17 | IA-01 | Bố cục không vỡ, không bị cắt ở độ phân giải 1920×1080, 1366×768 và 1024×768 | Passed | Passed | **Failed** [ảnh](android/screenshots/CL-17.png) |
| CL-18 | IA-01 | Phóng to 200% vẫn đọc được và dùng được mọi chức năng | **Failed** [ảnh](chrome/screenshots/CL-18.png) | **Failed** [ảnh](firefox/screenshots/CL-18.png) | N/A |
| CL-19 | IA-01 | Phóng to 400% (rộng 320 CSS px) nội dung dàn lại, không phải cuộn 2 chiều | **Failed** [ảnh](chrome/screenshots/CL-19.png) | **Failed** [ảnh](firefox/screenshots/CL-19.png) | N/A |
| CL-20 | IA-01 | Khi bật Dark mode, giao diện vẫn đọc được (không trộn nền tối với chữ tối) | Passed | Passed | N/A |
| CL-21 | IA-01 | Mã coupon dài (300 ký tự, ô Mã cho phép nhập) hiển thị không làm vỡ bảng | **Failed** [ảnh](chrome/screenshots/CL-21.png) | **Failed** [ảnh](firefox/screenshots/CL-21.png) | **Failed** [ảnh](android/screenshots/CL-21.png) |
| CL-22 | IA-01 | Thứ tự focus theo phím Tab đi từ trên xuống dưới, trái sang phải | Passed | Passed | Passed |
| CL-23 | IA-01 | Nút Xóa có tên truy cập phân biệt (trình đọc màn hình biết xóa mục nào) | **Failed** [ảnh](chrome/screenshots/CL-23.png) | **Failed** [ảnh](firefox/screenshots/CL-23.png) | **Failed** [ảnh](android/screenshots/CL-23.png) |
| CL-24 | IA-02 | Mỗi ô nhập có nhãn (label) hiển thị cố định, gắn với ô | **Failed** [ảnh](chrome/screenshots/CL-24.png) | **Failed** [ảnh](firefox/screenshots/CL-24.png) | **Failed** [ảnh](android/screenshots/CL-24.png) |
| CL-25 | IA-02 | Ô có giá trị mặc định vẫn cho biết ý nghĩa của ô | **Failed** [ảnh](chrome/screenshots/CL-25.png) | **Failed** [ảnh](firefox/screenshots/CL-25.png) | **Failed** [ảnh](android/screenshots/CL-25.png) |
| CL-26 | IA-02 | Trường bắt buộc có ký hiệu * bên cạnh nhãn | **Failed** [ảnh](chrome/screenshots/CL-26.png) | **Failed** [ảnh](firefox/screenshots/CL-26.png) | **Failed** [ảnh](android/screenshots/CL-26.png) |
| CL-27 | IA-02 | Để trống trường bắt buộc theo FR-17 thì không tạo được mã | **Failed** [ảnh](chrome/screenshots/CL-27.png) | **Failed** [ảnh](firefox/screenshots/CL-27.png) | **Failed** [ảnh](android/screenshots/CL-27.png) |
| CL-28 | IA-02 | Không thêm được danh mục khi tên để trống hoặc chỉ có khoảng trắng | **Failed** [ảnh](chrome/screenshots/CL-28.png) | **Failed** [ảnh](firefox/screenshots/CL-28.png) | **Failed** [ảnh](android/screenshots/CL-28.png) |
| CL-29 | IA-02 | Mã chỉ gồm khoảng trắng bị từ chối | **Failed** [ảnh](chrome/screenshots/CL-29.png) | **Failed** [ảnh](firefox/screenshots/CL-29.png) | **Failed** [ảnh](android/screenshots/CL-29.png) |
| CL-30 | IA-02 | Mã tự chuyển thành chữ IN HOA khi gõ | Passed | Passed | Passed |
| CL-31 | IA-02 | Ô Mã có giới hạn số ký tự tối đa | **Failed** [ảnh](chrome/screenshots/CL-31.png) | **Failed** [ảnh](firefox/screenshots/CL-31.png) | **Failed** [ảnh](android/screenshots/CL-31.png) |
| CL-32 | IA-02 | Giá trị giảm âm bị chặn | **Failed** [ảnh](chrome/screenshots/CL-32.png) | **Failed** [ảnh](firefox/screenshots/CL-32.png) | **Failed** [ảnh](android/screenshots/CL-32.png) |
| CL-33 | IA-02 | Giá trị giảm bằng 0 bị chặn | **Failed** [ảnh](chrome/screenshots/CL-33.png) | **Failed** [ảnh](firefox/screenshots/CL-33.png) | **Failed** [ảnh](android/screenshots/CL-33.png) |
| CL-34 | IA-02 | Loại Phần trăm không cho giá trị lớn hơn 100 | **Failed** [ảnh](chrome/screenshots/CL-34.png) | **Failed** [ảnh](firefox/screenshots/CL-34.png) | **Failed** [ảnh](android/screenshots/CL-34.png) |
| CL-35 | IA-02 | Đơn tối thiểu âm bị chặn | **Failed** [ảnh](chrome/screenshots/CL-35.png) | **Failed** [ảnh](firefox/screenshots/CL-35.png) | **Failed** [ảnh](android/screenshots/CL-35.png) |
| CL-36 | IA-02 | Số lần dùng tối đa nhỏ hơn 1 bị chặn | Passed | Passed | Passed |
| CL-37 | IA-02 | Không tạo được mã có ngày hết hạn trong quá khứ | **Failed** [ảnh](chrome/screenshots/CL-37.png) | **Failed** [ảnh](firefox/screenshots/CL-37.png) | **Failed** [ảnh](android/screenshots/CL-37.png) |
| CL-38 | IA-02 | Ô ngày không nhận ngày không tồn tại (31/02) | Passed | Passed | Passed |
| CL-39 | IA-02 | Dropdown Loại có giá trị mặc định và đủ lựa chọn, nhãn tiếng Việt | Passed | Passed | Passed |
| CL-40 | IA-02 | Gợi ý của ô Giá trị đổi theo Loại đã chọn | Passed | Passed | Passed |
| CL-41 | IA-02 | Thông báo lỗi xuất hiện ngay trên nút submit (không phải hộp thoại bật lên) | **Failed** [ảnh](chrome/screenshots/CL-41.png) | **Failed** [ảnh](firefox/screenshots/CL-41.png) | **Failed** [ảnh](android/screenshots/CL-41.png) |
| CL-42 | IA-02 | Nhấn Enter trong ô cuối cùng sẽ gửi form | Passed | Passed | Passed |
| CL-43 | IA-02 | Sau khi tạo thành công, form trở về giá trị mặc định | Passed | Passed | Passed |
| CL-44 | IA-02 | Nhấp đúp nút gửi không tạo bản ghi trùng hoặc lỗi giả | **Failed** [ảnh](chrome/screenshots/CL-44.png) | **Failed** [ảnh](firefox/screenshots/CL-44.png) | **Failed** [ảnh](android/screenshots/CL-44.png) |
| CL-45 | IA-02 | Tên có ký tự HTML hiển thị nguyên văn, không bị diễn giải | Passed | Passed | Passed |
| CL-46 | IA-03 | Sidebar làm nổi bật mục đang được chọn | Passed | Passed | Passed |
| CL-47 | IA-03 | Mục đang chọn được phân biệt không chỉ bằng màu sắc | **Failed** [ảnh](chrome/screenshots/CL-47.png) | **Failed** [ảnh](firefox/screenshots/CL-47.png) | **Failed** [ảnh](android/screenshots/CL-47.png) |
| CL-48 | IA-03 | Có thể chuyển màn hình bằng bàn phím (Tab đến mục sidebar, Enter để mở) | **Failed** [ảnh](chrome/screenshots/CL-48.png) | **Failed** [ảnh](firefox/screenshots/CL-48.png) | **Failed** [ảnh](android/screenshots/CL-48.png) |
| CL-49 | IA-03 | Sidebar dùng phần tử điều hướng ngữ nghĩa cho trình đọc màn hình | **Failed** [ảnh](chrome/screenshots/CL-49.png) | **Failed** [ảnh](firefox/screenshots/CL-49.png) | **Failed** [ảnh](android/screenshots/CL-49.png) |
| CL-50 | IA-03 | Nút đăng xuất có nhãn "Đăng xuất" (không phải "Thoát") | Passed | Passed | Passed |
| CL-51 | IA-03 | Đăng xuất tách biệt khỏi các mục điều hướng | **Failed** [ảnh](chrome/screenshots/CL-51.png) | **Failed** [ảnh](firefox/screenshots/CL-51.png) | **Failed** [ảnh](android/screenshots/CL-51.png) |
| CL-52 | IA-03 | Tải lại trang (F5) vẫn giữ màn hình đang xem | **Failed** [ảnh](chrome/screenshots/CL-52.png) | **Failed** [ảnh](firefox/screenshots/CL-52.png) | **Failed** [ảnh](android/screenshots/CL-52.png) |
| CL-53 | IA-03 | Nút Back của trình duyệt quay lại màn hình trước trong Admin | **Failed** [ảnh](chrome/screenshots/CL-53.png) | **Failed** [ảnh](firefox/screenshots/CL-53.png) | **Failed** [ảnh](android/screenshots/CL-53.png) |
| CL-54 | IA-03 | Tiêu đề màn hình khớp với tên mục đã chọn trên sidebar | Passed | Passed | Passed |
| CL-55 | IA-03 | Mục sidebar đổi màu khi rê chuột và hiện con trỏ bàn tay | **Failed** [ảnh](chrome/screenshots/CL-55.png) | **Failed** [ảnh](firefox/screenshots/CL-55.png) | N/A |
| CL-56 | IA-03 | Phần tử đang được focus có viền focus nhìn thấy rõ | Passed | Passed | Passed |
| CL-57 | IA-04 | Tạo mã thành công có thông báo xác nhận | **Failed** [ảnh](chrome/screenshots/CL-57.png) | **Failed** [ảnh](firefox/screenshots/CL-57.png) | **Failed** [ảnh](android/screenshots/CL-57.png) |
| CL-58 | IA-04 | Thêm danh mục thành công có thông báo xác nhận | **Failed** [ảnh](chrome/screenshots/CL-58.png) | **Failed** [ảnh](firefox/screenshots/CL-58.png) | **Failed** [ảnh](android/screenshots/CL-58.png) |
| CL-59 | IA-04 | Xóa mã giảm giá có hộp thoại xác nhận | **Failed** [ảnh1](chrome/screenshots/CL-59-truoc.png) [ảnh2](chrome/screenshots/CL-59.png) | **Failed** [ảnh1](firefox/screenshots/CL-59-truoc.png) [ảnh2](firefox/screenshots/CL-59.png) | **Failed** [ảnh1](android/screenshots/CL-59-truoc.png) [ảnh2](android/screenshots/CL-59.png) |
| CL-60 | IA-04 | Xóa danh mục có hộp thoại xác nhận | **Failed** [ảnh1](chrome/screenshots/CL-60-truoc.png) [ảnh2](chrome/screenshots/CL-60.png) | **Failed** [ảnh1](firefox/screenshots/CL-60-truoc.png) [ảnh2](firefox/screenshots/CL-60.png) | **Failed** [ảnh1](android/screenshots/CL-60-truoc.png) [ảnh2](android/screenshots/CL-60.png) |
| CL-61 | IA-04 | Xóa danh mục đang có sản phẩm thì được cảnh báo | **Failed** [ảnh](chrome/screenshots/CL-61.png) | **Failed** [ảnh](firefox/screenshots/CL-61.png) | **Failed** [ảnh](android/screenshots/CL-61.png) |
| CL-62 | IA-04 | Tạo mã trùng báo lỗi bằng tiếng Việt, dễ hiểu, không lộ lỗi kỹ thuật | **Failed** [ảnh](chrome/screenshots/CL-62.png) | **Failed** [ảnh](firefox/screenshots/CL-62.png) | **Failed** [ảnh](android/screenshots/CL-62.png) |
| CL-63 | IA-04 | Mã đã hết hạn được đánh dấu khác biệt | Passed | Passed | Passed |
| CL-64 | IA-04 | Có trạng thái đang tải (loading) khi dữ liệu chưa về | **Failed** [ảnh](chrome/screenshots/CL-64.png) | **Failed** [ảnh](firefox/screenshots/CL-64.png) | **Failed** [ảnh](android/screenshots/CL-64.png) |
| CL-65 | IA-04 | Nút gửi chuyển sang trạng thái đang xử lý (vô hiệu/"Đang tạo...") trong lúc chờ | **Failed** [ảnh](chrome/screenshots/CL-65.png) | **Failed** [ảnh](firefox/screenshots/CL-65.png) | **Failed** [ảnh](android/screenshots/CL-65.png) |
| CL-66 | IA-04 | Bảng trống hiển thị empty state có icon/hình minh họa và lời nhắn thân thiện | **Failed** [ảnh](chrome/screenshots/CL-66.png) | **Failed** [ảnh](firefox/screenshots/CL-66.png) | **Failed** [ảnh](android/screenshots/CL-66.png) |
| CL-67 | IA-04 | Mất kết nối backend thì hiển thị thông báo lỗi | **Failed** [ảnh](chrome/screenshots/CL-67.png) | **Failed** [ảnh](firefox/screenshots/CL-67.png) | **Failed** [ảnh](android/screenshots/CL-67.png) |
| CL-68 | IA-04 | Phiên hết hạn/token không hợp lệ thì báo cho người dùng trước khi về trang đăng nhập | **Failed** [ảnh](chrome/screenshots/CL-68.png) | **Failed** [ảnh](firefox/screenshots/CL-68.png) | **Failed** [ảnh](android/screenshots/CL-68.png) |
| CL-69 | IA-04 | Tổng doanh thu bằng tổng tiền các đơn đã giao (delivered) | **Failed** [ảnh](chrome/screenshots/CL-69.png) | **Failed** [ảnh](firefox/screenshots/CL-69.png) | **Failed** [ảnh](android/screenshots/CL-69.png) |
| CL-70 | IA-04 | Tổng số đơn hàng khớp số đơn thực tế | Passed | Passed | Passed |
| CL-71 | IA-04 | Bảng cập nhật ngay sau khi thêm/xóa, không cần tải lại trang | Passed | Passed | Passed |
| CL-72 | IA-04 | Nút có phản hồi khi rê chuột (đổi màu nền) | **Failed** [ảnh](chrome/screenshots/CL-72.png) | **Failed** [ảnh](firefox/screenshots/CL-72.png) | N/A |

Ghi chú lý do Failed của từng mục giống Task 1 (báo cáo chính mục 1.6) trừ các mục ở bảng 3, 4. Kết quả chi tiết (kèm ghi chú từng nền tảng) ở sheet **Task 3** của file Excel.
