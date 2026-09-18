# Ghi nhận đã kiểm chứng

Nguồn của bảng này là yêu cầu chỉnh sửa của nhóm, mã nguồn, log API và lượt chạy unit test. Đây không phải bảng quote được gán cho người dùng thử.

| Mã | Nguồn thực tế | Ghi nhận | Xử lý / kết luận |
|---|---|---|---|
| F01 | Yêu cầu của nhóm ngày 18/09/2026 | Danh sách thiếu Đỗ Đình Long và Nguyễn Như Tài. | Đã thêm hai tên vào danh sách và spec mục 8, tổng cộng 5 người. |
| F02 | Tài liệu tại commit `b1486a7` và yêu cầu bỏ bảng trống | Các bảng phiên thử/feedback chỉ có ô chờ điền. | Đã bỏ các bảng này, công bố số liệu có log và đặt nội dung minh họa trong file riêng. |
| F03 | [Lượt API, case C03/C07/C21](../eval/runs/cp3-baseline-20260918/cases.csv) | Ba câu thuộc chủ đề lab bị gán `other`, confidence lần lượt 0,70 / 0,80 / 0,70. | Ghi nhận lỗi phân loại; cần cải thiện định nghĩa chủ đề rồi đo lại. Không có kết quả sau sửa trong lượt này. |
| F04 | [Log C09-C11 và các nhãn cần rà lại](../eval/runs/cp3-baseline-20260918/cases.csv) | Bộ case thiếu nội dung trả lời để kiểm chứng nhãn ANSWERED; tổng cộng 9 case được đánh dấu rà nhãn. | Giữ cả 25 case trong mẫu số khi báo cáo; nêu hạn chế của nhãn, không loại case khó để tăng tỷ lệ. |
| F05 | [Unit test trên `b1486a7`](evidence/unit-tests.txt) | 11/11 test đạt, gồm lưu trạng thái, đổi chủ đề, link nguồn, SLA, lọc thông báo và che một số dạng thông tin nhạy cảm. | Ghi nhận các hành vi được test; kết quả này không đo độ hài lòng hoặc độ chính xác AI. |

## Tổng hợp

1. **Vấn đề nổi bật trong log:** phân loại chủ đề lab thành other ở C03/C07/C21 và thiếu bằng chứng cho một số nhãn. Không có số đếm mức lặp từ người dùng thử.
2. **Thay đổi đã làm:** cập nhật đủ 5 tên, bỏ bảng chờ điền, đính kèm bảng số liệu đã đối chiếu và phân biệt phản hồi minh họa.
3. **Giữ nguyên có căn cứ:** giữ nhãn gốc, mẫu số 25 và quality bar của spec để báo cáo mức khớp đúng với lần chạy đã lưu.
4. **Việc tiếp theo từ kết quả:** bổ sung hội thoại trả lời có nguồn, duyệt lại 9 nhãn, cải thiện phân loại chủ đề lab rồi chạy một lượt mới.

[5 câu minh họa](feedback-examples.md) là nội dung soạn theo yêu cầu của nhóm, không dùng làm bằng chứng R6.
