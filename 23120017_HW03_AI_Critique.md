# AI Critique (HW03 – GUI & Usability)

- Sinh viên: Trần Thanh An (23120017)
- Công cụ AI: Claude Code (model Claude Opus 5.5), chi tiết ở [23120017_HW03_AI_Audit_Report.md](23120017_HW03_AI_Audit_Report.md)

AI sai ở ba chỗ đáng kể. Thứ nhất, AI mô tả quy trình Task 1 đẹp hơn thực tế: báo cáo bản đầu viết như thể sinh viên review "vòng 1" của AI, trong khi thực tế chỉ có một prompt và AI tự review chính mình. Thứ hai, AI lấy FR-24 (giỏ hàng của Web) làm oracle cho màn Admin, tức là thiên lệch theo câu chữ đặc tả thay vì phạm vi thật. Thứ ba, AI tin số đo của script hơn bằng chứng: ba mục bị chấm Passed nhầm vì tiêu chí lỏng, ảnh không chụp được hộp thoại alert và thanh tab, và trên Android lỗi của script (bấm tọa độ ngoài màn hình, phần tử bị che) suýt được ghi thành lỗi của sản phẩm.

Các lỗi này không bị bắt ngay vì AI rà soát kết quả của chính nó trong cùng phiên, với cùng giả định ban đầu. Prompt "hoàn thành hoàn hảo task 1" cũng không có điểm dừng để con người kiểm tra. Lỗi chỉ lộ ra khi có một người đánh giá độc lập (subagent chấm điểm), khi tôi xem lại ảnh và tự thao tác trên SUT, và khi chạy cùng checklist trên nền tảng khác.

Nguyên tắc tôi rút ra: dẫn AI đi từng bước, dừng sau mỗi bước để duyệt. Mỗi kết luận Pass/Fail phải có bằng chứng nhìn thấy được. Người review không được là chính AI vừa sinh ra kết quả. Báo cáo phải ghi trung thực phần nào do AI làm, phần nào do tôi làm, kể cả phần chưa làm.
