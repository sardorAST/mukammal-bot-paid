from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍 Mahsulotlar'),
            KeyboardButton(text="‼ Qo'llanma")
        ],
        [],
    ],
    resize_keyboard=True

)