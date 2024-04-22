from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "5550694022:AAFlilrQkeRHCkA6CMRalFx5YK6YOa5-ueo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет!\ Напишите пожалуйста что-нибудь в чате (^-^'')~ ")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)