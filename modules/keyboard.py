from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


post = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Принять", callback_data="agree"),
            InlineKeyboardButton(text="❌ Отклонить", callback_data="disagree")
        ],
    ]
)
