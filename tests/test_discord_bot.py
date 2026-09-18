import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from discord_bot import RadarBot  # noqa: E402


class _Response:
    def __init__(self, events):
        self.events = events

    async def defer(self, **kwargs):
        self.events.append(("defer", kwargs))


class _Followup:
    def __init__(self, events):
        self.events = events

    async def send(self, message, **kwargs):
        self.events.append(("followup", message, kwargs))


class DiscordBotTest(unittest.IsolatedAsyncioTestCase):
    async def test_command_is_acknowledged_before_server_scope_check(self):
        events = []
        interaction = SimpleNamespace(
            guild_id=999,
            response=_Response(events),
            followup=_Followup(events),
        )
        bot = SimpleNamespace(settings=SimpleNamespace(discord_guild_id=123))

        await RadarBot.run_daily_radar(
            bot,
            interaction,
            before_hours=24,
        )

        self.assertEqual(events[0][0], "defer")
        self.assertEqual(events[1][0], "followup")
        self.assertTrue(events[1][2]["ephemeral"])

if __name__ == "__main__":
    unittest.main()
