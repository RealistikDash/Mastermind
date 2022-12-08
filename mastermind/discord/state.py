from __future__ import annotations

from copy import copy
from dataclasses import dataclass
from typing import Optional


@dataclass
class ServerConfiguration:
    channel_song_listen: Optional[int] = None  # TODO: Use discord.TextChannel


@dataclass
class SharedState:
    server_configurations: dict[int, ServerConfiguration]

    @staticmethod
    def default() -> SharedState:
        return SharedState(
            server_configurations={},
        )

    def ensure_server_configuration(self, server_id: int) -> ServerConfiguration:
        config = self.server_configurations.get(server_id)

        if config is None:
            config = ServerConfiguration()
            self.server_configurations[server_id] = config

        return copy(config)

    def set_server_configuration(
        self,
        server_id: int,
        config: ServerConfiguration,
    ) -> None:
        self.server_configurations[server_id] = config
