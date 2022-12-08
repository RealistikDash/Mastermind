from __future__ import annotations

from typing import Union

import discord
from discord.ext import commands

from mastermind.config import config
from mastermind.discord.client import Mastermind
from mastermind.music.constants import MusicErrors
from mastermind.music.queue import Queue
from mastermind.music.song import Song


class MusicCog(commands.Cog, name="Music"):
    def __init__(self, bot: Mastermind) -> None:
        self.bot = bot
        self.queues: dict[int, Queue] = {}

    def ensure_queue(self, server_id: int) -> Queue:
        queue = self.queues.get(server_id)

        if queue is None:
            queue = Queue()
            self.queues[server_id] = queue

        return queue

    def add_song(self, server_id: int, song: Song) -> MusicErrors:
        existed_prior = server_id in self.queues
        queue = self.ensure_queue(server_id)
        # Capacity validation
        if len(queue) >= config.music_playlist_capacity:
            return MusicErrors.PLAYLIST_FULL

        queue.add_song(song)
        return MusicErrors.SUCCESS

    def remove_song_by_index(
        self,
        server_id: int,
        index: int,
    ) -> Union[MusicErrors, Song]:
        queue = self.queues.get(server_id)
        if queue is None:
            return MusicErrors.PLAYLIST_NOT_CREATED

        # Index validation
        if index < 0 or index >= len(queue):
            return MusicErrors.PLAYLIST_SONG_NOT_IN_QUEUE

        song = queue.remove_song_by_index(index)

        if index == 0:
            return self.next_song(server_id)

        return song

    def next_song(self, server_id: int) -> Union[MusicErrors, Song]:
        queue = self.queues.get(server_id)
        if queue is None:
            return MusicErrors.PLAYLIST_NOT_CREATED

        res = queue.next_song()
        if res is None:
            return MusicErrors.PLAYLIST_EMPTY

        # TODO: Play the next song
        return res

    def destroy_queue(self, server_id: int) -> Union[MusicErrors, Queue]:
        if server_id not in self.queues:
            return MusicErrors.PLAYLIST_NOT_CREATED

        queue = self.queues.pop(server_id)
        return queue
