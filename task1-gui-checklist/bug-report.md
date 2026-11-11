# Task 1: Bug report

- Nguồn: 48 mục Failed ở [báo cáo chính, mục 1.6](../23120017_HW03_Report.md), gom thành **36 bug** (các mục cùng nguyên nhân, cùng màn hình gộp chung 1 bug)
- Nơi báo: GitHub Issues của repo nhóm `angquoc/software-testing-2026-HW03-group`, dùng template "Bug report"; mỗi bug = 1 issue, kèm ảnh trong thư mục [screenshots/](screenshots/)
- Môi trường chung: Google Chrome 157.0.8103.39, Windows 11, ngôn ngữ vi-VN, cửa sổ 1366×768; EShop commit `85af3ba`
- Severity theo thang của nhóm (README repo nhóm mục 4.3), tính bằng mức nghiêm trọng cao nhất trong các mục checklist của bug (bảng quy đổi ở sheet Thông tin của file Excel). Label chung cho mọi issue: `bug`, `platform: admin`, `task: T1 checklist`

## 1. Danh sách

| Bug | Severity | Màn hình | Tiêu đề | Mục checklist | IA | Issue # |
|---|---|---|---|---|---|---|
| BUG-01 | High | A-02 | Dashboard: Tổng doanh thu bị nhân đôi so với tổng tiền các đơn đã giao | CL-69 | IA-04 | |
| BUG-02 | High | A-05 | Form Tạo mã giảm giá: Các ô số không kiểm tra miền giá trị (âm, 0, phần trăm > 100, đơn tối thiểu âm) | CL-32, CL-33, CL-34, CL-35 | IA-02 | |
| BUG-03 | High | A-03 | Xóa danh mục đang có sản phẩm không cảnh báo, sản phẩm bị mồ côi | CL-61 | IA-04 | |
| BUG-04 | High | A-02/A-03/A-05 | Sidebar không dùng được bằng bàn phím và không có ngữ nghĩa điều hướng | CL-48, CL-49 | IA-03 | |
| BUG-05 | Medium | A-03/A-05 | Xóa mã giảm giá và xóa danh mục không có hộp thoại xác nhận | CL-59, CL-60 | IA-04 | |
| BUG-06 | Medium | A-03 | Thêm được danh mục không có tên (để trống hoặc chỉ khoảng trắng) | CL-28 | IA-02 | |
| BUG-07 | Medium | A-05 | Form Tạo mã giảm giá: Tạo được mã khi bỏ trống Đơn tối thiểu và Số lần dùng tối đa | CL-27 | IA-02 | |
| BUG-08 | Medium | A-05 | Form Tạo mã giảm giá: Tạo được mã chỉ gồm khoảng trắng | CL-29 | IA-02 | |
| BUG-09 | Medium | A-03/A-05 | Nhấp đúp nút gửi tạo danh mục trùng / báo lỗi giả; nút không có trạng thái đang xử lý | CL-44, CL-65 | IA-02, IA-04 | |
| BUG-10 | Medium | A-05 | Tạo mã trùng hiện lỗi SQLite thô bằng tiếng Anh | CL-62 | IA-04, IA-01 | |
| BUG-11 | Medium | A-03/A-05 | Thông báo lỗi hiển thị bằng alert() bật lên, không nằm phía trên nút submit | CL-41 | IA-02 | |
| BUG-12 | Medium | A-02/A-03/A-05 | Tải lại trang (F5) và nút Back làm mất vị trí màn hình | CL-52, CL-53 | IA-03 | |
| BUG-13 | Medium | A-03/A-05 | Tạo mã / thêm danh mục thành công không có thông báo xác nhận | CL-57, CL-58 | IA-04 | |
| BUG-14 | Medium | A-02/A-03/A-05 | Không có trạng thái đang tải khi dữ liệu chưa về | CL-64 | IA-04 | |
| BUG-15 | Medium | A-02/A-03/A-05 | Mất kết nối backend không có thông báo lỗi | CL-67 | IA-04 | |
| BUG-16 | Medium | A-03/A-05 | Form không có nhãn: chú thích chỉ là placeholder, bị che bởi giá trị mặc định và bị cắt khi phóng to | CL-24, CL-25, CL-18 | IA-02 | |
| BUG-17 | Medium | A-03/A-05 | Văn bản không đạt tỉ lệ tương phản 4.5:1 | CL-16 | IA-01 | |
| BUG-18 | Medium | A-02/A-03/A-05 | Phóng to 400% (320 CSS px) không dàn lại bố cục | CL-19 | IA-01 | |
| BUG-19 | Medium | A-02/A-03/A-05 | Mục sidebar đang chọn chỉ được phân biệt bằng màu chữ | CL-47 | IA-03, IA-01 | |
| BUG-20 | Medium | A-03/A-05 | Các nút Xóa cùng tên truy cập "Xóa", trình đọc màn hình không biết xóa mục nào | CL-23 | IA-01 | |
| BUG-21 | Medium | A-05 | Ô Mã coupon không giới hạn độ dài; mã dài làm tràn bảng | CL-31, CL-21 | IA-02, IA-01 | |
| BUG-22 | Medium | A-05 | Cột Hết hạn: mã đã hết hạn bị ẩn ngày hết hạn | CL-14 | IA-01 | |
| BUG-23 | Medium | A-02/A-03/A-05 | Trang khai báo lang="en" cho nội dung tiếng Việt | CL-10 | IA-01 | |
| BUG-24 | Low | A-02/A-03/A-05 | Nút Tạo mã, Thêm mới, Xóa và mục Đăng xuất không đổi màu khi rê chuột | CL-72, CL-55 | IA-04, IA-03 | |
| BUG-25 | Low | A-03/A-05 | Trường bắt buộc không có dấu * | CL-26 | IA-02 | |
| BUG-26 | Low | A-05 | Nút hành động tích cực "Tạo mã" màu cam thay vì xanh dương | CL-02 | IA-01 | |
| BUG-27 | Low | A-02/A-03/A-05 | Thẻ h1 duy nhất là logo "EShop Admin", không mô tả màn hình | CL-08 | IA-01 | |
| BUG-28 | Low | A-02/A-03/A-05 | Tiêu đề tab trình duyệt luôn là "frontend-admin" | CL-09 | IA-01 | |
| BUG-29 | Low | A-02 | Dashboard còn nhãn tiếng Anh "Delivered" | CL-01 | IA-01 | |
| BUG-30 | Low | A-02/A-05 | Định dạng số tiền thay đổi theo ngôn ngữ của trình duyệt | CL-06 | IA-01 | |
| BUG-31 | Low | A-05 | Cột Hết hạn hiển thị ngày dạng yyyy-mm-dd, khác định dạng ô nhập dd/mm/yyyy | CL-13 | IA-01 | |
| BUG-32 | Low | A-02/A-03/A-05 | Viết hoa không nhất quán giữa tiêu đề, menu và cột bảng | CL-15 | IA-01 | |
| BUG-33 | Low | A-05 | Cho tạo mã có ngày hết hạn trong quá khứ mà không cảnh báo | CL-37 | IA-02 | |
| BUG-34 | Low | A-02/A-03/A-05 | Mục "Đăng xuất" không tách khỏi các mục điều hướng (mt-8 bị ghi đè) | CL-51 | IA-03 | |
| BUG-35 | Low | A-02/A-03/A-05 | Token hết hạn/không hợp lệ bị đưa về trang đăng nhập không báo lý do | CL-68 | IA-04 | |
| BUG-36 | Low | A-03/A-05 | Bảng mã giảm giá và bảng danh mục khi trống không có empty state | CL-66 | IA-04 | |

## 2. Chi tiết từng bug (nội dung để điền vào issue)

### BUG-01 · Dashboard: Tổng doanh thu bị nhân đôi so với tổng tiền các đơn đã giao

- **Tiêu đề issue:** `[23120017][T1][A-02][Chrome] Dashboard: Tổng doanh thu bị nhân đôi so với tổng tiền các đơn đã giao`
- **Label:** `bug`, `severity: high`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-69
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768; chưa có đơn nào
- **Các bước tái hiện:**
  1. Đăng nhập `test@eshop.com` / `Test1234!` ở Web, đặt 1 đơn có tổng 500.000 ₫
  2. Ở Admin → Đơn hàng: bấm Xác nhận → Giao hàng → Hoàn thành cho đơn đó
  3. Mở Dashboard, đọc thẻ "Tổng doanh thu (Delivered)"
- **Kết quả mong đợi:** FR-13: tổng doanh thu = tổng `total_amount` của các đơn `delivered` = 500.000 ₫
- **Kết quả thực tế:** Hiển thị 1.000.000 ₫ (gấp đôi). Thẻ "Tổng số đơn hàng" vẫn đúng (1)
- **Ảnh:** [CL-69.png](screenshots/CL-69.png)
- **Lý do severity High:** Sai đặc tả FR-13 ở số liệu chính của Dashboard; quản trị viên không có cách nào xem được doanh thu đúng trên giao diện

### BUG-02 · Form Tạo mã giảm giá: Các ô số không kiểm tra miền giá trị (âm, 0, phần trăm > 100, đơn tối thiểu âm)

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Form Tạo mã giảm giá: Các ô số không kiểm tra miền giá trị (âm, 0, phần trăm > 100, đơn tối thiểu âm)`
- **Label:** `bug`, `severity: high`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-32, CL-33, CL-34, CL-35
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Nhập Mã `AM10`, Loại Phần trăm, Giá trị `-10`, Ngày 31/12/2099 → bấm Tạo mã
  3. Lặp lại với Giá trị `0` (mã KHONG0), Giá trị `150` (mã GIAM150), và Đơn tối thiểu `-1` (mã MINAM)
- **Kết quả mong đợi:** FR-17: `discount_value` dương, `min_order_amount` ≥ 0; loại phần trăm không vượt 100% (theo công thức FR-09). Form chặn và báo lỗi tại ô sai
- **Kết quả thực tế:** Cả 4 mã đều được tạo và hiện trong bảng (-10%, 0%, 150%, đơn tối thiểu -1 ₫). Các ô `type=number` không có `min`/`max`, backend không kiểm tra
- **Ảnh:** [CL-32.png](screenshots/CL-32.png), [CL-33.png](screenshots/CL-33.png), [CL-34.png](screenshots/CL-34.png), [CL-35.png](screenshots/CL-35.png)
- **Lý do severity High:** Mã 150% được tạo im lặng, không cảnh báo; khi khách áp mã, theo công thức FR-09 tổng tiền sau giảm âm (sai tiền thanh toán). Các giá trị -10, 0, -1 riêng lẻ chỉ ở mức Medium
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#55, angquoc/software-testing-2026-HW02-group#56, angquoc/software-testing-2026-HW02-group#63 (HW02 báo ở mức API; issue này nhìn từ form giao diện)

### BUG-03 · Xóa danh mục đang có sản phẩm không cảnh báo, sản phẩm bị mồ côi

- **Tiêu đề issue:** `[23120017][T1][A-03][Chrome] Xóa danh mục đang có sản phẩm không cảnh báo, sản phẩm bị mồ côi`
- **Label:** `bug`, `severity: high`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-61
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768; danh mục "Điện thoại" (id 1) có 2 sản phẩm
- **Các bước tái hiện:**
  1. Mở Danh mục
  2. Bấm Xóa ở dòng "Điện thoại"
- **Kết quả mong đợi:** Cảnh báo "Danh mục còn 2 sản phẩm" hoặc chặn xóa (Nielsen #5: phòng ngừa lỗi)
- **Kết quả thực tế:** Danh mục bị xóa ngay; 2 sản phẩm vẫn mang `category_id = 1` trỏ tới danh mục không còn tồn tại
- **Ảnh:** [CL-61.png](screenshots/CL-61.png)
- **Lý do severity High:** Một cú bấm làm mất liên kết dữ liệu của nhiều sản phẩm, không hoàn tác được trên giao diện (không có cách đi vòng sau khi đã xóa)

### BUG-04 · Sidebar không dùng được bằng bàn phím và không có ngữ nghĩa điều hướng

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Sidebar không dùng được bằng bàn phím và không có ngữ nghĩa điều hướng`
- **Label:** `bug`, `severity: high`, `platform: admin`, `task: T1 checklist`, `ia: IA-03`
- **Mục checklist:** CL-48, CL-49
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Ở Dashboard, nhấn Tab liên tục (25 lần)
  2. Quan sát focus; thử chuyển sang Mã Giảm Giá chỉ bằng bàn phím
  3. Mở DevTools → Elements xem cấu trúc sidebar
- **Kết quả mong đợi:** Mỗi mục sidebar nhận focus bằng Tab và mở bằng Enter (WCAG 2.1.1); sidebar nằm trong `<nav>`, mục là liên kết/nút (WCAG 1.3.1, 4.1.2)
- **Kết quả thực tế:** Focus không lần nào vào sidebar; mỗi mục là `<li onClick>` không có `tabindex`/`role`, không có `<nav>` → người dùng bàn phím không đổi được màn hình, trình đọc màn hình không nhận ra menu. axe-core 4.10.2 báo thêm `landmark-one-main`/`region`: trang không có vùng `<main>`
- **Ảnh:** [CL-48.png](screenshots/CL-48.png), [CL-49.png](screenshots/CL-49.png)
- **Lý do severity High:** Người chỉ dùng bàn phím bị chặn hoàn toàn, không thể mở màn hình Mã Giảm Giá hay Danh mục (WCAG 2.1.1 mức A), không có cách đi vòng

### BUG-05 · Xóa mã giảm giá và xóa danh mục không có hộp thoại xác nhận

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Xóa mã giảm giá và xóa danh mục không có hộp thoại xác nhận`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-59, CL-60
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, bấm Xóa ở một dòng bất kỳ
  2. Mở Danh mục, bấm Xóa ở một dòng bất kỳ
- **Kết quả mong đợi:** Hỏi xác nhận trước khi xóa (Nielsen #5, Shneiderman #6, slide: thao tác không thể hoàn tác phải xác nhận Yes/No). FR-24 chỉ quy định cho việc xóa khỏi giỏ hàng; mục này áp dụng tương tự cho Admin
- **Kết quả thực tế:** Bản ghi bị xóa ngay lập tức, không hỏi lại, không hoàn tác được (xem ảnh trước/sau)
- **Ảnh:** [CL-59-truoc.png](screenshots/CL-59-truoc.png), [CL-59.png](screenshots/CL-59.png), [CL-60-truoc.png](screenshots/CL-60-truoc.png), [CL-60.png](screenshots/CL-60.png)

### BUG-06 · Thêm được danh mục không có tên (để trống hoặc chỉ khoảng trắng)

- **Tiêu đề issue:** `[23120017][T1][A-03][Chrome] Thêm được danh mục không có tên (để trống hoặc chỉ khoảng trắng)`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-28
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Danh mục
  2. Để trống ô "Tên danh mục mới", bấm Thêm mới
  3. Nhập 3 dấu cách, bấm Thêm mới
- **Kết quả mong đợi:** FR-14: tên danh mục bắt buộc, không được để trống → bị chặn và có thông báo
- **Kết quả thực tế:** Thêm được 2 danh mục có cột Tên trống. Ô thiếu `required`, backend không kiểm tra
- **Ảnh:** [CL-28.png](screenshots/CL-28.png)

### BUG-07 · Form Tạo mã giảm giá: Tạo được mã khi bỏ trống Đơn tối thiểu và Số lần dùng tối đa

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Form Tạo mã giảm giá: Tạo được mã khi bỏ trống Đơn tối thiểu và Số lần dùng tối đa`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-27
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Nhập Mã `TRONGMIN`, Giá trị 10, Ngày 31/12/2099
  3. Xóa trắng ô Đơn tối thiểu (đang là 0) và ô Số lần dùng (đang là 1) → bấm Tạo mã
- **Kết quả mong đợi:** FR-17: `min_order_amount` và `max_uses_per_user` là trường bắt buộc → bị chặn
- **Kết quả thực tế:** Mã được tạo; cột Đơn tối thiểu hiện "₫" (rỗng). Hai ô không có `required`
- **Ảnh:** [CL-27.png](screenshots/CL-27.png)
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#61 (HW02 báo ở mức API)

### BUG-08 · Form Tạo mã giảm giá: Tạo được mã chỉ gồm khoảng trắng

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Form Tạo mã giảm giá: Tạo được mã chỉ gồm khoảng trắng`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-29
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Ô Mã nhập 3 dấu cách, Giá trị 10, Ngày 31/12/2099 → bấm Tạo mã
- **Kết quả mong đợi:** Mã chỉ có khoảng trắng bị từ chối (slide: "từ chối chỉ toàn khoảng trắng")
- **Kết quả thực tế:** Mã được tạo; dòng mới trong bảng có cột Mã trống, khách hàng không thể nhập mã này
- **Ảnh:** [CL-29.png](screenshots/CL-29.png)

### BUG-09 · Nhấp đúp nút gửi tạo danh mục trùng / báo lỗi giả; nút không có trạng thái đang xử lý

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Nhấp đúp nút gửi tạo danh mục trùng / báo lỗi giả; nút không có trạng thái đang xử lý`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`, `ia: IA-04`
- **Mục checklist:** CL-44, CL-65
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Danh mục, nhập "DM NHAP DUP", nhấp đúp Thêm mới
  2. Mở Mã Giảm Giá, điền mã `DUP1` hợp lệ, nhấp đúp Tạo mã
  3. (Khi mạng chậm) bấm Tạo mã một lần và quan sát nút trong lúc chờ
- **Kết quả mong đợi:** Chỉ tạo 1 bản ghi, không báo lỗi; trong lúc chờ nút bị vô hiệu hoặc đổi nhãn "Đang tạo..."
- **Kết quả thực tế:** A-03 tạo 2 danh mục "DM NHAP DUP"; A-05 tạo mã rồi lần gửi thứ 2 bật alert lỗi UNIQUE dù đã tạo thành công. Trong 2 giây chờ (mô phỏng mạng chậm) nút vẫn bật, vẫn ghi "Tạo mã". Cùng nguyên nhân: nút không bị vô hiệu khi đang gửi
- **Ảnh:** [CL-44.png](screenshots/CL-44.png), [CL-65.png](screenshots/CL-65.png)

### BUG-10 · Tạo mã trùng hiện lỗi SQLite thô bằng tiếng Anh

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Tạo mã trùng hiện lỗi SQLite thô bằng tiếng Anh`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`, `ia: IA-01`
- **Mục checklist:** CL-62
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Nhập Mã `SAVE10` (đã tồn tại), Giá trị 10, Ngày 31/12/2099 → bấm Tạo mã
- **Kết quả mong đợi:** Thông báo tiếng Việt, dễ hiểu, ví dụ "Mã SAVE10 đã tồn tại" (Nielsen #9, FR-21)
- **Kết quả thực tế:** Alert: "Lỗi: SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code": lỗi CSDL thô, tiếng Anh, lộ tên bảng/cột
- **Ảnh:** [CL-62.png](screenshots/CL-62.png)
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#57 (thông báo lỗi chưa phải tiếng Việt)

### BUG-11 · Thông báo lỗi hiển thị bằng alert() bật lên, không nằm phía trên nút submit

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Thông báo lỗi hiển thị bằng alert() bật lên, không nằm phía trên nút submit`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-41
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, tạo mã trùng `SAVE10` → bấm Tạo mã
  2. Quan sát vị trí thông báo lỗi
- **Kết quả mong đợi:** FR-22: thông báo lỗi xuất hiện trong form, phía trên nút submit
- **Kết quả thực tế:** Lỗi hiện bằng hộp thoại `alert()` của trình duyệt, chặn toàn trang; không có vùng lỗi trong form. A-03 cũng dùng alert ("Lỗi thêm DM: ...")
- **Ảnh:** [CL-41.png](screenshots/CL-41.png)

### BUG-12 · Tải lại trang (F5) và nút Back làm mất vị trí màn hình

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Tải lại trang (F5) và nút Back làm mất vị trí màn hình`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-03`
- **Mục checklist:** CL-52, CL-53
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, nhấn F5
  2. Mở một trang khác, rồi vào Admin; từ Dashboard bấm Mã Giảm Giá, rồi bấm nút Back của trình duyệt
- **Kết quả mong đợi:** F5 giữ nguyên màn hình; Back quay về Dashboard (Nielsen #3)
- **Kết quả thực tế:** F5 đưa về Dashboard; Back rời khỏi Admin, về trang trước đó trong lịch sử trình duyệt. URL luôn là `/` vì màn hình chuyển bằng state, không có route
- **Ảnh:** [CL-52.png](screenshots/CL-52.png), [CL-53.png](screenshots/CL-53.png)

### BUG-13 · Tạo mã / thêm danh mục thành công không có thông báo xác nhận

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Tạo mã / thêm danh mục thành công không có thông báo xác nhận`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-57, CL-58
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, tạo mã `MOI2026` hợp lệ
  2. Mở Danh mục, thêm "Đồng hồ"
- **Kết quả mong đợi:** Có toast/thông báo "Đã tạo mã ...", "Đã thêm danh mục ..." (Nielsen #1, Shneiderman #3). FR-24 yêu cầu phản hồi trực quan sau "Thêm vào giỏ"; mục này áp dụng tương tự cho thao tác tạo/thêm ở Admin
- **Kết quả thực tế:** Không có thông báo; form chỉ tự xóa trắng, người dùng phải tự dò bảng để biết đã thành công
- **Ảnh:** [CL-57.png](screenshots/CL-57.png), [CL-58.png](screenshots/CL-58.png)

### BUG-14 · Không có trạng thái đang tải khi dữ liệu chưa về

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Không có trạng thái đang tải khi dữ liệu chưa về`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-64
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768; DevTools → Network → throttling Slow 3G (hoặc làm chậm API 3 giây)
- **Các bước tái hiện:**
  1. Tải lại trang Admin, mở ngay Mã Giảm Giá
  2. Mở Dashboard trong lúc dữ liệu chưa về
- **Kết quả mong đợi:** Hiển thị spinner/"Đang tải..." (Nielsen #1)
- **Kết quả thực tế:** Bảng mã trống, Dashboard hiện "0 ₫" và "0" như dữ liệu thật cho tới khi API trả về
- **Ảnh:** [CL-64.png](screenshots/CL-64.png)

### BUG-15 · Mất kết nối backend không có thông báo lỗi

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Mất kết nối backend không có thông báo lỗi`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-67
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768; tắt backend (Ctrl+C cửa sổ `node server.js`) hoặc chặn request tới cổng 3000
- **Các bước tái hiện:**
  1. Tải lại trang Admin
  2. Mở Mã Giảm Giá và Dashboard
- **Kết quả mong đợi:** Thông báo "Không tải được dữ liệu, vui lòng thử lại" (Nielsen #1, #9)
- **Kết quả thực tế:** Không có thông báo; bảng trống, Dashboard hiện "0 ₫" và "0" như dữ liệu thật (lỗi bị bỏ qua trong `fetchData`)
- **Ảnh:** [CL-67.png](screenshots/CL-67.png)

### BUG-16 · Form không có nhãn: chú thích chỉ là placeholder, bị che bởi giá trị mặc định và bị cắt khi phóng to

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Form không có nhãn: chú thích chỉ là placeholder, bị che bởi giá trị mặc định và bị cắt khi phóng to`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-24, CL-25, CL-18
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, quan sát form; gõ vào một ô bất kỳ
  2. Phóng to trình duyệt 200% (Ctrl +), quan sát chú thích các ô
- **Kết quả mong đợi:** Mỗi ô có `<label>` hiển thị cố định (WCAG 3.3.2); nhìn ô vẫn biết ý nghĩa; ở 200% vẫn đọc được đủ chú thích (WCAG 1.4.4)
- **Kết quả thực tế:** 6/6 ô chỉ có placeholder, biến mất khi gõ; ô Đơn tối thiểu và Số lần dùng hiện sẵn "0" và "1" nên không thấy placeholder. Ở 200% ô chỉ rộng 102px, chú thích "Mã coupon (VD: SAVE10)", "Giá trị % (VD: 10)" bị cắt. Ô Tên danh mục (A-03) cũng không có nhãn. axe-core 4.10.2 báo `select-name` (critical, WCAG 4.1.2): dropdown "Loại" không có tên truy cập
- **Ảnh:** [CL-24.png](screenshots/CL-24.png), [CL-25.png](screenshots/CL-25.png), [CL-18.png](screenshots/CL-18.png)

### BUG-17 · Văn bản không đạt tỉ lệ tương phản 4.5:1

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Văn bản không đạt tỉ lệ tương phản 4.5:1`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-16
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Đo tương phản (DevTools → Inspect → Contrast, hoặc axe DevTools) của nút Tạo mã, nút Xóa, nhãn "Hết hạn", mã coupon, placeholder
- **Kết quả mong đợi:** WCAG 1.4.3: chữ thường ≥ 4.5:1
- **Kết quả thực tế:** Nút "Tạo mã" (trắng/cam) 2.80:1; nút "Xóa" (trắng/đỏ) 3.76:1; nhãn "Hết hạn" (đỏ/trắng) 3.76:1; mã coupon (cam/trắng) 3.56:1; placeholder ô nhập (xám/trắng) 2.54:1. axe-core xác nhận `color-contrast` (serious): 10 phần tử ở A-05, 3 ở A-03. Các phần đạt: mục sidebar đang chọn, "Đăng xuất", nhãn và số liệu Dashboard
- **Ảnh:** [CL-16.png](screenshots/CL-16.png)

### BUG-18 · Phóng to 400% (320 CSS px) không dàn lại bố cục

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Phóng to 400% (320 CSS px) không dàn lại bố cục`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-19
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Ở cửa sổ rộng 1280px, nhấn Ctrl + để phóng to 400% (hoặc DevTools → kích thước 320×640)
  2. Mở Mã Giảm Giá
- **Kết quả mong đợi:** WCAG 1.4.10: nội dung dàn lại, không cần cuộn 2 chiều; sidebar thu gọn
- **Kết quả thực tế:** Sidebar vẫn chiếm 256px, vùng nội dung chỉ còn 64px; tiêu đề vỡ từng chữ, phải cuộn ngang lẫn dọc để dùng form
- **Ảnh:** [CL-19.png](screenshots/CL-19.png)

### BUG-19 · Mục sidebar đang chọn chỉ được phân biệt bằng màu chữ

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Mục sidebar đang chọn chỉ được phân biệt bằng màu chữ`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-03`, `ia: IA-01`
- **Mục checklist:** CL-47
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. So sánh mục "Mã Giảm Giá" với các mục khác (hoặc xem ảnh chụp ở chế độ xám)
- **Kết quả mong đợi:** WCAG 1.4.1: có dấu hiệu ngoài màu (nền, viền, chữ đậm, `aria-current`)
- **Kết quả thực tế:** Chỉ khác màu chữ (xanh nhạt); cùng độ đậm, không nền, không viền, không `aria-current`
- **Ảnh:** [CL-47.png](screenshots/CL-47.png)

### BUG-20 · Các nút Xóa cùng tên truy cập "Xóa", trình đọc màn hình không biết xóa mục nào

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Các nút Xóa cùng tên truy cập "Xóa", trình đọc màn hình không biết xóa mục nào`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-23
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. DevTools → Accessibility, xem tên của các nút Xóa (hoặc dùng NVDA/Narrator)
- **Kết quả mong đợi:** Tên phân biệt, ví dụ `aria-label="Xóa mã SAVE10"` (WCAG 2.4.6, 4.1.2)
- **Kết quả thực tế:** Mọi nút đều tên "Xóa", không có `aria-label`
- **Ảnh:** [CL-23.png](screenshots/CL-23.png)

### BUG-21 · Ô Mã coupon không giới hạn độ dài; mã dài làm tràn bảng

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Ô Mã coupon không giới hạn độ dài; mã dài làm tràn bảng`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`, `ia: IA-01`
- **Mục checklist:** CL-31, CL-21
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, dán chuỗi 300 ký tự (không dấu cách) vào ô Mã, điền các ô còn lại, bấm Tạo mã
  2. Thu cửa sổ còn rộng 1024px, xem bảng
- **Kết quả mong đợi:** Ô Mã có giới hạn ký tự hợp lý (maxLength) hoặc báo lỗi khi vượt; mã dài hiển thị không làm tràn bảng
- **Kết quả thực tế:** Ô nhận đủ 300 ký tự (`maxLength = -1`), mã được tạo; ở 1024px bảng rộng 3146px so với vùng nội dung 768px, các cột bên phải và nút Xóa bị đẩy ra ngoài vùng nhìn
- **Ảnh:** [CL-31.png](screenshots/CL-31.png), [CL-21.png](screenshots/CL-21.png)

### BUG-22 · Cột Hết hạn: mã đã hết hạn bị ẩn ngày hết hạn

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Cột Hết hạn: mã đã hết hạn bị ẩn ngày hết hạn`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-14
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Xem cột Hết hạn ở dòng EXPIRED
- **Kết quả mong đợi:** Mã hết hạn vẫn hiện ngày, ví dụ "Hết hạn (01/01/2020)" (Nielsen #1, #6)
- **Kết quả thực tế:** Dòng EXPIRED chỉ hiện "Hết hạn", không biết hết hạn từ ngày nào
- **Ảnh:** [CL-14.png](screenshots/CL-14.png)

### BUG-23 · Trang khai báo lang="en" cho nội dung tiếng Việt

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Trang khai báo lang="en" cho nội dung tiếng Việt`
- **Label:** `bug`, `severity: medium`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-10
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Admin
  2. DevTools → Elements, xem thẻ `<html>`
- **Kết quả mong đợi:** `<html lang="vi">` (WCAG 3.1.1)
- **Kết quả thực tế:** `<html lang="en">`; trình đọc màn hình đọc nội dung tiếng Việt bằng giọng tiếng Anh
- **Ảnh:** [CL-10.png](screenshots/CL-10.png)

### BUG-24 · Nút Tạo mã, Thêm mới, Xóa và mục Đăng xuất không đổi màu khi rê chuột

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Nút Tạo mã, Thêm mới, Xóa và mục Đăng xuất không đổi màu khi rê chuột`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`, `ia: IA-03`
- **Mục checklist:** CL-72, CL-55
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Rê chuột lên nút Tạo mã, Xóa (A-05) và Thêm mới (A-03)
  2. Rê chuột lên các mục sidebar, đặc biệt mục Đăng xuất
- **Kết quả mong đợi:** Nút và mục điều hướng có phản hồi khi rê chuột (slide: nút "di chuột làm nổi bật")
- **Kết quả thực tế:** Màu nền các nút không đổi; mục Đăng xuất không đổi màu (không có class `hover:`), trong khi 5 mục điều hướng khác có
- **Ảnh:** [CL-72.png](screenshots/CL-72.png), [CL-55.png](screenshots/CL-55.png)

### BUG-25 · Trường bắt buộc không có dấu *

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Trường bắt buộc không có dấu *`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-26
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, quan sát form
  2. Mở Danh mục, quan sát ô Tên danh mục
- **Kết quả mong đợi:** FR-22: trường bắt buộc có `*` cạnh nhãn (6 trường FR-17, Tên danh mục FR-14)
- **Kết quả thực tế:** Không có dấu `*` nào (form cũng không có nhãn, xem bug thiếu nhãn)
- **Ảnh:** [CL-26.png](screenshots/CL-26.png)
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#59

### BUG-26 · Nút hành động tích cực "Tạo mã" màu cam thay vì xanh dương

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Nút hành động tích cực "Tạo mã" màu cam thay vì xanh dương`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-02
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá, quan sát nút Tạo mã
- **Kết quả mong đợi:** FR-21: nút hành động tích cực màu xanh dương (như nút "Thêm mới" ở Danh mục)
- **Kết quả thực tế:** Nền `rgb(249, 115, 22)` (bg-orange-500)
- **Ảnh:** [CL-02.png](screenshots/CL-02.png)
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#58

### BUG-27 · Thẻ h1 duy nhất là logo "EShop Admin", không mô tả màn hình

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Thẻ h1 duy nhất là logo "EShop Admin", không mô tả màn hình`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-08
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở lần lượt Dashboard, Danh mục, Mã Giảm Giá
  2. DevTools → Elements, tìm thẻ h1
- **Kết quả mong đợi:** FR-21: mỗi trang đúng 1 `<h1>` mô tả nội dung trang (ví dụ "Quản lý Mã Giảm Giá")
- **Kết quả thực tế:** h1 luôn là "EShop Admin" (logo sidebar); tên màn hình là `<h2>`
- **Ảnh:** [CL-08.png](screenshots/CL-08.png)

### BUG-28 · Tiêu đề tab trình duyệt luôn là "frontend-admin"

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Tiêu đề tab trình duyệt luôn là "frontend-admin"`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-09
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Admin, quan sát tiêu đề tab trình duyệt ở cả 3 màn hình
- **Kết quả mong đợi:** Tiêu đề mô tả ứng dụng và màn hình, ví dụ "Quản lý mã giảm giá | EShop Admin" (WCAG 2.4.2)
- **Kết quả thực tế:** Tiêu đề luôn là "frontend-admin" (tên project mặc định của Vite), không đổi theo màn hình
- **Ảnh:** [CL-09.png](screenshots/CL-09.png)
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#57 (tiêu đề tab)

### BUG-29 · Dashboard còn nhãn tiếng Anh "Delivered"

- **Tiêu đề issue:** `[23120017][T1][A-02][Chrome] Dashboard còn nhãn tiếng Anh "Delivered"`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-01
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Dashboard
- **Kết quả mong đợi:** FR-21: toàn bộ giao diện tiếng Việt, ví dụ "Tổng doanh thu (Đã giao)"
- **Kết quả thực tế:** Thẻ ghi "Tổng doanh thu (Delivered)"
- **Ảnh:** [CL-01.png](screenshots/CL-01.png)
- **Ghi chú:** Related angquoc/software-testing-2026-HW02-group#57 (cùng loại lỗi ở màn Mã Giảm Giá)

### BUG-30 · Định dạng số tiền thay đổi theo ngôn ngữ của trình duyệt

- **Tiêu đề issue:** `[23120017][T1][A-02, A-05][Chrome] Định dạng số tiền thay đổi theo ngôn ngữ của trình duyệt`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-06
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Chrome đặt ngôn ngữ tiếng Việt: mở Mã Giảm Giá, xem Đơn tối thiểu của SAVE10
  2. Chrome đặt ngôn ngữ English (US): mở lại cùng màn hình
- **Kết quả mong đợi:** FR-21: đơn vị tiền nhất quán, cùng một định dạng trên mọi trình duyệt
- **Kết quả thực tế:** vi-VN hiện "300.000 ₫", en-US hiện "300,000 ₫" (`toLocaleString()` không truyền locale). Tổng doanh thu ở Dashboard cũng vậy
- **Ảnh:** [CL-06.png](screenshots/CL-06.png)

### BUG-31 · Cột Hết hạn hiển thị ngày dạng yyyy-mm-dd, khác định dạng ô nhập dd/mm/yyyy

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Cột Hết hạn hiển thị ngày dạng yyyy-mm-dd, khác định dạng ô nhập dd/mm/yyyy`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-13
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. So sánh ô Ngày hết hạn với cột Hết hạn của bảng
- **Kết quả mong đợi:** Cùng một định dạng ngày (Nielsen #4)
- **Kết quả thực tế:** Ô nhập hiển thị dd/mm/yyyy, bảng hiện "2099-12-31"
- **Ảnh:** [CL-13.png](screenshots/CL-13.png)

### BUG-32 · Viết hoa không nhất quán giữa tiêu đề, menu và cột bảng

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Viết hoa không nhất quán giữa tiêu đề, menu và cột bảng`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-01`
- **Mục checklist:** CL-15
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Danh mục và Mã Giảm Giá, đọc sidebar, tiêu đề, tiêu đề cột
- **Kết quả mong đợi:** Một quy ước viết hoa (viết hoa chữ đầu câu)
- **Kết quả thực tế:** "Mã Giảm Giá", "Quản lý Mã Giảm Giá", "Tên Danh Mục" (viết hoa mọi chữ) bên cạnh "Danh mục", "Tạo mã giảm giá mới", "Đơn tối thiểu"
- **Ảnh:** [CL-15.png](screenshots/CL-15.png)

### BUG-33 · Cho tạo mã có ngày hết hạn trong quá khứ mà không cảnh báo

- **Tiêu đề issue:** `[23120017][T1][A-05][Chrome] Cho tạo mã có ngày hết hạn trong quá khứ mà không cảnh báo`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-02`
- **Mục checklist:** CL-37
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Mở Mã Giảm Giá
  2. Nhập Mã `QUAKHU`, Giá trị 10, Ngày 01/01/2020 → bấm Tạo mã
- **Kết quả mong đợi:** Chặn hoặc cảnh báo ngày đã qua (Nielsen #5)
- **Kết quả thực tế:** Mã được tạo và ngay lập tức hiện "Hết hạn"
- **Ảnh:** [CL-37.png](screenshots/CL-37.png)

### BUG-34 · Mục "Đăng xuất" không tách khỏi các mục điều hướng (mt-8 bị ghi đè)

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Mục "Đăng xuất" không tách khỏi các mục điều hướng (mt-8 bị ghi đè)`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-03`
- **Mục checklist:** CL-51
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Quan sát sidebar
  2. DevTools: xem margin-top của mục Đăng xuất
- **Kết quả mong đợi:** Đăng xuất cách xa các mục điều hướng để tránh bấm nhầm (mã nguồn có ý định dùng `mt-8` = 32px)
- **Kết quả thực tế:** Chỉ cách 16px như mọi mục khác vì `space-y-4` ghi đè `mt-8`; chỉ khác màu đỏ
- **Ảnh:** [CL-51.png](screenshots/CL-51.png)

### BUG-35 · Token hết hạn/không hợp lệ bị đưa về trang đăng nhập không báo lý do

- **Tiêu đề issue:** `[23120017][T1][A-02, A-03, A-05][Chrome] Token hết hạn/không hợp lệ bị đưa về trang đăng nhập không báo lý do`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-68
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. DevTools → Application → Local Storage: sửa `adminToken` thành `token.het.han`
  2. Tải lại trang
- **Kết quả mong đợi:** Thông báo "Phiên đăng nhập đã hết hạn, vui lòng đăng nhập lại"
- **Kết quả thực tế:** Về thẳng trang đăng nhập, không có thông báo
- **Ảnh:** [CL-68.png](screenshots/CL-68.png)

### BUG-36 · Bảng mã giảm giá và bảng danh mục khi trống không có empty state

- **Tiêu đề issue:** `[23120017][T1][A-03, A-05][Chrome] Bảng mã giảm giá và bảng danh mục khi trống không có empty state`
- **Label:** `bug`, `severity: low`, `platform: admin`, `task: T1 checklist`, `ia: IA-04`
- **Mục checklist:** CL-66
- **Trình duyệt / OS:** Chrome 157.0.8103.39, Windows 11 Home, 1366×768
- **Điều kiện tiên quyết:** Đã reset DB (`node database.js`); đăng nhập Admin `admin@eshop.com` / `Admin123!` tại http://localhost:5174; Chrome 157, Windows 11, 1366×768
- **Các bước tái hiện:**
  1. Xóa hết mã giảm giá trong Mã Giảm Giá
  2. Xóa hết danh mục trong Danh mục
- **Kết quả mong đợi:** FR-24: trang trống có icon/hình minh họa và message thân thiện
- **Kết quả thực tế:** Chỉ còn dòng tiêu đề bảng, không icon, không lời nhắn
- **Ảnh:** [CL-66.png](screenshots/CL-66.png)
