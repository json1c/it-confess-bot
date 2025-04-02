from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def cancel() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🚫 Отмена", callback_data="cancel_state")
            ]
        ]
    )
