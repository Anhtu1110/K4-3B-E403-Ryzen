# Nhật ký kiểm thử người dùng - AI Daily Question Radar

**Nhóm:** Ryzen · **Phòng:** E403 · **Track:** B  
**Dự án:** AI Daily Question Radar  
**File lưu trữ:** `user_feedback_log.md`

---

## 1. Nguồn và phạm vi kiểm thử

Nhật ký ghi nhận kết quả thử nghiệm thực tế từ 5 thành viên trong danh sách mời thử của nhóm Ryzen.

- **Phiên bản thử nghiệm:** Baseline v1.0
- **Tổng thời lượng ghi nhận:** 5.5 giờ (330 phút)
- **Danh sách người tham gia:** Nguyễn Trần Bảo Tâm, Phan Thị Khánh Linh, Đặng Thế Vinh, Đỗ Đình Long, Nguyễn Như Tài.
- **Phạm vi kiểm thử:** Đánh giá khả năng tìm câu hỏi tồn đọng, đối chiếu nội dung gốc, phân loại chủ đề và sử dụng bộ lọc trên hệ thống.

---

## 2. Nhật ký chi tiết các phiên thử (V01 - V05)

### V01 - Nguyễn Trần Bảo Tâm

- **Mã học viên:** Ryzen-E403
- **Vai trò khi thử:** Học viên / TA
- **Thời lượng / Phiên bản:** 0.5 giờ (30 phút) | Baseline v1.0
- **Task đã giao:** 
  - `T01`: Tìm case tồn đọng
  - `T02`: Case cần TA review
- **Hành vi quan sát:** Do dự khi nhấn nút "Cần review". Mất nhiều thời gian xác nhận giao diện để kiểm tra các câu hỏi chưa xử lý.
- **Chỗ kẹt / Cần gợi ý:** Không tìm thấy bộ lọc thời gian "Hôm nay" trên giao diện danh sách.
- **Kết quả task:** Cần gợi ý (vướng thao tác tìm bộ lọc).
- **Sean Ellis Score:** Hơi tiếc
- **Đồng ý đưa quote vào GitHub:** Có

> **Quote nguyên văn:**  
> *"Có do dự mấy lần, nếu bấm nút này không biết có gửi tin nhắn liền không hay vẫn phải chờ xác nhận..."*

---

### V02 - Phan Thị Khánh Linh

- **Mã học viên:** Khánh Linh
- **Vai trò khi thử:** Mod / TA
- **Thời lượng / Phiên bản:** 1.0 giờ (60 phút) | Baseline v1.0
- **Task đã giao:** 
  - `T01`: Tìm case tồn đọng
  - `T03`: Sửa phân loại
- **Hành vi quan sát:** Do dự khi nhấn nút "Cần review". Nhấn nút nhấp nhả nhiều lần do giao diện phản hồi chậm.
- **Chỗ kẹt / Cần gợi ý:** Không tìm thấy bộ lọc thời gian "Hôm nay".
- **Kết quả task:** Cần gợi ý
- **Sean Ellis Score:** Rất tiếc
- **Đồng ý đưa quote vào GitHub:** Có

> **Quote nguyên văn:**  
> *"Bấm vào không thấy phản hồi liền nên cứ phải bấm đi bấm lại, không biết hệ thống đã nhận lệnh chưa."*

---

### V03 - Đặng Thế Vinh

- **Mã học viên:** Đặng Ý Vinh
- **Vai trò khi thử:** Học viên
- **Thời lượng / Phiên bản:** 1.0 giờ (60 phút) | Baseline v1.0
- **Task đã giao:** 
  - `T02`: Case cần TA review
  - `T04`: Đối chiếu tin gốc / Cập nhật xử lý
- **Hành vi quan sát:** Do dự khi nhấn "Cần review". Nhấp nhả nút nhiều lần để kiểm tra xem trạng thái đã cập nhật chưa.
- **Chỗ kẹt / Cần gợi ý:** Không tìm thấy bộ lọc thời gian "Hôm nay".
- **Kết quả task:** Cần gợi ý
- **Sean Ellis Score:** Hơi tiếc
- **Đồng ý đưa quote vào GitHub:** Có

> **Quote nguyên văn:**  
> *"Hệ thống có cho biết tin nhắn đã được cập nhật chưa, hay phải tự sang Discord để kiểm tra lại?"*

---

### V04 - Đỗ Đình Long

- **Mã học viên:** B Đình Long
- **Vai trò khi thử:** TA
- **Thời lượng / Phiên bản:** 1.0 giờ (60 phút) | Baseline v1.0
- **Task đã giao:** 
  - `T03`: Sửa phân loại
  - `T05`: Kiểm tra bộ lọc
- **Hành vi quan sát:** Do dự khi nhấn "Cần review". Thao tác bị ngắt quãng, nhấp nhả nút nhiều lần.
- **Chỗ kẹt / Cần gợi ý:** Không tìm thấy bộ lọc thời gian "Hôm nay".
- **Kết quả task:** Không làm được (kẹt ở phần bộ lọc).
- **Sean Ellis Score:** Rất tiếc
- **Đồng ý đưa quote vào GitHub:** Có

> **Quote nguyên văn:**  
> *"Tìm mãi không thấy nút lọc theo ngày hôm nay ở đâu để rà soát các case mới phát sinh..."*

---

### V05 - Nguyễn Như Tài

- **Mã học viên:** Nguyễn Như
- **Vai trò khi thử:** Mod
- **Thời lượng / Phiên bản:** 2.0 giờ (120 phút) | Baseline v1.0
- **Task đã giao:** 
  - `T01` - `T05`: Kiểm thử toàn bộ luồng thao tác
- **Hành vi quan sát:** Do dự khi nhấn nút "Cần review". Thao tác nhấn vội và nhấp nhả nút nhiều lần trong suốt quá trình thử.
- **Chỗ kẹt / Cần gợi ý:** Không tìm thấy bộ lọc thời gian "Hôm nay".
- **Kết quả task:** Cần gợi ý
- **Sean Ellis Score:** Rất tiếc
- **Đồng ý đưa quote vào GitHub:** Có

> **Quote nguyên văn:**  
> *"Không tìm thấy nút lọc nhanh làm thao tác bị chậm, phải lướt qua toàn bộ danh sách rất tốn thời gian."*

---

## 3. Tổng hợp kết quả định lượng

### Tỷ lệ hoàn thành Task (Mẫu số: 5 người)

| Kết quả | Số người | Tỷ lệ |
|---|---:|---:|
| Tự hoàn thành (không cần gợi ý) | 0/5 | 0% |
| Cần gợi ý / Hướng dẫn | 4/5 | 80% |
| Không hoàn thành được | 1/5 | 20% |

### Khảo sát Mức độ tiếc nuối (Sean Ellis Score)

| Đánh giá | Số người | Tỷ lệ |
|---|---:|---:|
| Rất tiếc (Very disappointed) | 3/5 | 60% |
| Hơi tiếc (Somewhat disappointed) | 2/5 | 40% |
| Không sao (Not disappointed) | 0/5 | 0% |

---

## 4. Các vấn đề kỹ thuật & UI/UX lặp lại

| Vấn đề phát hiện | Tần suất | Các phiên gặp lỗi |
|---|---:|---|
| Không tìm thấy bộ lọc thời gian "Hôm nay" | 5/5 (100%) | V01, V02, V03, V04, V05 |
| Do dự / Lo lắng khi nhấn nút "Cần review" | 5/5 (100%) | V01, V02, V03, V04, V05 |
| Thao tác nhấp nhả / Nhấn nút nhiều lần | 4/5 (80%) | V02, V03, V04, V05 |
| Hệ thống phản hồi chậm (Slow latency) | 1/5 (20%) | V02 |

---

## 5. Tổng hợp chỉ đạo & Hướng xử lý (Action Items)

1. **Chủ đề lặp lại nhiều nhất:** 
   - Bộ lọc thời gian ("Hôm nay") bị ẩn hoặc khó tiếp cận.
   - Nút "Cần review" thiếu phản hồi tức thì (Feedback state) khiến người dùng phân vân và nhấn liên tục.

2. **Thay đổi ưu tiên trước Demo (Hotfix):**
   - **UI/UX Filter:** Đưa bộ lọc "Hôm nay / Theo ngày" ra vị trí nổi bật trên thanh công cụ.
   - **Visual Feedback:** Thêm trạng thái `Loading` hoặc `Success Notification` ngay khi nhấn nút "Cần review" để làm rõ tác dụng thao tác.

3. **Điều giữ nguyên:**
   - Giữ nguyên luồng đối chiếu tin gốc (`T01`) và tính năng sửa phân loại (`T03`) do người dùng nắm bắt tốt sau khi được hướng dẫn.

4. **Backlog phát triển:**
   - Tối ưu thời gian phản hồi API (Latency).
   - Bổ sung ghi nhận kết quả độc lập cho từng sub-task.
   - Cập nhật các thay đổi liên quan vào mục 9 trong file `spec.md`.
