# Kết quả kiểm chứng kỹ thuật

## Unit test chạy trong lần cập nhật này

- Ngày kiểm tra: 18/09/2026.
- Commit được chạy: `b1486a7`.
- Lệnh: `python -m unittest discover -s tests -v`.
- Kết quả: **11 test chạy, 11 đạt, 0 lỗi, 0 thất bại**; thời gian unittest báo: **0,301 giây**.
- [Output của lệnh](evidence/unit-tests.txt).

Các test dùng dữ liệu kiểm thử và có model giả trong test retry. Chúng kiểm tra logic; không gọi OpenAI hoặc Discord và không đo trải nghiệm của 5 người trong danh sách.

## Lượt API đã lưu

Nguồn đối chiếu: bộ artifact `artifacts/cp3-eval` trong checkout `cp3-evaluation`. [Bản tóm tắt công khai](../eval/runs/cp3-baseline-20260918/summary.json) chỉ giữ số liệu và mã case; trích đoạn tin nhắn, ID tin gốc, response ID, prompt và report thô không được đưa vào bản công khai.

| Thuộc tính | Giá trị trong log |
|---|---|
| Bắt đầu | 18/09/2026 08:01:30 UTC = 15:01:30 UTC+7 |
| Commit | `37ccf7b69103b0d71d11a7558ff837f2acb25468` |
| Model trả về | `gpt-4o-mini-2024-07-18` |
| Tổng case | 25 |
| Số request | 2, đều là phân loại câu hỏi |
| Tổng token | 2.517 |
| Thời gian toàn lượt | 14,361 giây |
| Khớp trạng thái | 12/25 = 48% |
| Khớp cả trạng thái và chủ đề | 11/25 = 44% |
| Nhãn cần rà lại | 9/25 |
| Phân luồng dự đoán | 17 NEEDS_TA_REVIEW, 2 UNANSWERED, 6 IGNORED, 0 ANSWERED |

Đối chiếu Git cho thấy `src/`, `tests/` và `eval/` của `37ccf7b` và `b1486a7` giống nhau. Log là một lượt lịch sử, không phải lượt API mới chạy trong lần sửa tài liệu này.

## Kiểm tra nguồn và cách tính

Đã tính lại cả 25 hàng từ dự đoán trong log gốc, đối chiếu fixture và CSV; các số tổng hợp khớp nhau. [summary.json](../eval/runs/cp3-baseline-20260918/summary.json) lưu hash SHA-256 của log gốc để đối chiếu với bản local. [cases.csv](../eval/runs/cp3-baseline-20260918/cases.csv) chỉ chứa mã case, nhãn, mức khớp và confidence.

- Khớp trạng thái: `actual_status == expected_status`.
- Khớp toàn bộ: khớp trạng thái và chủ đề; case có topic kỳ vọng IGNORE không chấm topic.
- Mẫu số là cả 25 case, gồm cả 9 case có nhãn cần rà lại.
- Hash SHA-256 của file core và fixture tại nguồn khớp manifest local.
- Fixture ở repo chính có cùng hash với fixture của lượt đo: `38bfb587a9a13c10ba95aa5ad88dd46e3e81e9a6785c29211f8953121755721d` (hash byte của file tại thời điểm đối chiếu).

## Hạn chế có trong dữ liệu gốc

Fixture không có timestamp hoặc channel thật. Lượt đo đã dùng tuổi tin mô phỏng 5 giờ và mỗi case một kênh; các điều kiện này được giữ rõ trong bản tóm tắt để không trình bày kết quả như đo trên hội thoại thật đã xác minh.

C09-C11 thiếu nội dung/timestamp/role của tin trả lời. C01/C02/C05/C23/C25 có xung đột giữa nhãn kỳ vọng và chính sách review; C24 có ghi chú không phải câu cần hỗ trợ nhưng nhãn là UNANSWERED. Bộ dữ liệu không có cặp duplicate được gắn nhãn nên không có số đo độ chính xác gom trùng.

Bảng 22/25 = 88% trong spec là thông tin đã có trước lần cập nhật này; log đã đối chiếu chỉ chứng minh mức khớp **11/25 = 44%** cho cả trạng thái và chủ đề. Không dùng nó để xác nhận con số 88%, tính chính xác trên hội thoại thật hoặc yêu cầu bảo mật tuyệt đối của spec.

## Chạy lại test kỹ thuật

Từ một checkout sạch của phiên bản cần kiểm tra, dùng môi trường Python có các dependency trong `requirements.txt`:

```powershell
python -m unittest discover -s tests -v
```

Kết quả API ở đây được trích từ bản lưu lịch sử. Chạy lại unit test không tạo ra một lượt đo AI mới.
