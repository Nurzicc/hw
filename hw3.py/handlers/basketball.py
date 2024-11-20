from aiogram import Router, types
from aiogram.filters import Text
from keyboards import basketball_shoes, buttons_accept
from texts import info_jordan, info_asics, info_nike_vomero, info_kobe_5, info_adidas, info_kobe9, info_luivit, info_dunkk, info_skulon


router = Router()

@router.message(Text("Баскетбольные"))
async def command_basketball(message: types.Message):
    await message.answer("В наличии: ", reply_markup=basketball_shoes)

@router.message(Text("Nike Kobe 5"))
async def command_kobe_5(message: types.Message):
    await message.reply_photo(photo="URL_IMAGE_KOBE_5")
    await message.answer(info_kobe_5)
    await message.answer("Цена: 181$", reply_markup=buttons_accept)


@router.message(Text("adidas AE 1"))
async def command_kobe_5(message: types.Message):
    await message.reply_photo(photo="https://www.basketballemotion.com/imagesarticulos/223344/grandes/zapatillas-adidas-a.e.-1-cloud-white-core-black-green-spark-0.webp")
    await message.answer(info_adidas)
    await message.answer("Цена: 77$", reply_markup=buttons_accept)
    

@router.message(Text("Nike Kobe 9 Elite Protro"))
async def command_kobe_5(message: types.Message):
    await message.reply_photo(photo="https://images2.minutemediacdn.com/image/upload/c_crop,w_900,h_506,x_0,y_134/c_fill,w_1440,ar_16:9,f_auto,q_auto,g_auto/images/voltaxMediaLibrary/mmsport/kicks/01j5rgefnrpv45cdxdg7.jpg")
    await message.answer(info_kobe9)
    await message.answer("Цена: 130$", reply_markup=buttons_accept)
# Аналогично для других баскетбольных кроссовок
