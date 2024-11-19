import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from config import token

bot = Bot(token=token)
dp = Dispatcher()

it_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend'), KeyboardButton(text='Ux-Ui')],
    [KeyboardButton(text='Android Developer'), KeyboardButton(text='Ios Developer')]
    ], one_time_keyboard=True)

buttons = [
    [KeyboardButton(text='Повседневные'), KeyboardButton(text='Баскетбольные')],
    [KeyboardButton(text='Коллекция люкс')]]

casual_shoes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Jordan 4 Retro'), KeyboardButton('ASICS Gel-1130'), KeyboardButton('Nike Zoom Vomero 5')]])

basketball_shoes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Nike Kobe 5'), KeyboardButton(text='adidas AE 1'), KeyboardButton(text='Nike Kobe 9 Elite Protro')]])

lux_edition = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Louis Vuitton LV Trainer'), KeyboardButton(text='')]])
keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')
