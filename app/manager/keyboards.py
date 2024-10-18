from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Відправьте свій номер', request_contact=True)]],
                                 resize_keyboard=True)
