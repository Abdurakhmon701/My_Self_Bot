from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Расскажи о себе', callback_data='answer'),
        ],

    ],
)

cases = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Кейсы', callback_data='cases'),
        ],

    ],
)

next = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Следующий', callback_data='next'),
        ],

    ],
)

contacts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Контакты', callback_data='contacts'),
        ],

    ],
)