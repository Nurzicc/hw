# #Повтор первого урока 

# # Модули это файлы с расширением .py

# # Пакеты это папки в которых хранится модули 

# # __init__ - В папке преврощает папку в пакет

# # 3 Вида модулей : Кастомные(это то что мы создаем), вложенные модули(choice, random, sqlite3,), Внешние модули(те модули которые создали другие и выставили в общий доступ )

# # Пакетный менеджер - pip

# # Как скачать aiogram определенной версии, просто пишем pip install aiogram (и тут версия аиограмма),

# # так же можем скачать несколько технологии pip install aiogram dfghj fghjk вот так 

# # git система контроля версии 

# # pip unistall - для удаления технологи, Y - для потверждения 

# # Почему именно aiogram - потому что он асинхронный 

# # telebot - синхронная технология 

# # await - как reply только для асинхронных функции

# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.filters import CommandStart, Command
# import asyncio 
# from config import token

# bot = Bot(token=token) #для связки кода и телеграмм бота 
# dp = Dispatcher()




