import logging

from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, booksMenu, telegram_keyboard
from aiogram.types import Message, CallbackQuery
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Mahsulot tanlang",reply_markup=categoryMenu)


@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.answer("Kursni tanlang", reply_markup=coursesMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="books")
async def buy_books(call: CallbackQuery):
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

#CallbackData yordamida filtrlash
@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida userdan qaytgan callbackni ko'ramiz
    logging.info(f"{callback_data =}")


    await call.message.answer(f"Siz Mukammal Telegram Bot kursini tanladingiz.",
                              reply_markup=telegram_keyboard)

    await call.answer(cache_time=60)

@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurutmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_callback.filter(item_name="cpp_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurutmangiz qabul qilindi", cache_time=60, show_alert=True)

@dp.callback_query_handler(book_callback.filter(item_name="js_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurutmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    #Oynada javob qaytaramiz
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()




