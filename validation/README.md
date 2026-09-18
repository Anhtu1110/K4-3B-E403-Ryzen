# Validation - AI Daily Question Radar

Nhóm Ryzen, lớp 3B, phòng E403, Track B.

**Trạng thái: đã chuẩn bị tài liệu, chưa có feedback thực tế được ghi nhận trong thư mục này.**
Các dòng chờ điền không phải bằng chứng người dùng đã thử sản phẩm. Chỉ cập nhật kết quả, quan sát và quote sau phiên thử thật.

## Link nộp form

[Thư mục validation trên GitHub](https://github.com/Anhtu1110/K4-3B-E403-Ryzen/tree/main/validation)

## Nội dung

| Tài liệu | Mục đích |
|---|---|
| [Kế hoạch dùng thử](test-plan.md) | Người tham gia dự kiến, kịch bản theo luồng Radar và phiên thử 10 phút |
| [Nhật ký feedback](feedback-log.md) | Ai thử, task, quan sát, quote nguyên văn, mức nghiêm trọng và quyết định |
| [Changelog từ feedback](changelog.md) | Liên kết feedback với thay đổi, quyết định giữ nguyên hoặc backlog |

## Vì sao trước đây chưa có thư mục này?

[README của repo](../README.md) mô tả cấu trúc cần nộp, trong đó có `validation/`, nhưng trên bản `719bd3d` chưa có file nào được Git theo dõi tại đường dẫn này. Hướng dẫn không tự tạo thư mục; Git cũng không lưu thư mục rỗng.

`validation/` dùng để lưu bằng chứng **người ngoài nhóm dùng thử** (R6).
[Golden set](../eval/golden%20set.json) và kết quả đo AI thuộc `eval/` (R4); tỷ lệ pass của AI hoặc unit test không thay cho feedback người dùng.

## Đối chiếu yêu cầu

- [Rubric R6](../04-rubric.md): feedback từ ít nhất 2 người ngoài nhóm, đủ tên/vai, task, quan sát và quote nguyên văn; có ít nhất 1 thay đổi từ feedback hoặc quyết định giữ nguyên có căn cứ.
- [Guide mục 4.2](../02-guide.md): phiên thử 10 phút/người, ghi mức nghiêm trọng và 4 dòng tổng hợp.
- [README mục R6](../README.md): yêu cầu 5 người ngoài nhóm, trong đó 2 người đã khai ở CP1.

Các tài liệu khác nhau về số người. Kế hoạch này chuẩn bị cho **5 người** để đáp ứng mức yêu cầu cao hơn. Cần đối chiếu bản nộp CP1 để xác nhận 2 willing user; tên trong [spec mục 8](../spec.md) chưa tự chứng minh việc đã khai CP1.

## Trước khi nộp kết quả validation

- [ ] Xác nhận người thử ngoài nhóm, vai trò thực tế và willing user đã khai CP1.
- [ ] Ghi phiên bản prototype, thời gian và hình thức thử: trực tiếp hay chỉ xem ảnh/mock.
- [ ] Ghi task, hành vi quan sát được, chỗ kẹt và quote đúng lời người thử vào feedback log.
- [ ] Tổng hợp 4 dòng cuối log, kể cả kết quả chưa tốt.
- [ ] Ghi quyết định dựa trên từng feedback vào changelog; đồng bộ thay đổi thực tế sang spec mục 9.
- [ ] Kiểm tra link minh chứng xem được và chỉ công khai nội dung đã được người tham gia đồng ý.

Việc tạo thư mục hoàn thành cấu trúc repo; chưa có log thực tế thì chưa đủ bằng chứng R6.
