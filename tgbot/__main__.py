import asyncio
import logging
import sys

import coloredlogs
from aiogram import Bot, Dispatcher
from aiohttp import web
from PIL import Image, ImageFont

from tgbot.config import Config, parse_config
from tgbot.handlers import get_handlers_router
from tgbot.services.api.generate import handle_generate


async def run_site(config: Config):
    config._cached_background = Image.open(config.settings.background_path).convert("RGB")
    config._cached_font = ImageFont.truetype(config.settings.font_path, size=52)
    with open(config.settings.parables_path) as file:
        config._parables_list = file.read().strip().splitlines()

    web_app = web.Application()

    web_app.add_routes([
        web.get("/generate", lambda req: handle_generate(config, req))
    ])

    runner = web.AppRunner(web_app)

    await runner.setup()

    site = web.TCPSite(
        runner=runner,
        host=config.web.listen_ip,
        port=config.web.listen_port
    )

    await site.start()


async def on_startup(dispatcher: Dispatcher, bot: Bot, config: Config):
    bot_info = await bot.get_me()

    logging.info(f"Name - {bot_info.full_name}")
    logging.info(f"Username - @{bot_info.username}")
    logging.info(f"ID - {bot_info.id}")

    logging.debug(f"Groups Mode - {bot_info.can_join_groups}")
    logging.debug(f"Privacy Mode - {not bot_info.can_read_all_group_messages}")
    logging.debug(f"Inline Mode - {bot_info.supports_inline_queries}")
    
    if not bot_info.supports_inline_queries:
        logging.error(f"Privacy Mode for bot @{bot_info.username} is not enabled! Exiting...")
        await bot.session.close()
        sys.exit(1)

    logging.error("Bot started!")

    asyncio.create_task(
        run_site(config)
    )


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    logging.warning("Stopping bot...")
    await dispatcher.fsm.storage.close()
    await bot.session.close()


async def main():
    coloredlogs.install(level=logging.INFO)

    router = get_handlers_router()
    config = parse_config("config.toml")
    dp = Dispatcher()

    bot = Bot(config.bot.token)

    dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    await dp.start_polling(bot, config=config)


if __name__ == "__main__":
    asyncio.run(main())
