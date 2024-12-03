# import sqlite3
# import random
# import string
# import logging
# from datetime import datetime
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.filters import Command
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from config import token

# # Настройка логирования
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

# # Инициализация бота и базы данных
# bot = Bot(token=token)
# dp = Dispatcher(storage=MemoryStorage())

# conn = sqlite3.connect("visa_card.db", check_same_thread=False)
# cursor = conn.cursor()

# # Создание таблицы для хранения данных пользователей
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     user_id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     passport TEXT,
#     email TEXT,
#     password TEXT,
#     registration_date TEXT
# )
# """)
# conn.commit()

# # Машина состояний для регистрации
# class RegistrationState(StatesGroup):
#     waiting_for_name = State()
#     waiting_for_surname = State()
#     waiting_for_passport = State()
#     waiting_for_email = State()

# # Функция для генерации пароля
# def generate_password(length=8):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# # Главное меню
# def main_menu():
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="📋 Регистрация", callback_data="start_registration")],
#         [InlineKeyboardButton(text="👤 Личный кабинет", callback_data="profile")],
#         [InlineKeyboardButton(text="ℹ️ Команды", callback_data="help")]
#     ])

# # Кнопка "Назад"
# def back_button():
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="⬅️ Назад", callback_data="cancel_registration")]
#     ])

# # Обработчик команды /start
# @dp.message(Command("start"))
# async def start_command(message: types.Message):
#     logger.info(f"Пользователь {message.from_user.id} запустил бота")
#     await message.answer(
#         "👋 Добро пожаловать в систему Visa Card!\n"
#         "Выберите действие или используйте команды:\n"
#         "/start - Запуск бота\n"
#         "/help - Список доступных команд",
#         reply_markup=main_menu()
#     )

# # Обработчик команды /help
# @dp.message(Command("help"))
# async def help_command(message: types.Message):
#     logger.info(f"Пользователь {message.from_user.id} запросил справку")
#     await message.answer(
#         "ℹ️ Список доступных команд:\n"
#         "/start - Запуск бота\n"
#         "/help - Список команд\n"
#         "📋 Регистрация - Заполните свои данные.\n"
#         "👤 Личный кабинет - Просмотр ваших данных.",
#         reply_markup=main_menu()
#     )

# # Начало регистрации
# @dp.callback_query(lambda c: c.data == "start_registration")
# async def start_registration(callback: types.CallbackQuery, state: FSMContext):
#     logger.info(f"Пользователь {callback.from_user.id} начал регистрацию")
#     await callback.message.edit_text("Введите ваше имя:", reply_markup=back_button())
#     await state.set_state(RegistrationState.waiting_for_name)

# # Ввод имени
# @dp.message(F.state == RegistrationState.waiting_for_name)
# async def enter_name(message: types.Message, state: FSMContext):
#     if not message.text or len(message.text.strip()) < 2:
#         await message.answer("❗ Пожалуйста, введите корректное имя (не менее 2 символов).")
#         return
#     await state.update_data(name=message.text.strip())
#     logger.info(f"Пользователь {message.from_user.id} ввёл имя: {message.text}")
#     await message.answer("Введите вашу фамилию:", reply_markup=back_button())
#     await state.set_state(RegistrationState.waiting_for_surname)

# # Ввод фамилии
# @dp.message(F.state == RegistrationState.waiting_for_surname)
# async def enter_surname(message: types.Message, state: FSMContext):
#     if not message.text or len(message.text.strip()) < 2:
#         await message.answer("❗ Пожалуйста, введите корректную фамилию (не менее 2 символов).")
#         return
#     await state.update_data(surname=message.text.strip())
#     logger.info(f"Пользователь {message.from_user.id} ввёл фамилию: {message.text}")
#     await message.answer("Введите номер вашего паспорта:", reply_markup=back_button())
#     await state.set_state(RegistrationState.waiting_for_passport)

# # Ввод номера паспорта
# @dp.message(F.state == RegistrationState.waiting_for_passport)
# async def enter_passport(message: types.Message, state: FSMContext):
#     if not message.text or not message.text.strip().isdigit():
#         await message.answer("❗ Пожалуйста, введите корректный номер паспорта (только цифры).")
#         return
#     await state.update_data(passport=message.text.strip())
#     logger.info(f"Пользователь {message.from_user.id} ввёл номер паспорта: {message.text}")
#     await message.answer("Введите ваш EMAIL:", reply_markup=back_button())
#     await state.set_state(RegistrationState.waiting_for_email)

# # Ввод email
# @dp.message(F.state == RegistrationState.waiting_for_email)
# async def enter_email(message: types.Message, state: FSMContext):
#     if "@" not in message.text or "." not in message.text:
#         await message.answer("❗ Пожалуйста, введите корректный EMAIL.")
#         return
#     user_data = await state.get_data()
#     user_data['email'] = message.text.strip()
#     user_data['password'] = generate_password()
#     user_data['registration_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     cursor.execute("""
#     INSERT INTO users (user_id, name, surname, passport, email, password, registration_date) 
#     VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (message.from_user.id, user_data['name'], user_data['surname'], user_data['passport'],
#           user_data['email'], user_data['password'], user_data['registration_date']))
#     conn.commit()

#     logger.info(f"Пользователь {message.from_user.id} завершил регистрацию: {user_data}")
#     await message.answer(
#         f"✅ Регистрация завершена!\nВаш пароль: {user_data['password']}\n"
#         "Вы можете использовать его для входа в личный кабинет.",
#         reply_markup=main_menu()
#     )
#     await state.clear()

# # Обработчик кнопки "Назад"
# @dp.callback_query(lambda c: c.data == "cancel_registration")
# async def cancel_registration(callback: types.CallbackQuery, state: FSMContext):
#     logger.info(f"Пользователь {callback.from_user.id} отменил регистрацию")
#     await state.clear()
#     await callback.message.edit_text("❌ Регистрация отменена. Выберите действие:", reply_markup=main_menu())

# # Личный кабинет
# @dp.callback_query(lambda c: c.data == "profile")
# async def view_profile(callback: types.CallbackQuery):
#     cursor.execute("SELECT name, surname, passport, email, registration_date FROM users WHERE user_id = ?", (callback.from_user.id,))
#     user = cursor.fetchone()
#     if user:
#         profile_text = (f"👤 Ваши данные:\n"
#                         f"Имя: {user[0]}\n"
#                         f"Фамилия: {user[1]}\n"
#                         f"Номер паспорта: {user[2]}\n"
#                         f"EMAIL: {user[3]}\n"
#                         f"Дата регистрации: {user[4]}")
#         logger.info(f"Пользователь {callback.from_user.id} просмотрел профиль")
#         await callback.message.edit_text(profile_text, reply_markup=main_menu())
#     else:
#         logger.info(f"Пользователь {callback.from_user.id} попытался зайти в профиль без регистрации")
#         await callback.message.edit_text("❌ Вы ещё не зарегистрированы.", reply_markup=main_menu())

# async def main():
#     try:
#         await dp.start_polling(bot)
#     finally:
#         await bot.session.close()

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
