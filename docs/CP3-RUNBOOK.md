# CP3 · Chạy lõi AI thật

`src/radar.py` là lõi demo: dữ liệu CSV → rule filter/reply graph → OpenAI semantic classification → report JSON ẩn danh. Nó **không** gửi message hay cần Discord API thật.

## Cài và chạy

Dùng Python environment mà team đã thống nhất; không tạo environment mới trong repo nếu chưa thống nhất.

```powershell
pip install -r requirements.txt
$env:OPENAI_API_KEY = "..."
python src/radar.py --input data/discord-pack/k4_messages.csv --output artifacts/radar-report.json
```

Có thể chọn model bằng `--model <model-id>` hoặc `OPENAI_MODEL`. Không commit API key; `.env` đã nằm trong `.gitignore`.

## Output cần kiểm tra

- Terminal in count bốn trạng thái: `ANSWERED`, `UNANSWERED`, `NEEDS_TA_REVIEW`, `WAITING`.
- `artifacts/radar-report.json` có audit của bot/announcement/noise, danh sách decision, và cluster backlog.
- Report chỉ dùng `HV_xxxx`, không xuất `author` gốc trong decisions/clusters.

## Quy tắc quyết định

1. Bot và `@everyone/@here` bị loại trước khi gửi nội dung vào model.
2. Tin gốc được model phân loại theo topic, question, intent-key và confidence.
3. Tin dưới 4 giờ là `WAITING`; không tính tồn đọng.
4. Deadline/quy chế/điểm danh/XP hay low confidence là `NEEDS_TA_REVIEW`.
5. Tin còn lại chỉ là `ANSWERED` nếu model xác nhận reply trong cửa sổ 4 giờ giải đáp trực tiếp; nếu không là `UNANSWERED`.

## Lưu ý demo

CSV fixture không có role Mod/TA. Lõi này vì vậy không khẳng định người trả lời là TA; case rủi ro luôn chuyển review. Bản production cần roster `authorized_responder_ids` từ Discord API/vận hành.

OpenAI Responses API đang được gọi với `store=False` và Structured Outputs (`json_schema`) để output bám schema. Tham khảo [OpenAI API Reference: Create a model response](https://developers.openai.com/api/reference/cli/resources/responses/methods/create).

## Chạy bot trong Discord demo

1. Bật **Message Content Intent** trong Discord Developer Portal → Bot.
2. Bật Discord Developer Mode, copy Server ID và ID của `#general`/`#homework-help`.
3. Điền Server ID, ID của `#general`/`#homework-help`, và ID Summary/Audit vào `.env`. Không đưa các ID vận hành của server vào `.env.example` hoặc GitHub.
4. Nếu `.env` còn placeholder dạng `ID_server_...` / `ID_...`, resolve theo tên server/channel. Lệnh không in token hoặc ID:

```powershell
python src/discord_configure.py
```

5. Kiểm tra kết nối read-only. Lệnh này đăng nhập, kiểm tra guild/channel/quyền rồi tự ngắt; không gửi message:

```powershell
python src/discord_healthcheck.py
```

Kết quả cần thấy: `HEALTHCHECK PASSED`. Nếu thiếu quyền, script ghi rõ channel và quyền còn thiếu.

6. Chạy bot:

```powershell
python src/discord_bot.py
```

Khi terminal in `Logged in as ...`, Discord bot sẽ online. Trong `Mini_Hackathon`, TA dùng `/daily-radar` với:

`/daily-radar` chỉ dùng dữ liệu Discord thật. Chọn `before_hours` để quét N giờ trước thời điểm hiện tại; nếu không có dữ liệu thì bot không đăng bản tin.

Bot đăng summary và tối đa `DISCORD_MAX_CASE_CARDS` case tương tác vào `#ta-daily-summary`. TA có thể nhận case, lưu bản nháp, đánh dấu đã phản hồi, escalation và đổi chủ đề. Với case LIVE, nút `Trả lời nhanh` mở form và gửi reply trực tiếp vào tin gốc sau khi TA xác nhận gửi. Mọi action ghi vào `#radar-audit`; bot không tự reply hoặc DM học viên khi TA chưa thực hiện action này.

`RADAR_ANSWER_SLA_MINUTES` cấu hình thời gian chờ trước khi một câu hỏi vào hàng đợi; mặc định là `240`. Khi kiểm thử UI, có thể tạm đặt `2` và khởi động lại bot.

Trong giai đoạn test, mọi thành viên trong server đã cấu hình đều có thể chạy lệnh và thao tác trên case; chưa bật giới hạn theo role TA/Mod.

## Chạy test

```powershell
python -m unittest discover -s tests -v
```

Test không cần Discord/OpenAI network. `tests/test_discord_ui.py` kiểm tra embed, deep-link và controls; `tests/test_case_store.py` kiểm tra state được lưu lại.
