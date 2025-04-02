from uuid import uuid4

from aiogram import Bot, Router
from aiogram.types import InlineQuery, InlineQueryResultPhoto

from tgbot.config import Config

router = Router()


@router.inline_query()
async def inline_query_handler(inline_query: InlineQuery, config: Config):
    uuid = uuid4()

    results = [
        InlineQueryResultPhoto(
            id=uuid.hex,
            photo_url=f"{config.api.api_url}/generate?uuid={uuid.hex}",
            thumbnail_url=f"{config.api.api_url}/generate?uuid={uuid.hex}",
            photo_width=1524,
            photo_height=1024,
        )
    ]

    await inline_query.answer(results, is_personal=True, cache_time=1)
