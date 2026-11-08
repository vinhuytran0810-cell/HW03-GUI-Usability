# Hướng dẫn sử dụng Skill `gui-checklist-auditor` trong Codex

## 1. Cài đặt

Giải nén file ZIP **vào thư mục gốc workspace HW03** (nơi bạn mở Codex). Giữ nguyên cấu trúc:

```text
HW03/
├── .agents/
│   └── skills/
│       └── gui-checklist-auditor/
│           ├── SKILL.md
│           ├── references/gui-criteria.md
│           ├── assets/checklist-template.csv
│           ├── assets/bug-report-template.md
│           ├── assets/execution-summary-template.md
│           └── scripts/validate_skill.py
├── docs/SKILL-USAGE.md
└── eshop-sut/             # nếu bạn clone SUT tại đây
```

**Lưu ý:** Đừng chỉ giải nén `SKILL.md` riêng lẻ. Codex phải thấy `.agents/skills/gui-checklist-auditor/SKILL.md` trong thư mục đang làm việc hoặc trong phạm vi cha mà Codex quét. Nếu Codex đang mở riêng repo `eshop-sut` và không nhận Skill ở thư mục cha, hãy mở workspace `HW03` hoặc đặt `.agents/skills/` trong repo root đó.

## 2. Kiểm tra cấu trúc

Tại terminal ở root HW03:

```bash
python .agents/skills/gui-checklist-auditor/scripts/validate_skill.py
```

Trên Windows nếu không có lệnh `python`, thử `py`.

Kết quả kỳ vọng: `PASS: skill structure, front matter, workflow stages, and CSV template`. Đây **chỉ là kiểm tra cấu trúc Skill**, không chứng minh EShop đã được kiểm thử.

## 3. Kiểm tra Codex nhận Skill

Mở Codex trong workspace HW03, nhập `/skills` hoặc gõ `$` rồi tìm `gui-checklist-auditor`. Nếu chưa thấy, tải lại/restart Codex và kiểm tra đường dẫn. Tài liệu chính thức: https://learn.chatgpt.com/docs/build-skills

## 4. Dùng Skill từng giai đoạn (không bao gồm khảo sát)

**Trước khi dùng Skill:** Bạn tự setup EShop hoặc giao Codex một nhiệm vụ setup/khảo sát **riêng, không gọi Skill**. Sau đó cung cấp cho Skill URL đang chạy, phạm vi màn hình cần kiểm thử và yêu cầu HW03. Skill không có stage `explore` và không tự lập danh sách màn hình.

**Lần 1 — Thiết kế checklist**

```text
$gui-checklist-auditor
Stage=design. SUT=EShop.
Scope=những màn hình tôi đã chọn và mô tả trong tài liệu đính kèm.
Dựa trên yêu cầu HW03, tạo ít nhất 41 checkpoint có thể kiểm chứng,
thuộc IA-01 đến IA-04. Không tự mở rộng sang màn hình ngoài scope.
Đánh dấu tất cả Not Run. Nêu các giả định cần tôi xác nhận.
Xuất reports/gui-audit/02-checklist.csv để tôi review.
```

**Lần 2 — Thực thi có bằng chứng**

```text
$gui-checklist-auditor
Stage=execute. Chỉ kiểm tra các item đã được tôi phê duyệt.
Dùng trình duyệt thực sự có sẵn; ghi đúng tên môi trường.
Lưu ảnh gốc ở evidence/gui/, kết quả và hạn chế ở reports/gui-audit/.
Không tạo GitHub Issues hoặc tự sửa source.
```

**Lần 3 — So sánh môi trường**

```text
$gui-checklist-auditor
Stage=compare. Dùng cùng checklist ID cho những môi trường tôi chỉ định.
Không gọi viewport emulation là Android Chrome hoặc Safari thật.
Nếu thiếu thiết bị/browser, ghi Blocked và báo tôi cách kiểm thử thủ công.
```

**Lần 4 — Tổng hợp bug report**

```text
$gui-checklist-auditor
Stage=report. Tính số lượng Passed/Failed/Blocked/Not Run/N/A từ CSV thực tế.
Soạn draft bug report cho các Failed có bằng chứng.
Không đăng issue lên GitHub cho đến khi tôi duyệt.
```

## 5. Minh chứng phần Agent Skill trong HW03

- Commit lần 1: `Add reusable GUI checklist auditor skill` (Skill + tài liệu, trước khi chạy test).
- Lưu nguyên văn prompt và output Codex, cùng ngày/giờ thực tế của từng lần dùng AI theo yêu cầu bài.
- Quay video demo: hiển thị file SKILL.md, gọi `$gui-checklist-auditor`, chạy stage design hoặc execute, và mở artifact thực tế.
- Sau khi sử dụng, chỉnh Skill nếu thấy điểm yếu; lưu Git diff và giải thích vì sao thay đổi.
- Nếu bài yêu cầu video, kiểm tra lại rubric để bảo đảm thời lượng/nội dung phù hợp.

## 6. Giới hạn quan trọng

Skill là **quy trình hướng dẫn Agent**, không phải phần mềm tự kiểm thử có khả năng chạy khi không có công cụ. Kết quả GUI chỉ được xác nhận sau khi truy cập và quan sát ứng dụng thật. Bài usability vẫn cần người tham gia thật; Skill không tạo dữ liệu SUS/UEQ-S giả.
