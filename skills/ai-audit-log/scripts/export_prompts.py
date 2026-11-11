"""Xuất nguyên văn prompt của người dùng + câu trả lời văn bản của AI từ file phiên Claude Code (.jsonl).

Usage: python -I -X utf8 export_prompts.py <session.jsonl> <out.md> [tool_name]

- Prompt: lấy đúng chữ người dùng gõ/dán; chỉ bỏ các thẻ do IDE/hệ thống tự chèn
  (<ide_...>, <system-reminder>), không sửa chữ.
- Ảnh đính kèm: ghi số lượng (không nhúng ảnh).
- AI output: toàn bộ phần văn bản AI trả lời trong lượt đó (không gồm suy nghĩ nội bộ),
  kèm thống kê các công cụ AI đã gọi (đọc file, chạy lệnh, sửa file, subagent...).
- Lượt "tiếp tục sau khi tóm tắt ngữ cảnh" (isCompactSummary) không phải prompt của người dùng nên bỏ qua.
"""
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone

src, out = sys.argv[1], sys.argv[2]
tool = sys.argv[3] if len(sys.argv) > 3 else "Claude Code (model Claude Opus 5.5), tiện ích VS Code"
VN = timezone(timedelta(hours=7))
STRIP = re.compile(r"<(ide_[a-z_]+|system-reminder|task-notification)>.*?</\1>", re.S)
PASTE = re.compile(r"<pasted_content[^>]*>(.*?)</pasted_content[^>]*>", re.S)


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(VN)


def clean(text):
    text = STRIP.sub("", text)
    text = PASTE.sub(lambda m: "[Nội dung dán vào]\n" + m.group(1).strip(), text)
    return text.strip()


turns = []
for line in open(src, encoding="utf-8"):
    d = json.loads(line)
    t = d.get("type")
    msg = d.get("message") or {}
    content = msg.get("content")
    if t == "user" and not d.get("isMeta") and not d.get("isCompactSummary") and not d.get("isSidechain"):
        blocks = [{"type": "text", "text": content}] if isinstance(content, str) else (content or [])
        if any(b.get("type") == "tool_result" for b in blocks):
            continue
        texts = [clean(b["text"]) for b in blocks if b.get("type") == "text"]
        texts = [x for x in texts if x and not x.startswith("This session is being continued")]
        images = sum(1 for b in blocks if b.get("type") == "image")
        if not texts and not images:
            continue
        turns.append({"time": ts(d["timestamp"]), "end": ts(d["timestamp"]), "prompt": "\n\n".join(texts),
                      "images": images, "outputs": [], "tools": Counter()})
    elif t == "assistant" and turns and not d.get("isSidechain"):
        turns[-1]["end"] = ts(d["timestamp"])
        for b in content or []:
            if b.get("type") == "text" and b["text"].strip():
                turns[-1]["outputs"].append(b["text"].strip())
            elif b.get("type") == "tool_use":
                turns[-1]["tools"][b.get("name", "?")] += 1

fmt = "%Y-%m-%d %H:%M:%S"
with open(out, "w", encoding="utf-8") as f:
    f.write("# AI interaction log (xuất nguyên văn từ file phiên)\n\n")
    f.write(f"- Nguồn: `{src.replace(chr(92), '/').split('/')[-1]}` (file phiên Claude Code, định dạng JSONL)\n")
    f.write(f"- Công cụ AI: {tool}\n- Giờ: UTC+7\n- Số lượt prompt: {len(turns)}\n")
    f.write(f"- Xuất lúc: {datetime.now(VN).strftime(fmt)} bằng `export_prompts.py` (lượt cuối có thể chưa đủ câu trả lời vì đang chạy khi xuất)\n\n")
    f.write("| # | Bắt đầu | Kết thúc | Prompt (rút gọn) | Ảnh | Số lần gọi công cụ |\n|---|---|---|---|---|---|\n")
    for i, tr in enumerate(turns, 1):
        short = re.sub(r"\s+", " ", tr["prompt"])[:90].replace("|", "\\|")
        f.write(f"| {i:02d} | {tr['time'].strftime(fmt)} | {tr['end'].strftime(fmt)} | {short} | {tr['images'] or ''} | {sum(tr['tools'].values())} |\n")
    for i, tr in enumerate(turns, 1):
        f.write(f"\n---\n\n## #{i:02d} · {tr['time'].strftime(fmt)}\n\n### Prompt\n\n")
        f.write("````text\n" + (tr["prompt"] or "(chỉ có ảnh)") + "\n````\n")
        if tr["images"]:
            f.write(f"\n_Kèm {tr['images']} ảnh chụp màn hình._\n")
        if tr["tools"]:
            f.write("\n_Công cụ AI đã gọi trong lượt này: " + ", ".join(f"{k} ×{v}" for k, v in tr["tools"].most_common()) + "._\n")
        f.write("\n### AI output\n\n")
        f.write("\n\n".join(tr["outputs"]) if tr["outputs"] else "_(không có văn bản trả lời)_")
        f.write("\n")
print(f"{len(turns)} prompts -> {out}")
