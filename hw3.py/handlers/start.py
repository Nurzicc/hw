from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards import keyboard

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer("Вас приветствует магазин StockX!", reply_markup=keyboard)
    await message.answer("Выберите пожалуйста категорию:")
