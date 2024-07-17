from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


async def get_start_kb():
    buttons = [[KeyboardButton(text="Search")]]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return kb


async def get_compare_button(button_url:str):
    buttons = [[InlineKeyboardButton(text="Compare the price", web_app=WebAppInfo(url=button_url))]]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
