from __future__ import annotations

from mastermind import logger
from mastermind.config import config
from mastermind.init_bot import bot


def main() -> int:
    logger.init_logging(config.log_level)
    logger.info("Mastermind is starting up...")

    bot.run(config.app_token)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
