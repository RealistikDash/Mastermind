from __future__ import annotations

import discord
from discord.ext import commands

from mastermind.discord.client import Mastermind


class MusicCog(commands.Cog, name="Music"):
    def __init__(self, bot: Mastermind) -> None:
        self.bot = bot
