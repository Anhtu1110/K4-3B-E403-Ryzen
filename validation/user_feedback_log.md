# User Feedback Log - AI Daily Question Radar

Nhóm Ryzen - Track B - E403.

Đây là file duy nhất lưu validation với người dùng. Chỉ ghi điều đã xảy ra trong phiên thử thật: hành vi quan sát, câu nói nguyên văn và quyết định của nhóm. Không dùng unit test, golden set hay câu ví dụ tự soạn để thay cho feedback người dùng.

## Mục tiêu

Kiểm tra xem người dùng có thể dùng AI Daily Question Radar để tìm câu hỏi cần hỗ trợ, đối chiếu với tin gốc và quyết định xử lý an toàn hay không.

Danh sách nhóm dự kiến mời thử:

1. Nguyễn Trần Bảo Tâm
2. Phan Thị Khánh Linh
3. Đặng Thế Vinh
4. Đỗ Đình Long
5. Nguyễn Như Tài

Tên trong danh sách không đồng nghĩa đã tham gia. Chỉ thêm kết quả của người đã thử thật.

## Cách làm một phiên thử

Mỗi người thử khoảng 10 phút. Người thử tự cầm chuột; người trong nhóm không chỉ nút cần bấm.

1. Nói: "Tụi mình đang thử sản phẩm, không đánh giá bạn. Không có đúng hay sai, bạn cứ nói to suy nghĩ của mình."
2. Hỏi ngữ cảnh: "Lần gần nhất bạn cần tìm hoặc kiểm tra một câu hỏi chưa được trả lời trên Discord, bạn làm như thế nào?"
3. Chọn một task bên dưới và giao theo đúng kết quả cần đạt.
4. Im lặng quan sát: ghi thao tác đầu tiên, chỗ do dự, chỗ hiểu sai và lúc cần gợi ý.
5. Hỏi sau khi dùng: "Điều gì khó hiểu hoặc khó chịu nhất?" - "Bạn có tin kết quả này không, vì sao?" - "Nếu ngày mai không còn công cụ này, bạn rất tiếc / hơi tiếc / không sao?"

## Task để giao

Chọn 1-2 task phù hợp cho mỗi người:

- **T01 - Tìm case tồn đọng:** "Hãy tìm một câu hỏi còn cần hỗ trợ và kiểm tra bản tóm tắt có đúng với tin gốc không."
- **T02 - Case cần TA review:** "Hãy xử lý câu hỏi thiếu ngữ cảnh hoặc liên quan deadline, quy chế hay điểm danh. Bạn sẽ làm gì tiếp?"
- **T03 - Sửa phân loại:** "Một câu hỏi đang nằm sai chủ đề. Hãy sửa để người tiếp nhận hiểu đúng việc cần làm."
- **T04 - Cập nhật xử lý:** "Sau khi có người phản hồi, hãy cập nhật để danh sách phân biệt được case đã xử lý và case còn tồn."
- **T05 - Kiểm tra bộ lọc:** "Hãy rà soát danh sách và chỉ ra tin bot, thông báo, tin đã trả lời hoặc tin còn trong SLA có bị tính nhầm không."

## Gửi thông tin cho Codex sau mỗi người thử

Gửi đúng mẫu này, mỗi người một khối. Không cần viết đẹp; cần đúng sự thật.

```text
Tên:
Mã học viên (nếu đồng ý công khai):
Vai trò khi thử (TA/Mod/học viên đóng vai TA/...):
Ngày giờ và commit đang thử:
Task đã giao (T01-T05):
Hành vi quan sát được:
Chỗ kẹt hoặc cần gợi ý:
Quote nguyên văn:
Kết quả task (tự làm được / cần gợi ý / không làm được):
Sean Ellis (rất tiếc / hơi tiếc / không sao) và lý do nguyên văn:
Đồng ý đưa quote vào GitHub: có/không
```

Sau khi có ít nhất 2 khối thông tin thật, Codex sẽ điền các phiên vào file này, tổng hợp chủ đề lặp lại, thay đổi trước demo, điều giữ nguyên và backlog. Nếu có thay đổi sản phẩm, cập nhật thêm `spec.md` mục 9 bằng mã phiên liên quan.

## Kết quả validation

Chưa có phiên người dùng thật được ghi trong file này.

Khi có dữ liệu, mỗi phiên sẽ được thêm ở đây theo dạng:

```markdown
### V01 - [Tên người thử]

- Thời gian và phiên bản: ...
- Vai trò: ...
- Task: ...
- Hành vi quan sát: ...
- Quote nguyên văn: "..."
- Kết quả: ...
- Sean Ellis: ...
- Quyết định của nhóm: ...
```

## Tổng hợp sau vòng thử

Chỉ viết phần này sau khi đã có phiên thật:

- Chủ đề lặp lại nhiều nhất: ...
- Thay đổi trước demo: ...
- Giữ nguyên và lý do: ...
- Backlog: ...
