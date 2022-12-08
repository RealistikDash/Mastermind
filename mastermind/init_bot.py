from __future__ import annotations

import discord

from mastermind import logger
from mastermind.config import config
from mastermind.discord.client import Mastermind
from mastermind.discord.state import SharedState


def init_bot() -> Mastermind:
    intents = discord.Intents.default()
    intents.message_content = True

    state = SharedState.default()

    bot = Mastermind(intents=intents, state=state)

    @bot.event
    async def on_ready() -> None:
        assert bot.user is not None
        logger.info(
            f"Mastermind has successfully logged in as {bot.user.name} ({bot.user.id})!",
        )

    return bot


bot = init_bot()
