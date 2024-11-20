from aiogram import Router, types
from aiogram.filters import Text
from keyboards import lux_edition, buttons_accept
from texts import info_jordan, info_asics, info_nike_vomero, info_kobe_5, info_adidas, info_kobe9, info_luivit, info_dunkk, info_skulon


router = Router()

@router.message(Text("Коллекция люкс"))
async def command_luxury(message: types.Message):
    await message.answer("В наличии: ", reply_markup=lux_edition)

@router.message(Text("Louis Vuitton LV Trainer"))
async def command_luivit(message: types.Message):
    await message.reply_photo(photo="https://ru.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8-lv-trainer-%D0%BE%D0%B1%D1%83%D0%B2%D1%8C--BQ9U1PPC31_PM1_Side%20view.jpg")
    await message.answer(info_luivit)
    await message.answer("Цена: 1397$", reply_markup=buttons_accept)


@router.message(Text("Nike SB Dunk Low'"))
async def command_luivit(message: types.Message):
    await message.reply_photo(photo="https://img.brandshop.ru/cache/products/m/muzhskie-krossovki-nike-sb-x-diamond-supply-co-dunk-low-pro-og-qs-white-chrome-black-tropical-twist-3_1104x1104.jpg")
    await message.answer(info_dunkk)
    await message.answer("Цена: 1345$", reply_markup=buttons_accept)
    
@router.message(Text("Nike Air Skylon 2"))
async def command_luivit(message: types.Message):
    await message.reply_photo(photo="https://ru.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8-lv-trainer-%D0%BE%D0%B1%D1%83%D0%B2%D1%8C--BQ9U1PPC31_PM1_Side%20view.jpg")
    await message.answer(info_skulon)
    await message.answer("Цена: 137$", reply_markup=buttons_accept)