# Quyết định từ feedback

**Trạng thái: chưa có quyết định dựa trên feedback người dùng.**
Việc tạo tài liệu này là chuẩn bị cấu trúc repo, không tính là thay đổi sản phẩm xuất phát từ validation.

## Nhật ký quyết định

Chỉ thêm dòng khi đã có feedback thật trong [feedback log](feedback-log.md).
Một quyết định có thể là sửa sản phẩm, giữ nguyên có lý do hoặc đưa vào backlog.

| Ngày giờ | Mã feedback / phiên | Vấn đề quan sát được | Quyết định | Lý do / căn cứ | Người phụ trách | Trạng thái | Commit / minh chứng thử lại |
|---|---|---|---|---|---|---|---|
| Chưa có | Chưa có | Chưa ghi nhận | Chưa quyết định | Chưa có dữ liệu | Chưa phân công | Chờ validation | Chưa có |

## Đồng bộ với spec

Khi có thay đổi thực tế hoặc quyết định giữ nguyên có căn cứ, cập nhật [spec mục 9](../spec.md) theo cấu trúc có sẵn: **Thời điểm | Đổi gì | Vì sao (trỏ về feedback/case nào)**.

Trong cột "Vì sao", dẫn mã feedback và link về log. Nếu chọn giữ nguyên, nêu quan sát nào hỗ trợ quyết định; nếu đưa vào backlog, nêu giới hạn và thời điểm dự kiến xem lại.

Không sửa quality bar trong spec mục 7 dựa trên kết quả vừa quan sát. Kết quả chạy AI vẫn lưu ở `eval/`; validation ghi nhận trải nghiệm người dùng.
