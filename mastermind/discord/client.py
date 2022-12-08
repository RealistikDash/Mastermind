from __future__ import annotations

import discord.ext.commands

from mastermind.discord.state import SharedState


class Mastermind(discord.ext.commands.Bot):
    state: SharedState

    def __init__(
        self,
        state: SharedState,
        intents: discord.Intents,
        command_prefix: str,
        **options,
    ) -> None:
        super().__init__(intents=intents, **options, command_prefix=command_prefix)
        self.state = state
