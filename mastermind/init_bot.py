from __future__ import annotations

import discord

from mastermind import logger
from mastermind.config import config
from mastermind.discord.client import Mastermind
from mastermind.discord.state import SharedState


async def init_cogs(bot: Mastermind) -> None:
    from mastermind.music.cog import MusicCog

    await bot.add_cog(MusicCog(bot))


def init_bot() -> Mastermind:
    intents = discord.Intents.default()
    intents.message_content = True

    state = SharedState.default()

    bot = Mastermind(
        intents=intents,
        state=state,
        command_prefix=config.commands_prefix,
    )

    @bot.event
    async def on_ready() -> None:
        assert bot.user is not None
        logger.info(
            f"Mastermind has successfully logged in as {bot.user.name} ({bot.user.id})!",
        )

        # Cog initialisation must be done in an event loop.
        await init_cogs(bot)

        logger.info("Mastermind is ready to go!")

    return bot


bot = init_bot()
