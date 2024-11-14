from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
from config import token
import random


bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message : Message):
    await message.answer('Привет, я загадал число от 1 до 3, угадайте :)')
    
@dp.message()
async def ramdom(message : types.Message):
    try:
        number = random.choice(1,3)
        user_num=int(message.text)
        if user_num > 3:
            await message.answer('Число введено не корректно, пожалуйста выберите число от 1 до 3') 
            
        elif number == user_num:
            await message.reply_photo(photo='https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
            await message.answer(f'Вы угадали заданное число:({number})')
            await message.answer(f'Выберите еще')
        
        else:
            await message.reply_photo(photo='https://media.makeameme.org/created/sorry-you-lose.jpg')
            await message.reply(f'Вы проиграли :( заданное число: ({number})')
            await message.answer(f'Загадайте еще :)')
    except ValueError:
        await message.answer(f'Некоректный ввод')
    
async def main():
        await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Выход')

