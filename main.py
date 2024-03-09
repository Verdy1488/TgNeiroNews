import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hlink
from aiogram.utils.media_group import MediaGroupBuilder, InputMediaType

from modules import neiro
from modules import keyboard

token = '*'

bot = Bot(token=token)
dp = Dispatcher()

answer_text = None
media = None


async def main():
    await dp.start_polling(bot)


@dp.message()
async def neiro_message(message: Message):
    global answer_text, media

    first = await message.answer('Сообщение в обработке...')
    answer_text = f'{neiro.get_answer(message.text or message.caption)}\n\n{hlink("🎮 Ultimate News. Подписаться.", "t.me/ultimatevlk")}'

    media = MediaGroupBuilder(caption=answer_text)

    if message.photo:
        photo = message.photo[-1]
        media.add(type=InputMediaType.PHOTO, media=photo.file_id)
    if message.video:
        video = message.video
        media.add(type=InputMediaType.VIDEO, media=video.file_id)

    await message.answer(answer_text, parse_mode="HTML", reply_markup=keyboard.post)
    await first.delete()


@dp.callback_query(F.data == 'agree')
async def neiro_callback(query: CallbackQuery):
    global media

    media_group = media.build()

    await query.message.answer("Отправлено!")

    await bot.send_media_group(chat_id=-1002085439347, media=media_group)


asyncio.run(main())
