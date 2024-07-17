from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import MenuButtonWebApp, WebAppInfo

async def get_open_browser(link: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Visit site",url=link )
    builder.button(text='Open site', web_app=WebAppInfo(url=link))
    return builder.as_markup()