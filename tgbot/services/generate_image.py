from PIL import Image, ImageDraw, ImageFont


def generate_image_with_teaching(teaching, background_path="batya.png", font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    img = Image.open(background_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, size=50)

    max_width = img.width // 2 - 60  # ширина текста (только правая часть)
    x_start = img.width // 2 + 20    # сдвиг вправо от центра
    y = 140  # начальная высота

    # Цвет текста в hex -> RGB
    text_color = (0xf7, 0xe7, 0xd8)

    # Автоматический перенос текста по ширине
    words = teaching.split()
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
        y += 50  # отступ между строками

    output_path = "blessed_result.png"
    img.save(output_path)
    return output_path


# Пример использования
generate_image_with_teaching("Не забывай, если открыл доступ к базе из мира, на проде узнаешь цену своей лени.")
