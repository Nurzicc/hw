import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from config import token

#ReplyKeyboardMarkup - Собирает клавиатуру

bot = Bot(token=token)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='Направления'), KeyboardButton(text='Контакты')],
    [KeyboardButton(text='О нас')]
]


it_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend'), KeyboardButton(text='Ux-Ui')],
    [KeyboardButton(text='Android Developer'), KeyboardButton(text='Ios Developer')]
    ], one_time_keyboard=True)



# it_keyboard = ReplyKeyboardMarkup(input_field_placeholder='Выберите кнопку:')
keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')

@dp.message(CommandStart())
async def command_start(message: types.Message):\
    await message.answer('Приветствую вас :)', reply_markup=keyboard)
    
async def main():
        await dp.start_polling(bot)

@dp.message(F.text == 'О нас')
async def command_about(message: types.Message):
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6lkqYtQ1s_EQNAI_pdjiP20sQjk-gdTCldQ&s')
    await message.answer('''Международная IT-академия Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию. В данный момент более 1200 студентов в возрасте от 12 до 45 лет изучают здесь программирование, дизайн и английский язык. Филиальная сеть образовательного центра представлена в таких городах, как Бишкек, Ош, Ташкент и Кара-Балта. ''')

@dp.message(F.text == 'Направления')
async def command_it(message: types.Message):
    await message.answer('Выберите направление:', reply_markup=it_keyboard)


@dp.message(F.text == 'Backend')
async def command_backend(message: types.Message):
    await message.answer_photo(photo='https://c8.alamy.com/comp/2DB193X/back-end-icon-simple-element-from-website-development-collection-filled-back-end-icon-for-templates-infographics-and-more-2DB193X.jpg',)
    await message.answer('''Бэкенд-разработчик — это программист, который работает над внутренней частью веб-ресурсов. Он пишет код, разрабатывает бизнес-логику веб-приложений, задает им алгоритм работы и обеспечивает корректное выполнение пользовательских запросов.''')
    await message.answer('Стоимость этого направление составляет: 12000 сом')
    await message.answer('Время обучения этого направление состовляет: 5 месяцев')
    
@dp.message(F.text == 'Frontend')
async def commannd_front(message: types.Message):
    await message.answer_photo(photo='https://camo.githubusercontent.com/9d6c5d72431a9b20da7515f6b5389dcb68416c437acc96020f62939d47174332/68747470733a2f2f63646e2e7261776769742e636f6d2f7368616e6e6f6e6d6f656c6c65722f66726f6e742d656e642d6c6f676f2f6d61737465722f6578706f7274732f66726f6e742d656e642d6c6f676f2d62772e706e67')
    await message.answer('Frontend-разработчик — это специалист, который занимается разработкой пользовательского интерфейса, то есть той части сайта или приложения, которую видят посетители страницы. Главная задача фронтенд разработчика — перевести готовый дизайн-макет в код так, чтобы все работало правильно.')
    await message.answer('Стоимость этого направление составляет: 12000 сом')
    await message.answer('Время обучения этого направление состовляет: 5 месяцев')
    
@dp.message(F.text == 'Ux-Ui')
async def command_uxui(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdKvOhH1iOUmdb9mVoQmLkUjbSRNzQ9WaCpQ&s')
    await message.answer('UX/UI-дизайнер – IT-специалист, проектирующий и разрабатывающий пользовательский интерфейс приложений, сайтов, программ. В работе анализирует и опирается на пользовательский опыт.')    
    await message.answer('Стоимость этого направление составляет: 12000 сом')
    await message.answer('Время обучения этого направление состовляет: 4 месяца')
    
@dp.message(F.text == 'Android Developer')
async def command_android(message: types.Message):
    await message.answer_photo(photo='https://www.google.com/imgres?q=andriod%20developer%20logo&imgurl=https%3A%2F%2Fwww.clipartmax.com%2Fpng%2Fmiddle%2F349-3495654_now-we-have-developers-as-customers-android-app-development-logo.png&imgrefurl=https%3A%2F%2Fwww.clipartmax.com%2Fmiddle%2Fm2H7G6A0Z5d3m2d3_now-we-have-developers-as-customers-android-app-development-logo%2F&docid=6xhWKcxCaZ8Z7M&tbnid=mOMfyYxD-9DxuM&vet=12ahUKEwjfk8ijw-iJAxXWFxAIHQ4gDl0QM3oECFwQAA..i&w=840&h=578&hcb=2&ved=2ahUKEwjfk8ijw-iJAxXWFxAIHQ4gDl0QM3oECFwQAA')
    await message.answer('Android-разработчик — это программист, который специализируется на создании мобильных приложений для операционной системы Android. Он разрабатывает приложения с использованием языков программирования Java и Kotlin, интегрирует различные API, работает с базами данных и оптимизирует приложения для разных устройств.')
    await message.answer('Стоимость этого направление составляет: 12000 сом')
    await message.answer('Время обучения этого направление состовляет: 7 месяцев')
    
@dp.message(F.text == 'Ios Developer')  
async def command_ios(message: types.Message):
    await message.answer_photo(photo='https://developer.apple.com/news/images/og/apple-developer-og-twitter.png')
    await message.answer('iOS-разработчик создает приложения для устройств Apple. Это не только iPhone, но и iPad, Apple Watch и другие гаджеты, входящие в экосистему. Он не только пишет код и работает над интерфейсом, но и занимается поддержкой приложения, адаптацией его под разные модели устройств, тестированием и исправлением багов.   ')
    await message.answer('Стоимость этого направление составляет: 12000 сом')
    await message.answer('Время обучения этого направление состовляет: 7 месяцев')
    
@dp.message(F.text == 'Контакты')
async def command_contact(message: types.Message):
    await message.answer_contact(phone_number='+996557052018', last_name='It', first_name='Geeks')
    
    
if __name__ == "__main__":
    asyncio.run(main())


