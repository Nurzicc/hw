from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text="Повседневные"), KeyboardButton(text="Баскетбольные")],
    [KeyboardButton(text="Коллекция люкс")],
]

keyboard = ReplyKeyboardMarkup(
    keyboard=buttons, resize_keyboard=True, input_field_placeholder="Выберите категорию"
)

regular_shoes = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Jordan 4 Retro"), KeyboardButton(text="ASICS Gel-1130"), KeyboardButton(text="Nike Zoom Vomero 5")]
    ]
)

basketball_shoes = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Nike Kobe 5"), KeyboardButton(text="adidas AE 1"), KeyboardButton(text="Nike Kobe 9 Elite Protro")]
    ]
)

lux_edition = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Louis Vuitton LV Trainer"), KeyboardButton(text="Nike SB Dunk Low"), KeyboardButton(text="Nike Air Skylon 2")]
    ]
)

buttons_accept = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Сделать заказ"), KeyboardButton(text="Отменить выбор")]]
)
