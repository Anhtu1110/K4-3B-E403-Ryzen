# CP3 · Chạy lõi AI thật

`src/radar.py` là lõi demo: dữ liệu CSV → rule filter/reply graph → OpenAI semantic classification → report JSON ẩn danh. Nó **không** gửi message hay cần Discord API thật.

## Cài và chạy

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
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
4. Chạy:

```powershell
python src/discord_bot.py
```

Khi terminal in `Logged in as ...`, Discord bot sẽ online. Trong `Mini_Hackathon`, TA dùng `/daily-radar hours:24`. Bot chỉ post summary ẩn danh vào `#ta-daily-summary` và log count vào `#radar-audit`; không tự reply hoặc DM học viên.
