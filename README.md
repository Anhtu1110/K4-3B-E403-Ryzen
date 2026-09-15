# Mini Hackathon AI — Batch 04 · Lớp 3B

**SPEC → Prototype → Demo.** Đây không phải cuộc thi code — đây là cuộc thi **tư duy sản phẩm AI**.

- Thời lượng: **39 giờ** từ phát đề đến thuyết trình (ca 3B) — LAB 5 (phát đề + build) · LEC 6 (tiếp tục build theo ca) · LAB 6 (vòng thi)
- Nhóm: **4-5 người** · thi theo phòng (E403 / E402), chia cụm rồi chung kết phòng — xem *Thể thức thi*

## Bắt đầu từ đâu?

1. Đọc **`01-challenge-brief.md`** để hiểu khung chung và 5 tiêu chí, rồi **`tracks/README.md`** để chọn track và đề.
2. Mở **`02-guide.md`** — hướng dẫn từng giai đoạn, đứng ở đâu đọc mục đó.
3. Viết spec theo **`03-ai-spec-template.md`** — deliverable trung tâm của cả sự kiện.
4. Đọc **`04-rubric.md`** ngay từ đầu — biết trước bài được chấm theo tiêu chí nào.

| File / thư mục | Nội dung |
|---|---|
| `01-challenge-brief.md` | Đề bài: bảng 5 track · lát cắt · ràng buộc chung · 5 tiêu chí nghiệm thu |
| `02-guide.md` | Hướng dẫn 5 giai đoạn: khám phá → spec → build → đo & validate → demo |
| `03-ai-spec-template.md` | Template AI Spec (nộp tại **hạn chốt spec** — xem Lịch) |
| `04-rubric.md` | Rubric 100 điểm (25 nộp checkpoint + 67 chấm bài + 8 bonus) + checklist xác minh 6 mốc |
| `tracks/` | **5 track**, mỗi đề cùng một khung mục: A VLearn Tutor · B Trợ lý Discord · C Lesson Studio · D Học tập thích ứng & tương tác · E Làn mở (trong phạm vi AI20k) — bắt đầu từ `tracks/README.md` |
| `data/` | Dữ liệu thật đã ẩn danh: `vlearn-pack/` (chatlog VLearn tutor + 6 transcript bài giảng + 2 bộ slide bản hackathon) và **`discord-pack/` (tin nhắn Discord khoá 4 + bản tin bot)** — dùng để tìm bằng chứng và xây golden set. **Đọc `data/README.md` trước** |
| `further-reading/` | Tài liệu tham khảo có tóm lược tiếng Việt: **Mom Test** (phỏng vấn), **PAIR Guidebook** (Google, 6 chương), **HAX Toolkit** (Microsoft, 18 nguyên tắc), **JTBD Playbook** + worksheet — bắt đầu từ `further-reading/README.md` |

## Lịch — 6 checkpoint (ca 3B · 39 giờ)

| Mốc | Cần hoàn thành | Hạn (ca 3B) |
|---|---|---|
| — | Khai mạc 17:30 · phát đề 18:00 | 17/9 |
| **CP1** | Canvas 4 ô + người phụ trách nộp | **19:30** · 17/9 |
| **CP2** | Bản có thể bấm thử (mock cũng được) | **21:00** · 17/9 |
| **CP3** | Video AI chạy thật 30 giây + số đo | **16:00** · 18/9 |
| **CP4** | Chốt đặc tả + báo phần còn thiếu | **21:00** · 18/9 |
| **CP5** | Slide PDF + video demo dự phòng — nộp cuối | **22:30** · 18/9 |
| **CP6** | Thuyết trình · không nộp thêm | **09:00** · 19/9 |

Hai phòng cùng ca dùng chung lịch · **nộp qua form** — nhận đủ 5 link từ đầu, xong mốc nào nộp mốc đó. CP1–CP5: mỗi mốc 5 điểm, **nộp muộn = 0 điểm mốc đó**. CP5 là hạn nộp cuối: **PDF slide + video demo dự phòng**, phải xong trước giờ pitch. CP6 không nộp thêm.

Giữa các mốc là thời gian tự làm (ngoài giờ học và trong buổi LEC 18/9 theo ca của bạn); coach hỗ trợ trên lớp và Discord. Buổi LAB 19/9 (09:00–13:00 19/9) là **vòng thi**: pitch theo cụm rồi chung kết phòng.

**Hạn chốt spec.md** (quality bar khoá từ thời điểm này): **21:00 18/9, tại CP4**.

### Link nộp

| Mốc | Form nộp |
|---|---|
| CP1 | *(cập nhật lúc khai mạc)* |
| CP2 | *(cập nhật lúc khai mạc)* |
| CP3 | *(cập nhật lúc khai mạc)* |
| CP4 | *(cập nhật lúc khai mạc)* |
| CP5 | *(cập nhật lúc khai mạc)* |

Mỗi thành viên tự nộp form của từng mốc; cả nhóm dùng chung một link repo. Link được công bố tại khai mạc và ghim trên Discord.

## Thể thức thi

- 2 ca × 2 phòng = **4 cuộc thi độc lập**, chấm và trao giải riêng từng phòng; mỗi phòng một tổ giám khảo.
- **E403** (~230 người, ~51 nhóm): 6 cụm thi, mỗi nhóm **6 phút** ở vòng cụm → 6 đội vào chung kết phòng → **Top 3**.
- **E402** (~120 người, ~27 nhóm): 5 cụm thi, mỗi nhóm **7 phút** ở vòng cụm → 5 đội vào chung kết phòng → **Top 2**.
- Nhóm 4–5 người. Giám khảo có thể hỏi **bất kỳ thành viên** — ai cũng phải hiểu bài (vibe-coding rule).
- Số nhóm/cụm là ước tính; thể lệ chi tiết vòng cụm và chung kết công bố lúc khai mạc.

## Giải thưởng

**Giải theo phòng — mỗi lớp 5 đội, hai lớp 10 đội:**

| Lớp | E403 | E402 | Tổng |
|---|---|---|---|
| 3A | Top 3 | Top 2 | 5 đội |
| 3B | Top 3 | Top 2 | 5 đội |

Đội vào Top được **cộng điểm bonus vào bài lab ngày 5 và ngày 6** cho mọi thành viên.

**Giải theo track — 4 giải, chấm chung cả hai lớp:**

- **Track A · VLearn Tutor và Track D · Học tập thích ứng & tương tác:** 2 giải, do team VLearn chọn.
- **Track C · Lesson Studio:** 2 giải, do team Studio chọn.

Một đội có thể vừa vào Top phòng vừa nhận giải track. Phần thưởng cụ thể sẽ được công bố sau.

Mỗi mốc cần show gì và được xác minh thế nào: xem bảng trong `04-rubric.md`.

## Nộp bài

Một repo nhóm, cấu trúc như sau. Spec chốt tại hạn chốt spec (xem Lịch); bản hoàn chỉnh trước CP6.

```
repo/
├── README.md          ← thành viên (mã HV + tên) + phân công có tên từng phần
├── spec.md            ← AI Spec theo 03-ai-spec-template.md
├── demo-slides.pdf    ← slide 6 trang theo 02-guide.md §5.1
├── codebase/          ← prototype (ghi rõ phần nào mock)
├── eval/              ← golden set + bảng kết quả các lượt chạy
├── validation/        ← feedback log từ vòng user test (bonus, nếu có)
└── reflection/        ← mỗi người 1 file
```

## Chấm điểm

Tổng **100 điểm = 25 điểm nộp checkpoint + 67 điểm chấm bài nộp + tối đa 8 điểm bonus** (validation với user — không bắt buộc). Chi tiết từng ý điểm: `04-rubric.md`.

**25 điểm nộp — mỗi checkpoint 5 điểm (CP1-CP5):** nộp đúng hạn → 5 điểm · nộp muộn → 0 điểm cho mốc đó. Mỗi thành viên nộp riêng, cả nhóm dùng chung một link repo.

**67 điểm chấm + 8 bonus — trên artifact trong repo, mỗi con điểm trỏ về một file:**

| Khối | Điểm | Chấm trên file nào |
|---|---|---|
| R1 · Bằng chứng & impact | 15 | `spec.md` §1-§2 + log khảo sát/mining |
| R2 · Lát cắt & thiết kế | 15 | `spec.md` §4 |
| R3 · Chỗ khó & kịch bản rủi ro | 11 | `spec.md` §5-§6 |
| R4 · Kiểm thử | 15 | `spec.md` §7 + `eval/` |
| R5 · Prototype chạy được | 8 | `codebase/` + demo |
| R6 · Validation với user — **bonus** | +8 | `validation/` |
| R7 · Quy trình & repo | 3 | cấu trúc repo |

Ba điều nên biết trước khi làm:

- Điểm dựa trên **chuỗi quyết định và bằng chứng**, không dựa trên mức độ hoành tráng của sản phẩm.
- Kết quả đo **ghi nhận trung thực** — kể cả khi không đạt mục tiêu nhóm tự đặt — vẫn được tính đủ điểm. Số liệu bị chỉnh sửa hoặc che giấu sẽ không được tính.
- Reflection cá nhân chấm riêng theo rubric của khoá. Điểm vòng demo, chấm chéo trong cụm và thưởng thêm (nếu có) theo thể lệ công bố lúc khai mạc.

## Luật chung

1. Prototype có 3 mức **Sketch / Mock / Working** — mức nào cũng bắt buộc **≥1 lời gọi AI chạy thật**.
2. **Vibe-coding rule:** dùng AI để build thoải mái, nhưng không giải thích được phần có tên mình thì phần đó 0 điểm (giám khảo hỏi bất kỳ thành viên khi thuyết trình).
3. **Quality bar** chốt tại hạn chốt spec (21:00 18/9, tại CP4) và giữ nguyên sau đó.
4. Chỉ dùng dữ liệu trong `data/` hoặc dữ liệu giả tự sinh — không dùng dữ liệu thật của người thật. Không commit API key.
5. Tuân thủ **quy định bảo mật dữ liệu** bên dưới — đây là điều kiện để được cấp data.

## Bảo mật dữ liệu được cung cấp

Dữ liệu trong `data/` là dữ liệu thật của khoá học (đã ẩn danh), cấp riêng cho hackathon này. Khi nhận data, nhóm cam kết:

1. **Chỉ dùng trong phạm vi hackathon** — cho việc tìm bằng chứng, xây golden set và build prototype. Không dùng cho mục đích khác.
2. **Không chia sẻ ra ngoài khoá học** — không đăng lên mạng xã hội, không gửi cho người ngoài, không đưa vào bất kỳ dataset hay repo công khai nào.
3. **Không commit data pack vào repo nộp bài** — repo nhóm chỉ chứa trích dẫn ngắn để minh hoạ (vài dòng); golden set trích từ data ghi rõ mã đoạn/mã hội thoại thay vì dán nguyên văn dài.
4. **Cẩn trọng khi đưa data vào công cụ ngoài** — chỉ đưa phần tối thiểu cần cho việc đang làm; lưu ý API/công cụ free tier có thể dùng dữ liệu để huấn luyện (xem `02-guide.md` §3.4).
5. **Không cố suy ngược danh tính** từ dữ liệu đã ẩn danh (`S####`, `T#####`, `D####`, `[HV]`, [học viên]). Riêng `discord-pack/`: người trong đó là **bạn cùng khoá** — tuyệt đối không đoán/hỏi "tin này của ai"; trích dẫn tối đa 2 câu mỗi ví dụ (xem `data/discord-pack/README.md`).
6. Sau sự kiện, **xoá các bản sao data pack** khỏi máy cá nhân và các công cụ đã upload nếu ban tổ chức yêu cầu.

Vi phạm được xử lý theo quy định của khoá và có thể ảnh hưởng trực tiếp đến điểm của nhóm.
