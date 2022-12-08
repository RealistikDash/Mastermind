from __future__ import annotations

import random
from typing import Optional

from mastermind.config import config
from mastermind.music.constants import MusicErrors
from mastermind.music.constants import PlayOrder
from mastermind.music.song import Song


class Queue:
    __slots__ = (
        "songs",
        "current_song",
        "order",
    )

    def __init__(self, order: PlayOrder) -> None:
        self.songs: list[Song] = []
        self.current_song: Optional[Song] = None
        self.order = order

    def __len__(self) -> int:
        return len(self.songs)

    @property
    def empty(self) -> bool:
        return len(self.songs) == 0

    def end_current_song(self) -> None:
        if self.current_song is None:
            return None

        self.songs.remove(self.current_song)
        self.current_song = None

    def start_new_song(self, song: Song) -> None:
        self.current_song = song

    def add_song(self, song: Song) -> MusicErrors:
        if len(self.songs) >= config.music_playlist_capacity:
            return MusicErrors.PLAYLIST_CAPACITY_EXCEEDED

        self.songs.append(song)
        if self.current_song is None:
            self.current_song = song

        return MusicErrors.SUCCESS

    def remove_song_by_index(self, index: int) -> MusicErrors:
        if index >= len(self.songs):
            return MusicErrors.PLAYLIST_SONG_NOT_IN_QUEUE

        if self.current_song is self.songs[index]:
            self.end_current_song()

        del self.songs[index]
        return MusicErrors.SUCCESS

    def next_song(self) -> Optional[Song]:
        self.end_current_song()

        if self.empty:
            return None

        if self.order is PlayOrder.SHUFFLE:
            new_song = random.choice(self.songs)
            self.start_new_song(new_song)
        elif self.order is PlayOrder.REPEAT:
            if self.current_song is None:
                self.start_new_song(self.songs[0])
            else:
                self.start_new_song(self.current_song)

        elif self.order is PlayOrder.SEQUENTIAL:
            self.start_new_song(self.songs[0])

        return self.current_song
