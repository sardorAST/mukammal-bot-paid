from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback,book_callback

#1 - usul
categoryMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/telegram/")
        ],
        [
            InlineKeyboardButton(text="🔍Qidirish", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan")
        ],
    ]
)

#Kurslar uchun Keyboard
coursesMenu = InlineKeyboardMarkup(row_width=1)
python = InlineKeyboardButton(text="🐍 Python Dasturlash asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌐 Django web dasturlash", callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="📟 Mukammal telegram bot", callback_data=course_callback.new(item_name="telegram"))
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(text="📈 Ma'lumotlar tuzulmasi va Algoritmlar", callback_data=course_callback.new(item_name='algorithm'))
coursesMenu.insert(algorithm)


back_button = InlineKeyboardButton(text="🔙 Ortga ", callback_data="cancel")
coursesMenu.insert(back_button)

# 3- usul

books = {
    "Python. Dasturlash asoslari":"python_book",
    "C++. Dasturlash asoslari ":"cpp_book",
    "Mukammal dasturlash. JavaScript":"js_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key,callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)

# har bir kurs uchun tugma

telegram_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/" )
        ],
    ],
)

algorithm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar")
        ],
    ],
)











