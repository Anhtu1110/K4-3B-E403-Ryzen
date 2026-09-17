| # | Dòng | Nội dung |
|---|---|---|
| 1 | Track + đề | B · Tính năng mới cho TA/học viên |
| 2 | Job executor (ai · đang ở đâu · làm gì) | Mod / Learning Coach · kiểm tra kênh Discord cuối ngày · để rà soát và xử lý các câu hỏi học viên chưa được hỗ trợ.|
| 3 | Pain một câu (ai – đang làm gì – vướng đâu – hậu quả) | TA/Mod đang rà soát bản tin cuối ngày để hỗ trợ học viên, nhưng vướng ở chỗ bot đếm sai (tính cả tin bot/tin đã trả lời) và tóm tắt lỗi, khiến họ phải dò lại từng kênh thủ công và dễ bỏ sót học viên đang mắc kẹt. |
| 4 | 1–2 bằng chứng đầu (số + cách đếm + mã hội thoại/tin nhắn, hoặc khảo sát/phỏng vấn có số người) | K4-L2-3 (gửi 2026-09-14) và K4-L3-4 (gửi 2026-09-14)
- Trong `data/discord-pack/k4_daily_reports.md`, bản tin bot có nhiều lỗi thật: câu hỏi đã có phản hồi nhưng vẫn ghi “chưa xác nhận đã xử lý”, và từ “nguồn tham chiếu” bị chèn sai chỗ; đó là bằng chứng cho thấy summary hiện tại không đáng tin.
   - Trong `data/discord-pack/k4_messages.csv`, hàng trăm tin nhắn xoay quanh deadline, lab, điểm danh, ticket, team, XP; các câu hỏi này lặp lại và rất dễ bị bỏ sót nếu không có bộ lọc/nhóm chủ đề. |
| 5 | Lát cắt MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả) | Một TA cuối ngày mở bản tin, AI chỉ lọc ra các câu hỏi chưa ai trả lời sau 4 giờ và gom theo chủ đề, trả về danh sách tồn đọng sạch mà không làm lộ tên học viên. |
| 6 | AI tự làm đến đâu + 1 dòng lý do · ≥3 willing users ngoài nhóm |AI tự động lọc và gom nhóm câu hỏi, nhưng các tin nhắn mơ hồ sẽ bị đẩy vào luồng "Cần TA xem lại" vì báo sai thông tin deadline/quy chế có hậu quả rất đắt. · 3 willing users: Nguyễn Trần Bảo Tâm(2A202602408), Phan Thị Khánh Linh (2A202602360), Đặng Thế Vinh(2A202602587). |
| 7 | Phân công có tên |Anh Tú (Product Spec & Faciliator), Tất Đạt (Code ReAct & Data filter), Hồng Cường (Prompt & Golden Set), Bảo Trang (Mock UI & Demo Slide). |
