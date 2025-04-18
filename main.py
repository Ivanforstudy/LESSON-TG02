import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()




@dp.message(Command('help'))
async def help_command(message:Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')



@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')

@dp.message(F.photo)
async def react_photo(message: Message):
		list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
		await bot.download(message.photo[-1],destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)





async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())