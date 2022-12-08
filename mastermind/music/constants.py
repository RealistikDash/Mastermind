from __future__ import annotations

from enum import auto
from enum import IntEnum


class PlayOrder(IntEnum):
    SEQUENTIAL = 0
    SHUFFLE = 1
    REPEAT = 2

    def __str__(self) -> str:
        return self.name.lower()


class MusicErrors(IntEnum):
    SUCCESS = auto()
    PLAYLIST_CAPACITY_EXCEEDED = auto()
    PLAYLIST_SONG_NOT_IN_QUEUE = auto()
