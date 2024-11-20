from aiogram import Router, types
from aiogram.filters import Text

router = Router()

@router.message(Text("Сделать заказ"))
async def command_accept(message: types.Message):
    await message.reply("Заказ оформлен, спасибо за обращение :)")

@router.message(Text("Отменить выбор"))
async def command_cancel(message: types.Message):
    await message.reply("Заказ отменен, спасибо за обращение :)")
