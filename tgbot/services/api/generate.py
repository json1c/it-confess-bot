import random
from asyncio import to_thread
from io import BytesIO

from aiohttp import web
from PIL import Image, ImageDraw, ImageFont

from tgbot.config import Config


def generate_image_bytes(text: str, background: Image.Image, font: ImageFont.FreeTypeFont):
    img = background.copy()
    draw = ImageDraw.Draw(img)

    text_color = (0xf7, 0xe7, 0xd8)

    max_width = img.width // 2 - 60  # ширина текста (только правая часть)
    x_start = img.width // 2 + 20    # сдвиг вправо от центра
    y = 240  # начальная высота

    text_color = (0xf7, 0xe7, 0xd8)

    # Автоматический перенос текста по ширине
    words = text.split()
    line = ""
    lines = []

    for word in words:
        test_line = line + " " + word if line else word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)

    # Рисуем каждую строку
    for line in lines:
        draw.text((x_start, y), line, font=font, fill=text_color)
        y += 50

    # В память, не в файл
    output = BytesIO()
    img.save(output, format="JPEG", quality=85)
    output.seek(0)

    return output


def get_random_parable(parables: list):
    return random.choice(parables)


async def handle_generate(config: Config, request: web.Request):
    text = get_random_parable(config._parables_list)

    image_bytes = await to_thread(
        generate_image_bytes,
        text,
        config._cached_background,
        config._cached_font
    )

    return web.Response(body=image_bytes.read(), content_type="image/jpg")
