from __future__ import annotations

import discord

from mastermind.discord.state import SharedState


class Mastermind(discord.Client):
    state: SharedState

    def __init__(self, state: SharedState, intents: discord.Intents, **options) -> None:
        super().__init__(intents=intents, **options)
        self.state = state
