from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SharedState:
    ...

    @staticmethod
    def default() -> SharedState:
        return SharedState()
