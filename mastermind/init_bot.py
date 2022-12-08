from __future__ import annotations

import discord

from mastermind import logger
from mastermind.config import config


def init_bot() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready() -> None:
        assert bot.user is not None
        logger.info(
            f"Mastermind has successfully logged in as {bot.user.name} ({bot.user.id})!",
        )

    return bot


bot = init_bot()
