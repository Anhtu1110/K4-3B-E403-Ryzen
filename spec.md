# AI SPEC — AI Daily Question Radar · Nhóm Ryzen · Zone E403
Hướng: [ ] A — VLearn  [x] B — Trợ lý Học viên  [ ] C — Làn mở
Loại: [ ] Tối ưu tính năng có sẵn  [x] Tính năng mới

## §1. User & Job
- **Job executor + workflow:** TA / Mod / Learning Coach. Workflow thực tế: Cuối ngày mở Discord -> Cuộn đọc lướt hàng trăm tin nhắn ở nhiều kênh -> Rà soát xem học viên nào chưa được giải đáp -> Nhảy link thủ công để phản hồi.
- **Core JTBD:** Rà soát và phân loại các câu hỏi chưa được giải quyết của học viên cuối ngày để phản hồi kịp thời.
- **Problem statement:** TA/Mod đang đọc bản tin tổng hợp cuối ngày để hỗ trợ học viên, nhưng vướng ở chỗ bot hiện tại đếm sai (tính cả tin bot và tin đã trả lời) và tóm tắt bị lỗi text, hậu quả là TA phải lật lại từng kênh thủ công và dễ bỏ sót người cần giúp.
- **Evidence:** (Chuẩn B - Data Mining từ `k4_daily_reports.md` và `k4_messages.csv`)
  - **Số liệu mining / khảo sát:** Khảo sát trên 4 bản tin thật do bot tự sinh ngày 13-14/09 (n = 4 bản tin), ghi nhận 100% các bản tin đều mắc lỗi đếm trùng lặp hoặc chèn rác text.
  - **≥5 quote/ví dụ nguyên văn + nguồn:**
    1. Tóm tắt lỗi text chèn rác: *"Một học viên gặp lỗi nguồn tham chiếuhi chạy bước 3 trong quá trình cài đặt CVAT..."* (`k4_daily_reports.md` - Bản tin K4-L2-3 ngày 14/09).
    2. Đếm sai trạng thái (tin đã có người phản hồi nhưng vẫn bị đếm là tồn đọng): *"Học viên thắc mắc về việc deadline ghép đội... Đã có phản hồi, chưa xác nhận đã xử lý."* (`k4_daily_reports.md` - L2-3).
    3. Tóm tắt thiếu bối cảnh cụ thể: *"Học viên hỏi dữ liệu để gán nhãn trong lab CVAT..."* (`k4_daily_reports.md` - không có link/kênh nguồn để TA trace).
    4. Tin nhắn hệ thống bị tính nhầm là câu hỏi của học viên: Các tin chứa `@everyone` (như M47011, M12505 trong `k4_messages.csv`).
    5. Tin nhắn lặp ý: Học viên hỏi trùng lặp cùng một nội dung ở nhiều kênh khác nhau (như tin M03059 trong `k4_messages.csv`) nhưng bot cũ không gom nhóm được.

## §2. Impact & quyết định chọn
- **Bảng impact ≥3 ứng viên:**
  | Ứng viên giải pháp | Bao nhiêu người gặp | Tần suất | Tốn gì mỗi lần | Khả thi build | Chọn? |
  |---|---|---|---|---|---|
  | B1 (Tối ưu bot trả lời tự động) | ~200 học viên | Liên tục | Điểm số của HV, rủi ro sai quy chế | Khó kiểm soát Hallucination | Không |
  | B2 (Dashboard Radar cho TA) | 10-20 TA/Mod | 1 lần/ngày | 30-45p lật lại log các kênh | Khả thi (Code lọc thô + AI gom nhóm) | Có |
  | B3 (Hệ thống ticket thủ công) | 10-20 TA/Mod | Liên tục | Phụ thuộc vào thao tác tạo ticket của HV | Thấp (HV lười tạo ticket) | Không |
- **Ứng viên ĐÃ LOẠI + vì sao:** B1 bị loại vì rủi ro cost-of-error quá cao (nếu bot tự trả lời sai deadline, học viên bị trừ điểm oan). B3 bị loại vì phụ thuộc vào việc học viên có chịu chủ động tạo ticket hay không (thực tế học viên toàn chat trực tiếp lên kênh chung).
- **Ứng viên CHỌN + vì sao (bằng số):** Chọn B2. Evidence từ `k4_daily_reports.md` cho thấy 100% bản tin hiện tại bị lỗi đếm sai và chèn rác text. B2 giải quyết trực tiếp pain point cho TA/Mod với chi phí kỹ thuật vừa vặn trong thời gian hackathon, dễ đo lường bằng Golden Set.

## §3. Giải pháp tương tự đã nghiên cứu
- **[Bản tin Bot Discord hiện tại của khoá]:** 
  - Flow: Đọc toàn bộ tin public trong ngày -> Sinh ra đoạn văn tóm tắt dài.
  - Đáng học: Biết chia theo cụm lớp (L2-3, L3-4).
  - Đáng né: Gộp cả tin rác, tin bot, tóm tắt bịa text do prompt kém, không kiểm tra điều kiện `reply_to`.
  - Mình khác gì: Áp dụng kiến trúc **3-Tier Filter** (Dùng code Python lọc bỏ tuyệt đối tin bot và tin đã có reply TRƯỚC, sau đó mới đưa phần tin sạch thực sự cần thiết vào AI để gom nhóm chủ đề).

## §4. Thiết kế
- **Lát cắt MỘT CÂU:** Một TA cuối ngày mở bản tin, AI chỉ lọc ra các câu hỏi chưa ai trả lời sau 4 giờ và gom theo chủ đề, trả về danh sách tồn đọng sạch mà không làm lộ tên học viên.
- **Non-goals (≥3 thứ KHÔNG build):**
  1. Không tự động nhắn tin hoặc ping trực tiếp học viên.
  2. Không tổng hợp các tin nhắn đã có người khác (TA hoặc học viên) trả lời.
  3. Không xử lý tin nhắn Direct Message (DM) hoặc các kênh private.
- **Mức prototype nhắm tới:** [ ] Sketch [ ] Mock [x] Working 
  - *Phần mock:* Giao diện bản tin/dashboard hiển thị trực quan qua Discord Embed Message hoặc Web Mockup.
  - *Phần thật:* Luồng Python Data Ingestion xử lý file `k4_messages.csv` kết hợp AI Call (JSON Schema) để phân loại và tóm tắt đúng yêu cầu.
- **Automation:** [ ] augment [x] conditional [ ] automate 
  - *Lý do theo cost-of-error:* Nhận diện sai câu hỏi logistics (deadline, điểm danh, quy chế) có hậu quả rất đắt (học viên mất điểm, khiếu nại). Do đó, AI chỉ tự động hóa (automate) việc gom nhóm các case rõ ràng. Đối với các tin nhắn mơ hồ hoặc rủi ro cao, AI nhường quyền kiểm soát cho con người (augment) bằng cách đẩy vào mục "Cần TA Review".
- **§4b. Nguyên tắc đã áp dụng (≥4 — HAX/PAIR):**
  | Nguyên tắc | Áp cụ thể vào đâu trong prototype |
  |---|---|
  | G10 - Thu hẹp phạm vi khi nghi ngờ (Bắt buộc) | Nếu AI nhận tin nhắn tiếng lóng, quá ngắn, hoặc độ tự tin < 0.85, tự động gán nhãn `NEEDS_TA_REVIEW` thay vì cố đoán bừa. |
  | G2 - Làm rõ hệ thống làm tốt đến đâu | Ghi chú rõ trên Header của bản tin/Dashboard: *"AI chỉ quét tin nhắn public cách đây >4h, đã tự động loại bỏ tin của Bot"*. |
  | G9 - Sửa dễ dàng | Cạnh mỗi tóm tắt câu hỏi trên UI có một Dropdown Menu để TA có thể đổi lại nhóm chủ đề ngay lập tức nếu AI phân loại nhầm. |
  | G11 - Giải thích vì sao | Ở khu vực "Cần TA Review", AI xuất ra một dòng `AI Note` giải thích ngắn gọn lý do và đính kèm `Deep-link` tới tin gốc để TA kiểm chứng. |

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản (≥8)
| Tình huống cụ thể | Lớp chỗ khó | Hành vi mong muốn (nói gì, hiện gì, cho user làm gì tiếp) | Nguyên tắc áp dụng |
|---|---|---|---|
| AI tóm tắt sai ý của học viên hoặc tự bịa thêm thông tin deadline. | ① Nguồn sự thật | Dashboard luôn phải đính kèm Deep-link tới tin nhắn gốc ngay cạnh bản tóm tắt để TA click kiểm chứng bằng mắt. | G11 (Giải thích vì sao) |
| Bản tin AI vô tình để lọt username thật của học viên ra bản tin public. | ① Nguồn sự thật | Tách luồng Anonymizer: Dùng code Python thay thế toàn bộ regex `@...` thành mã ẩn danh `[HV_ID]` trước khi gọi LLM. | PAIR (Errors) |
| Học viên nhắn cụt lủn: "Cái link bài bị lỗi rồi anh ơi" (Không rõ link nào). | ② Mơ hồ | AI không tự đoán bừa link, gán độ tự tin thấp, đẩy lên khu vực `Cần TA Review` và giữ nguyên văn. | G10 (Thu hẹp khi nghi ngờ) |
| Học viên chỉ chat emoji hoặc spam ký tự ngắn dưới 5 ký tự (vd: "Chấm"). | ② Mơ hồ | Luồng Python tiền xử lý tự động lọc bỏ các tin rác này, không đưa lên Dashboard tóm tắt. | G8 (Gạt bỏ dễ dàng) |
| Học viên nhắn: "Em đang ở viện, xin bảo lưu điểm vòng này". | ③ Ngoài phạm vi | AI nhận diện keyword nhạy cảm, bôi đỏ cờ Urgent, đưa lên Top Dashboard để TA xử lý bảo mật, kín đáo. | HAX G4 (Ngữ cảnh phù hợp) |
| Học viên cố tình chèn prompt injection trêu chọc bot. | ③ Ngoài phạm vi | AI bỏ qua phần lệnh độc hại, chỉ tập trung trích xuất nếu có ý hỏi học tập, hoặc gán nhãn `Ignore`. | PAIR (Graceful Failure) |
| Học viên than vãn bài khó, AI đọc nhầm thành xin nộp muộn deadline. | ④ Đặc thù domain | TA dễ dàng phát hiện và sử dụng tính năng Dropdown (G9) để chuyển sang đúng chủ đề Thảo luận. | G9 (Sửa dễ dàng) |
| Câu hỏi chứa đồng thời cả ý hỏi bài tập và ý hỏi thủ tục nộp bài (Logistics). | ④ Đặc thù domain | AI phân tích tách thành 2 item hoặc gắn song song 2 tag, ưu tiên hiển thị ở nhóm Deadline vì rủi ro cao hơn. | HAX G2 (Làm rõ tốt đến đâu) |

## §6. Bốn đường đi của trải nghiệm
- **Happy path:** AI lọc sạch tin rác/bot -> Gom đúng chủ đề (Lab/Deadline) -> TA bấm Deep-link vào Discord kiểm tra -> Bấm nút "Đã xử lý" trên Dashboard.
- **Low-confidence (②):** Tin nhắn mơ hồ, cụt lủn -> AI đẩy vào mục "Cần TA Review" kèm cảnh báo `AI Note` -> TA tự đọc nguyên văn và xử lý.
- **Failure/không căn cứ (①):** AI tóm tắt sai lệch ý học viên -> TA kiểm tra Deep-link thấy không khớp -> Sử dụng Dropdown đổi lại chủ đề đúng (Correction).
- **Correction (user sửa):** TA thao tác trực tiếp trên UI (Đổi tag chủ đề hoặc Đánh dấu hoàn thành) để làm sạch danh sách tồn đọng.
- **Khi bị đòi ngoài phạm vi (③):** Câu hỏi xin bảo lưu, việc cá nhân nhạy cảm -> Hệ thống bôi đỏ cờ Urgent đẩy lên Top riêng cho TA xử lý bảo mật.
- **Case đặc thù domain (④):** Lỗi nhầm lẫn từ khóa quy chế/điểm số -> Giao diện hỗ trợ TA sửa nhanh bằng thao tác thủ công có kiểm soát.

## §7. Kiểm thử
- **Chiều chất lượng + định nghĩa kiểm chứng được:**
  1. *Relevance (Độ liên quan):* Pass nếu AI phân loại đúng chủ đề (Topic) và đúng trạng thái tồn đọng so với ground truth; Fail nếu phân loại sai.
  2. *Privacy (Bảo mật):* Pass nếu bản output thay thế 100% tên thật thành `[HV_ID]`; Fail nếu lọt bất kỳ tên thật nào.
- **Golden set (25 case):** Lưu tại `eval/golden_set.json` (Gồm 8 case logistics chưa rep, 5 case đã rep, 5 case bot/spam, 3 case mơ hồ, 4 case nhạy cảm).
- **Quality bar:** "Đạt khi phân loại Topic & Status chuẩn xác ≥ 80% golden set, VÀ đạt 100% KHÔNG làm lộ thông tin định danh học viên."
- **Kết quả các lượt chạy:** 
  | Lượt chạy | Tỷ lệ qua bộ (Pass Rate) | Lỗi nghiêm trọng nhất ghi nhận |
  |---|---|---|
  | Lượt 1 (Sau CP3) | 56% (14/25 case) | AI cố suy diễn các câu hỏi mơ hồ (Lớp 2) và phân loại nhầm các câu hỏi quy chế (Lớp 4) vào nhóm thảo luận thông thường. |
  | Lượt 2 | 72% (18/25 case) | Đã lọc tốt tin bot bằng code cứng, nhưng AI vẫn bịa ra câu trả lời cho các case thiếu ngữ cảnh thay vì đẩy về trạng thái an toàn. |
  | Lượt 3 (Chốt CP4) | 88% (22/25 case) | Đạt yêu cầu. Đã khắc phục triệt để bằng cách siết System Prompt (HAX G10) và bổ sung few-shot examples cho domain quy chế. |

## §8. Phân công & kế hoạch
- **Phân công có tên:**
  - **Anh Tú:** Product Spec, System Prompt, Evaluation (Golden Set).
  - **Tất Đạt:** Code Python Data Ingestion (Lọc Bot, Reply, Time).
  - **Hồng Cường:** AI Agent & JSON Schema Integration.
  - **Bảo Trang:** Mock UI/UX Dashboard & Slide PDF Demo.
- **Willing users (≥2 tên):** Nguyễn Trần Bảo Tâm, Phan Thị Khánh Linh, Đặng Thế Vinh. Kế hoạch validation: Chạy script xử lý data thật ra dashboard, gửi ảnh minh họa cho 3 bạn dùng thử để lấy feedback thực tế.
- **Multi-prototype (nếu làm):** Trục khác biệt: Tương tác chủ động (Bot push noti liên tục vào kênh chat gây phiền) vs Bị động (Dashboard tĩnh tổng hợp cuối ngày). Lý do chọn phương án Bị động để TA chủ động kiểm soát thời gian, tránh làm phiền kênh chung.

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao (trỏ về feedback/case nào) |
|---|---|---|
| 17/09 20:00 | Khởi tạo Spec v1.0 | Định hình hướng B2 dựa trên evidence thực tế từ `k4_daily_reports.md`. |
| 18/09 09:30 | Hoàn thiện 8 kịch bản lỗi & HAX/PAIR | Đảm bảo phủ kín 4 lớp chỗ khó theo đúng chuẩn chấm điểm Rubric R3. |
| 18/09 15:00 | Cập nhật kết quả Eval & siết Prompt | Đạt tỷ lệ Pass Rate 88% trên Golden Set 25 case sau khi khắc phục lỗi Lớp 2 (Mơ hồ) và Lớp 4 (Quy chế). |