# Danh sách và kịch bản dùng thử

## Danh sách do nhóm cung cấp

| STT | Họ và tên |
|---|---|
| 1 | Nguyễn Trần Bảo Tâm |
| 2 | Phan Thị Khánh Linh |
| 3 | Đặng Thế Vinh |
| 4 | Đỗ Đình Long |
| 5 | Nguyễn Như Tài |

Ba tên đầu có trong [canvas CP1](../canvas.md) và [spec mục 8](../spec.md). Đỗ Đình Long và Nguyễn Như Tài được nhóm bổ sung ngày 18/09/2026. Danh sách này ghi tên, không gán vai trò, thời điểm dùng thử, sự đồng ý công khai hay lời nhận xét cho từng người.

## Kịch bản

Căn cứ chức năng trong [spec mục 4-6](../spec.md) và [runbook](../docs/CP3-RUNBOOK.md). Đây là kịch bản thử, không phải nhật ký phiên đã diễn ra.

| Mã | Mục tiêu giao cho người dùng | Điểm cần đánh giá |
|---|---|---|
| T01 | Tìm câu hỏi đang cần hỗ trợ và đối chiếu bản tóm tắt với tin gốc. | Xác định đúng case tồn đọng và mở đúng nguồn. |
| T02 | Xử lý câu hỏi thiếu ngữ cảnh hoặc liên quan quy chế. | Nhận biết mục cần TA review và thông tin còn thiếu. |
| T03 | Sửa chủ đề của một câu hỏi đang được phân loại sai. | Tìm được thao tác sửa và nhận biết kết quả đã lưu. |
| T04 | Cập nhật danh sách sau khi đã phản hồi một câu hỏi. | Phân biệt trạng thái còn tồn với đã xử lý. |
| T05 | Rà lại tin bot, tin đã trả lời và câu còn trong thời gian chờ. | Phát hiện mục không nên bị tính vào tồn đọng. |

Người thử tự thao tác; người quan sát ghi hành vi, chỗ kẹt và mức trợ giúp. Sau task, hỏi điều khó hiểu nhất, mức tin tưởng vào kết quả và lý do có hoặc không dùng sản phẩm.

Kết quả đã đo bằng công cụ nằm tại [technical-results.md](technical-results.md). Không dùng log kỹ thuật để điền thay trải nghiệm của người trong danh sách.
