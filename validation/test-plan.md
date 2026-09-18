# Kế hoạch dùng thử

**Trạng thái: dự kiến, chưa ghi nhận phiên thử hoàn thành.**

## Mục tiêu và phiên bản

Kiểm tra một người dùng có thể rà soát câu hỏi tồn đọng, kiểm chứng tin gốc và cập nhật cách xử lý bằng AI Daily Question Radar hay không.

- Căn cứ thiết kế: [spec mục 4-6](../spec.md).
- Căn cứ vận hành: [CP3 runbook](../docs/CP3-RUNBOOK.md).
- Phiên bản tham chiếu khi lập kế hoạch: `719bd3d`. Mỗi phiên phải ghi commit thực tế đã thử.
- Phân biệt rõ thử trực tiếp prototype với xem ảnh/dashboard mock. Với ảnh tĩnh, chỉ ghi nhận khả năng hiểu thông tin; chưa kết luận thao tác tương tác thành công.

## Người tham gia dự kiến

Ba tên đầu đã được khai là willing users trong spec mục 8, nhưng chưa có xác nhận tham gia hay log ở đây.

| Mã dự kiến | Người tham gia | Vai trò thực tế | Đã khai CP1? | Trạng thái |
|---|---|---|---|---|
| V01 | Nguyễn Trần Bảo Tâm | Chờ xác nhận | Chờ đối chiếu | Chờ dùng thử |
| V02 | Phan Thị Khánh Linh | Chờ xác nhận | Chờ đối chiếu | Chờ dùng thử |
| V03 | Đặng Thế Vinh | Chờ xác nhận | Chờ đối chiếu | Chờ dùng thử |
| V04 | Chưa mời | Chờ xác nhận | Chờ đối chiếu | Chưa lên lịch |
| V05 | Chưa mời | Chờ xác nhận | Chờ đối chiếu | Chưa lên lịch |

Ưu tiên TA/Mod/Learning Coach theo job executor trong spec. Nếu người thử là học viên đóng vai TA, ghi đúng vai trò đó và giới hạn của kết quả.

## Chuẩn bị

1. Chạy bản prototype đã chọn theo runbook, ghi commit và phần nào đang mock.
2. Chuẩn bị kênh thử với tin giả lập: câu hỏi rõ ràng, tin mơ hồ, tin bot, câu đã có phản hồi và câu hỏi quy chế. Không dùng thông tin cá nhân thật để tạo case thử.
3. Ghi cửa sổ quét và SLA thực tế. Mặc định SLA là 240 phút; nếu giảm SLA để demo phải ghi rõ, không coi đó là kết quả kiểm chứng chờ 4 giờ.
4. Đảm bảo người thử có quyền mở tin gốc và thao tác trên kênh thử. Các hành động gửi trả lời chỉ thử trong kênh thử đã thống nhất.
5. Xin phép ghi chép và công khai quote/minh chứng; che thông tin cá nhân, token và nội dung ngoài phạm vi được đồng ý.

## Task giao theo mục tiêu

Các tiêu chí dưới đây là **điều cần quan sát**, chưa phải kết quả đã đạt. Chọn 2-3 task phù hợp cho mỗi phiên và ghi mã task vào log.

| Mã | Lời giao task | Điều cần quan sát |
|---|---|---|
| T01 | Cuối ngày, hãy tìm một câu hỏi còn cần hỗ trợ và kiểm tra xem bản tóm tắt có đúng với tin gốc không. | Người thử xác định được case tồn đọng, tìm được nguồn và phát hiện sai lệch nếu có. |
| T02 | Có một câu hỏi quá ngắn hoặc liên quan quy chế. Hãy quyết định bước xử lý tiếp theo dựa trên thông tin đang có. | Người thử hiểu mục cần TA review, nhận ra thiếu căn cứ và không coi suy đoán của AI là câu trả lời chắc chắn. |
| T03 | Một câu hỏi đang nằm sai nhóm chủ đề. Hãy sửa cách phân loại để người tiếp nhận hiểu đúng việc cần làm. | Người thử tự tìm thao tác đổi chủ đề và kiểm tra trạng thái sau khi sửa. |
| T04 | Bạn đã phản hồi một câu hỏi. Hãy cập nhật danh sách để người khác biết tình trạng xử lý. | Người thử phân biệt trạng thái đã xử lý với chưa xử lý, kiểm tra được kết quả cập nhật. |
| T05 | Hãy rà lại danh sách tồn đọng và chỉ ra mục nào không nên xuất hiện, nếu có. | Người thử đối chiếu tin bot, câu đã trả lời, tin còn trong SLA và phát hiện mục bị đếm nhầm. |

## Một phiên 10 phút

1. **Làm quen (1 phút):** nói rõ đang đánh giá sản phẩm, không đánh giá người thử; mời họ nói to suy nghĩ.
2. **Bối cảnh (1 phút):** hỏi lần gần nhất họ rà soát hoặc chờ giải đáp câu hỏi trên Discord, đã làm gì và kẹt ở đâu.
3. **Giao task (1 phút):** đọc mục tiêu ở bảng, để người thử tự thao tác; không chỉ trước vị trí nút.
4. **Quan sát (5 phút):** ghi hành động đầu tiên, chỗ do dự, hiểu sai và mọi lần phải trợ giúp. Khi cần chỉ hỏi trung tính: "Bạn sẽ làm gì tiếp?".
5. **Hỏi sau khi dùng (2 phút):** ghi nguyên văn câu trả lời cho các câu hỏi bên dưới.

## Câu hỏi sau khi dùng

- Điều gì khó hiểu hoặc khó chịu nhất?
- Bạn có tin kết quả này không? Vì sao?
- Bạn có dùng thật không? Vì sao hoặc vì sao chưa?
- Nếu từ mai không được dùng sản phẩm nữa, bạn thấy rất tiếc, hơi tiếc hay không sao? Vì sao?

Ghi hành vi thực tế tách khỏi nhận xét và dự đoán tương lai. Nếu mọi phản hồi chỉ là lời khen chung chung, dùng task khó hơn để thu được quan sát cụ thể.
