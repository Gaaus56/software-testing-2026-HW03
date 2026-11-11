---
name: ai-audit-log
description: Trích tự động toàn bộ prompt (nguyên văn), thời gian và câu trả lời của AI từ file phiên Claude Code (.jsonl) thành log Markdown cho AI Audit Report (đề bài §9). Dùng khi người dùng nói "xuất prompt log", "làm AI audit report", "trích prompt từ file JSON".
---

# AI audit log

## Cách dùng
1. Tìm file phiên: `~/.claude/projects/<thư-mục-dự-án>/<session-id>.jsonl` (mỗi phiên một file; chọn file mới nhất của dự án).
2. Chạy:
   ```
   python -I -X utf8 scripts/export_prompts.py <session.jsonl> <out.md> "Claude Code (model ...)"
   ```
3. Kiểm tra đầu ra:
   - Số lượt prompt khớp số lần người dùng gửi tin nhắn.
   - Không còn thẻ hệ thống (`<system-reminder>`, `<ide_...>`, `<task-notification>`).
   - Lượt có ảnh ghi "Kèm N ảnh".
4. Dùng bảng tóm tắt đầu file để điền phần "Danh sách lần dùng AI" của AI Audit Report: công cụ, ngày giờ, prompt, output (tóm tắt + link tới log đầy đủ).

## Script làm gì
- Chỉ lấy tin nhắn của người dùng, bỏ kết quả công cụ, tin nhắn meta và đoạn tóm tắt ngữ cảnh tự động.
- Giữ nguyên chữ người dùng gõ/dán, chỉ bỏ thẻ do IDE/hệ thống tự chèn.
- Ghi văn bản trả lời của AI và thống kê công cụ AI đã gọi trong lượt (Bash, Read, Edit, Write, Agent...).
- Đổi giờ sang UTC+7.

## Quy tắc
- Không sửa nội dung prompt cho "đẹp"; nếu cần ẩn thông tin cá nhân thì thay bằng `[ẩn]` và ghi chú lý do.
- Xuất lại ở cuối buổi làm để log có cả các lượt mới nhất.
