from aiogram import Router, types
from aiogram.filters import Text
from keyboards import regular_shoes, buttons_accept
from texts import info_jordan, info_asics, info_nike_vomero, info_kobe_5, info_adidas, info_kobe9, info_luivit, info_dunkk, info_skulon

router = Router()

@router.message(Text("Повседневные"))
async def command_regular(message: types.Message):
    await message.answer("В наличии: ", reply_markup=regular_shoes)

@router.message(Text("Jordan 4 Retro"))
async def command_jordan(message: types.Message):
    await message.reply_photo(photo="'https://spikeprague.cz/cdn/shop/files/eb020bfedc19497fc8266bf91ee3ce05_700x700.webp?v=1727947987")
    await message.answer(info_jordan)
    await message.answer("Цена: 85$", reply_markup=buttons_accept)

@router.message(Text("ASICS Gel-1130"))
async def command_asics(message: types.Message):
    await message.reply_photo(photo="https://www.freesoulz.nl/cdn/shop/files/asics-gel-1130-white-black-724065.jpg?v=1725547494&width=2048")
    await message.answer(info_asics)
    await message.answer("Цена: 95$", reply_markup=buttons_accept)

@router.message(Text("Nike Zoom Vomero 5"))
async def command_nike(message: types.Message):
    await message.reply_photo(photo="https://www.sneakerhype.eu/cdn/shop/products/nike-zoom-vomero-5-photon-dust-metallic-silver-w-sneakerhype-2.webp?v=1731074702")
    await message.answer(info_nike_vomero)
    await message.answer("Цена: 92$", reply_markup=buttons_accept)
