# Validation - AI Daily Question Radar

Nhóm Ryzen, lớp 3B, phòng E403, Track B.

[Link thư mục để nộp form](https://github.com/Anhtu1110/K4-3B-E403-Ryzen/tree/main/validation)

## Kết quả có minh chứng

| Nội dung | Kết quả | Nguồn |
|---|---|---|
| Bộ test kỹ thuật chạy trên commit `b1486a7` | 11/11 test đạt | [Log unit test](evidence/unit-tests.txt) |
| Lượt API ngày 18/09/2026, 15:01:30 UTC+7 | 25 case, 2 request, 2.517 token | [Bản tóm tắt đã đối chiếu](../eval/runs/cp3-baseline-20260918/summary.json) |
| Khớp trạng thái với nhãn của nhóm | 12/25 = 48% | [Bảng từng case](../eval/runs/cp3-baseline-20260918/cases.csv) |
| Khớp cả trạng thái và chủ đề | 11/25 = 44% | [Bảng từng case](../eval/runs/cp3-baseline-20260918/cases.csv) |
| Case cần rà lại nhãn/bằng chứng trả lời | 9/25 | [Chi tiết kiểm chứng](technical-results.md) |

Lượt API đã có sẵn trong checkout `cp3-evaluation`; lần cập nhật này đối chiếu log gốc và công bố bản tóm tắt, không tuyên bố đã gọi API thêm một lượt. Đây là kết quả trên bộ 25 tình huống của nhóm, có ngữ cảnh thời gian mô phỏng được ghi trong [bản tóm tắt](../eval/runs/cp3-baseline-20260918/summary.json).

## Danh sách và tài liệu

- [Danh sách đủ 5 người và kịch bản dùng thử](test-plan.md): Nguyễn Trần Bảo Tâm, Phan Thị Khánh Linh, Đặng Thế Vinh, Đỗ Đình Long, Nguyễn Như Tài.
- [Ghi nhận đã kiểm chứng](feedback-log.md): các vấn đề có nguồn và cách xử lý trong lần cập nhật này.
- [Kết quả kỹ thuật](technical-results.md): cách đo, số liệu, giới hạn và lệnh chạy lại test.
- [Changelog](changelog.md): những việc đã thực hiện.
- [5 câu phản hồi minh họa](feedback-examples.md): nội dung tự soạn, không phải lời nói của 5 người trong danh sách.

## Phạm vi bằng chứng

Tên người tham gia do nhóm cung cấp. Repo hiện không có bản ghi phiên dùng thử hoặc quote trực tiếp của 5 người này. Kết quả kỹ thuật và câu minh họa không chứng minh họ đã dùng sản phẩm.

[Rubric R6](../04-rubric.md) yêu cầu feedback thực tế từ ít nhất 2 người ngoài nhóm; [README](../README.md) ghi 5 người, gồm 2 willing user đã khai CP1. Các bảng chờ điền đã được bỏ; tài liệu chỉ ghi thông tin có nguồn và phân biệt rõ phần minh họa.
