from telegram import *
from telegram.ext import *

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот. Как дела?')

# Обработчик команды /help
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Я бот. Чем могу помочь?')

# Обработчик текстовых сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Обработчик неизвестных команд
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Извините, я не понимаю эту команду.")

def main():
    # Токен вашего бота от BotFather
    updater = Updater("5550694022:AAFlilrQkeRHCkA6CMRalFx5YK6YOa5-ueo")

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(None, echo))

    # Регистрируем обработчик неизвестных команд
    dp.add_handler(MessageHandler(None, unknown))

    # Запускаем бота
    updater.start_polling()

    # Остановить бота, когда нажимаем Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
