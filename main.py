import telebot
from telebot import types  # для указания типов
from small.config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤓 Экспериментальное задание №17")
    btn2 = types.KeyboardButton("📖 Ресурсы для подготовки")
    btn3 = types.KeyboardButton("✍️ О проекте")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! "
                          "Я бот для подготовки к ОГЭ по физике".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "🤓 Экспериментальное задание №17":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("О задании")
        btn2 = types.KeyboardButton("Решения 19 типов этого задания")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Что Вас интересует?",
                         reply_markup=markup)

    elif message.text == "О задании":
        bot.send_message(message.chat.id, "Описание задания")

    elif message.text == "Решения 19 типов этого задания":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Видео с решением")
        btn2 = types.KeyboardButton("Текстовая инструкция")
        btn3 = types.KeyboardButton("Таблица анализа условия задания")
        btn4 = types.KeyboardButton("Пример оформления решения на бланке")
        btn5 = types.KeyboardButton("Рисунок/схема")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выберите интересующий ресурс",
                         reply_markup=markup)

    elif message.text == "Видео с решением":
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_first = types.InlineKeyboardButton(text='1', callback_data='video')
        # И добавляем кнопку на экран
        keyboard.add(key_first)
        key_second = types.InlineKeyboardButton(text='2',
                                                callback_data='video')
        keyboard.add(key_second)
        key_third = types.InlineKeyboardButton(text='3', callback_data='video')
        keyboard.add(key_third)
        key_fourth = types.InlineKeyboardButton(text='4',
                                                callback_data='video')
        keyboard.add(key_fourth)
        key_fifth = types.InlineKeyboardButton(text='5', callback_data='video')
        keyboard.add(key_fifth)
        key_sixth = types.InlineKeyboardButton(text='6', callback_data='video')
        keyboard.add(key_sixth)
        key_seventh = types.InlineKeyboardButton(text='7',
                                                 callback_data='video')
        keyboard.add(key_seventh)
        key_eighth = types.InlineKeyboardButton(text='8',
                                                callback_data='video')
        keyboard.add(key_eighth)
        key_ninth = types.InlineKeyboardButton(text='9', callback_data='video')
        keyboard.add(key_ninth)
        key_kozerog = types.InlineKeyboardButton(text='10-19',
                                                 callback_data='video')
        keyboard.add(key_kozerog)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака',
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Ссылка на видео")

    elif message.text == "Текстовая инструкция":
        bot.send_message(message.chat.id, "Текст инструкции")

    elif message.text == "Таблица анализа условия задания":
        bot.send_message(message.chat.id, "Таблица анализа условия задания")

    elif message.text == "Пример оформления решения на бланке":
        bot.send_message(message.chat.id,
                         "Пример оформления решения на бланке")

    elif message.text == "Рисунок/схема":
        bot.send_message(message.chat.id, "Ссылка на рисунок/схему")

    elif message.text == "📖 Ресурсы для подготовки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Для ОГЭ")
        btn2 = types.KeyboardButton("Источники для изучения физики")
        btn3 = types.KeyboardButton("Полезные приложения и сайты для учебы")
        btn4 = types.KeyboardButton("Учебники по физике (углубленные)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Выберите интересующий ресурс",
                         reply_markup=markup)

    elif message.text == "Для ОГЭ":
        bot.send_message(message.chat.id, "Что-то для ОГЭ")

    elif message.text == "Источники для изучения физики":
        bot.send_message(message.chat.id, text="Какие-то источники для "
                                               "изучения физики")

    elif message.text == "Полезные приложения и сайты для учебы":
        bot.send_message(message.chat.id, text="Какие-то полезные приложения "
                                               "и сайты для учебы")

    elif message.text == "Учебники по физике (углубленные)":
        bot.send_message(message.chat.id, text="Какие-то учебники по физике "
                                               "(углубленные)")
    elif message.text == "✍️ О проекте":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Описание проекта",
                         reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤓 Экспериментальное задание №17")
        btn2 = types.KeyboardButton("📖 Ресурсы для подготовки")
        btn3 = types.KeyboardButton("✍️ О проекте")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         text="На такую комманду я не запрограммировал..")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = '123'
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True)
