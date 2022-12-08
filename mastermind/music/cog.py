from __future__ import annotations

import discord
from discord.ext import commands

from mastermind.discord.client import Mastermind
from mastermind.music.constants import MusicErrors
from mastermind.music.queue import Queue
from mastermind.music.song import Song


class MusicCog(commands.Cog, name="Music"):
    def __init__(self, bot: Mastermind) -> None:
        self.bot = bot
        self.queues: dict[int, Queue] = {}
