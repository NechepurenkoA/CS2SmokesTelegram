import asyncio

from create_bot import bot, dp
from handlers import lineups_router, start_router
from logger import configure_logging


async def main():
    dp.include_router(start_router)
    dp.include_router(lineups_router)
    configure_logging()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
