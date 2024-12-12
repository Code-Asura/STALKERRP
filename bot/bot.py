import asyncio
import logging

from aiogram import Bot, Dispatcher

from data import config
from handlers import includer

async def main() -> None:
    bot = Bot(config.token.get_secret_value())
    dp = Dispatcher()

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger.info("Bot started")

    await includer(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stoped")