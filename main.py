import asyncio
import logging
import sys

from aiogram import F, html

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from aiogram.exceptions import TelegramForbiddenError

from odm_files.crud import save_user, get_all_users, change_user_status
from bot_app.bot_init import bot, dp
from bot_app.key_boards import get_open_browser
from keyboards import get_start_kb, get_compare_button
from parsers import search_user_query
from states import Form


# Bot token can be obtained via https://t.me/BotFather


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    data = {'first_name': message.from_user.first_name, 'last_name': message.from_user.last_name,
            'language': message.from_user.language_code, 'chat_id': message.from_user.id}
    await save_user(data)
    await message.reply(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=await get_start_kb())


@dp.message(F.text == 'Search')
async def search_handler(message: Message, state: FSMContext) -> None:
    print('Start search handler')
    await message.answer('Type the name of the item: ')
    await state.set_state(Form.title)

@dp.message(Form.title)
async def process_title(message: Message, state: FSMContext) -> None:
    print('Start process title')
    await state.update_data(name=message.text)
    print(f'Message Text: {message.text}')
    await state.clear()
    products = await search_user_query(message.text)
    for product in products:
        caption = f'{product.get("title")}\n{product.get("price")}'
        await bot.send_photo(chat_id=message.from_user.id, photo=product.get('img'), caption=caption,
                             reply_markup= await get_compare_button(product.get('compare')))


@dp.message(F.text.lower() == 'exit')
async def exit_handler(message: Message) -> None:
    await message.answer(f"Good bye {message.from_user.first_name}")
@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def send_notification(text:str):
    users = await get_all_users()
    print(f"User count = {len(users)}")
    for user in users:
        try:
            await bot.send_message(chat_id=user.chat_id, text=text,
                reply_markup= await get_open_browser(link='https://www.google.com/'))
        except TelegramForbiddenError:
            await change_user_status(chat_id=user.chat_id, status=False)

async def main() -> None:
    await send_notification(text='Simple notification')
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())