# import logging
# import asyncio
# import sqlite3

# from aiogram import Bot, Dispatcher, types, F
# from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import CommandStart
# from aiogram import Router

# # Инициализация
# router = Router()
# bot = Bot(token='7839930317:AAFnKEP-rraQdaEZ8M0LZMS21qW4D8YYxWE')
# dp = Dispatcher()

# # Команды бота
# command = [BotCommand(command="start", description="Начать")]

# # Кнопки
# buttons = [
#     [KeyboardButton(text="Добавить задачу"), KeyboardButton(text="Показать задачи")],
#     [KeyboardButton(text="Очистить список")],
# ]
# keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Выберите кнопку")

# inline_button = [
#     [InlineKeyboardButton(text="Подтвердить", callback_data="confirm_clear")],
#     [InlineKeyboardButton(text="Отменить", callback_data="cancel_clear")],
# ]
# inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_button)

# # База данных
# connect = sqlite3.connect("to_do_list.db")
# cursor = connect.cursor()

# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     telegram_user INTEGER UNIQUE
# )
# """
# )

# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS tasks (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     task TEXT,
#     user_id INTEGER,
#     FOREIGN KEY (user_id) REFERENCES users (id)
# )
# """
# )
# connect.commit()

# def register_user(telegram_user):
#     cursor.execute("INSERT OR IGNORE INTO users (telegram_user) VALUES (?)", (telegram_user,))
#     connect.commit()

# def add_task(telegram_user, task):
#     cursor.execute("SELECT id FROM users WHERE telegram_user = ?", (telegram_user,))
#     user_id = cursor.fetchone()
#     if user_id:
#         cursor.execute("INSERT INTO tasks (task, user_id) VALUES (?, ?)", (task, user_id[0]))
#         connect.commit()

# def get_tasks(telegram_user):
#     cursor.execute(
#         """
#         SELECT tasks.id, tasks.task 
#         FROM tasks 
#         JOIN users ON tasks.user_id = users.id 
#         WHERE users.telegram_user = ?
#         """,
#         (telegram_user,),
#     )
#     return cursor.fetchall()

# def delete_all_tasks(telegram_user):
#     cursor.execute(
#         """
#         DELETE FROM tasks WHERE user_id = (
#             SELECT id FROM users WHERE telegram_user = ?
#         )
#         """,
#         (telegram_user,),
#     )
#     connect.commit()

# def tasks_buttons(tasks):
#     markup = InlineKeyboardMarkup()
#     for task_id, task_text in tasks:
#         button_text = " ".join(task_text.split()[:2])
#         markup.add(InlineKeyboardButton(text=button_text, callback_data=f"task_{task_id}"))
#     return markup

# @router.message(CommandStart())
# async def command_start(message: types.Message):
#     register_user(message.from_user.id)
#     await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=keyboard)

# @router.message(F.text == "Добавить задачу")
# async def ask_task(message: types.Message):
#     await message.answer("Введите содержание задачи:")

# @router.message(lambda msg: msg.text not in ["Добавить задачу", "Показать задачи", "Очистить список"])
# async def save_task(message: types.Message):
#     add_task(message.from_user.id, message.text)
#     await message.answer("Задача добавлена!", reply_markup=keyboard)

# @router.message(F.text == "Показать задачи")
# async def show_tasks(message: types.Message):
#     tasks = get_tasks(message.from_user.id)
#     if tasks:
#         await message.answer("Ваши задачи:", reply_markup=tasks_buttons(tasks))
#     else:
#         await message.answer("Список задач пуст.")

# @router.message(F.text == "Очистить список")
# async def confirm_clear_list(message: types.Message):
#     await message.answer("Вы уверены?", reply_markup=inline_keyboard)

# @router.callback_query(F.data == "confirm_clear")
# async def clear_tasks(callback: types.CallbackQuery):
#     delete_all_tasks(callback.from_user.id)
#     await callback.message.edit_text("Список задач очищен.")

# @router.callback_query(F.data == "cancel_clear")
# async def cancel_clear(callback: types.CallbackQuery):
#     await callback.message.edit_text("Очистка отменена.")

# async def main():
#     logging.basicConfig(level=logging.INFO)
#     dp.include_router(router)
#     await bot.set_my_commands(command)
#     await dp.start_polling(bot)

# try:
#     asyncio.run(main())
# except KeyboardInterrupt:
#     print("Выход")

import asyncio 
from aiogram import Bot, Dispatcher, Router, F, types  # Импортируем необходимые модули aiogram
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup  # Работа с клавиатурой
from aiogram.filters import Command  # Для обработки команды /start
from aiogram.fsm.context import FSMContext  # Контекст FSM (Finite State Machine)
from aiogram.fsm.state import State, StatesGroup  # Определение состояний
from aiogram.fsm.storage.memory import MemoryStorage  # Используем хранилище в памяти
import logging  # Для логирования

logging.basicConfig(level=logging.INFO)  # Настраиваем логирование
buttons = [  # Определяем кнопки для клавиатуры
    [KeyboardButton(text='Подтвердить'), KeyboardButton(text='Отменить')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)  # Создаём клавиатуру

storage = MemoryStorage()  # Инициализируем хранилище для состояний
dp = Dispatcher(storage=storage)  # Создаём диспетчер и связываем его с хранилищем
bot = Bot(token='7839930317:AAFnKEP-rraQdaEZ8M0LZMS21qW4D8YYxWE')  # Создаём объект бота с токеном


class Data(StatesGroup):  # Определяем группу состояний для работы с заметками
    waiting_for_note_date = State()  # Состояние ожидания заголовка заметки
    waiting_for_note_content = State()  # Состояние ожидания содержимого заметки
    
@dp.message(Command('start'))  # Обработчик команды /start
async def startt(message: types.Message, state: FSMContext):
    first_name = message.from_user.first_name  # Получаем имя пользователя
    await message.answer(f'Привет, {first_name}!\n\n Введи заголовок заметки:')  # Отправляем приветственное сообщение
    await state.set_state(Data.waiting_for_note_date)  # Переводим пользователя в состояние ожидания заголовка заметки
    
@dp.message(Data.waiting_for_note_date)  # Обработчик ввода заголовка заметки
async def set_note_title(message: types.Message, state: FSMContext):
    await message.answer('Введи содержимое заметки:')  # Просим ввести содержимое заметки
    await state.update_data(note_title=message.text)  # Сохраняем заголовок заметки в состояние
    await state.set_state(Data.waiting_for_note_content)  # Переводим пользователя в состояние ожидания содержимого заметки

@dp.message(Data.waiting_for_note_content)  # Обработчик ввода содержимого заметки
async def set_note_content(message: types.Message, state: FSMContext):
    await state.update_data(note_content=message.text)  # Сохраняем содержимое заметки в состояние
    user_data = await state.get_data()  # Извлекаем все данные из состояния
    note_title = user_data.get('note_title')  # Получаем заголовок заметки
    note_content = user_data.get('note_content')  # Получаем содержимое заметки
    
    await message.answer(  # Отправляем пользователю сообщение с кнопками подтверждения или отмены
        f'Подтвердите сохранение заметки:\n\nЗаголовок: {note_title}\nСодержимое: {note_content}',
        reply_markup=keyboard  # Клавиатура с кнопками
    )
    
@dp.message(F.text == 'Подтвердить')  # Обработчик нажатия кнопки "Подтвердить"
async def confirm(message: types.Message, state: FSMContext):
    data = await state.get_data()  # Извлекаем данные из состояния
    note_title = data.get('note_title')  # Получаем заголовок заметки
    note_content = data.get('note_content')  # Получаем содержимое заметки

    await message.answer(  # Подтверждаем сохранение заметки
        f'Заметка сохранена:\n\nЗаголовок: {note_title}\nСодержимое: {note_content}'
    )
    await state.clear()  # Очищаем состояние после сохранения

@dp.message(F.text == 'Отменить')  # Обработчик нажатия кнопки "Отменить"
async def cancel(message: types.Message, state: FSMContext):
    await message.answer('Заметка удалена.')  # Сообщаем об отмене
    await state.clear()  # Очищаем состояние

async def main():  # Основная функция для запуска бота
    await dp.start_polling(bot)  # Запускаем long polling

if __name__ == '__main__':  # Точка входа в программу
    asyncio.run(main())  # Запускаем бота


