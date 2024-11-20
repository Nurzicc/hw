# # from aiogram import Bot, Dispatcher, types, F
# # from aiogram.types import Message
# # from aiogram.filters import CommandStart, Command
# # import asyncio
# # from config import token
# # import random


# # bot = Bot(token=token)
# # dp = Dispatcher()

# # @dp.message(CommandStart())
# # async def start(message : Message):
# #     await message.answer('Привет, я загадал число от 1 до 3, угадайте :)')
    
# # @dp.message()
# # async def ramdom(message : types.Message):
# #     try:
# #         number = random.choice(1,3)
# #         user_num=int(message.text)
# #         if user_num > 3:
# #             await message.answer('Число введено не корректно, пожалуйста выберите число от 1 до 3') 
            
# #         elif number == user_num:
# #             await message.reply_photo(photo='https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
# #             await message.answer(f'Вы угадали заданное число:({number})')
# #             await message.answer(f'Выберите еще')
        
# #         else:
# #             await message.reply_photo(photo='https://media.makeameme.org/created/sorry-you-lose.jpg')
# #             await message.reply(f'Вы проиграли :( заданное число: ({number})')
# #             await message.answer(f'Загадайте еще :)')
# #     except ValueError:
# #         await message.answer(f'Некоректный ввод')
    
# # async def main():
# #         await dp.start_polling(bot)

# # try:
# #     asyncio.run(main())
# # except KeyboardInterrupt:
# #     print('Выход')

# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import CommandStart
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from config import token
# from aiogram import Router


# bot = Bot(token=token)
# dp = Dispatcher()
# router = Router()

# buttons = [
#     [KeyboardButton(text='Повседневные'), KeyboardButton(text='Баскетбольные')],
#     [KeyboardButton(text='Коллекция люкс')]
# ]

# casual_shoes = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text='Jordan 4 Retro'), KeyboardButton(text='ASICS Gel-1130'), KeyboardButton(text='Nike Zoom Vomero 5')]],
#     resize_keyboard=True
# )

# basketball_shoes = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text='Nike Kobe 5'), KeyboardButton(text='adidas AE 1'), KeyboardButton(text='Nike Kobe 9 Elite Protro')]],
#     resize_keyboard=True
# )

# lux_edition = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text='Louis Vuitton LV Trainer'), KeyboardButton(text='Nike SB Dunk Low'), KeyboardButton(text='Nike Air Skylon 2')]],
#     resize_keyboard=True
# )

# keyboard = ReplyKeyboardMarkup(
#     keyboard=buttons,
#     resize_keyboard=True,
#     input_field_placeholder='Выберите кнопку'
# )

# dp.include_router(router)

# @router.message(CommandStart())
# async def command_start(message: types.Message):
#     await message.answer('Приветствую вас! Выберите категорию:', reply_markup=keyboard)

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
