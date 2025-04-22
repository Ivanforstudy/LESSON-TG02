import asyncio
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
from gtts import gTTS
import os

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(Command('doc'))
async def doc(message: Message):
	doc = FSInputFile("Возврат.bmp")
	await bot.send_document(message.chat.id, doc)




@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('Desireless - John.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('Д З ОР09.mp4')
    await bot.send_video(message.chat.id, video)


@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1:\\n1. Скручивания: 3 подхода по 15 повторений\\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2:\\n1. Подъемы ног: 3 подхода по 15 повторений\\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3:\\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
   tts = gTTS(text=rand_tr, lang='ru')
   tts.save(training.ogg)
   audio = FSInputFile('1718883178_sample4.ogg')
   await bot.send_voice(message.chat.id, audio)
   os.remove("1718883178_sample4.ogg")


@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("1718883178_sample4.ogg")
    await message.answer_voice(voice)


@dp.message(Command('help'))
async def help_command(message:Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /video \n /audio')



@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Зачетный Кошак!', 'Классный котик!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

    # Скачивание фотографии
    photo = message.photo[-1]  # Получаем самое качественное фото
    file_path = f'tmp/{photo.file_id}.jpg'  # Путь для сохранения
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')


@dp.message()
async def start(message:Message):
    if message.text.lower() == 'test':
        await message.answer('Тестируем')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())