#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""Simple inline keyboard bot with multiple CallbackQueryHandlers.

This Bot uses the Application class to handle the bot.
First, a few callback functions are defined as callback query handler. Then, those functions are
passed to the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging
import types

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
(BACK, FIRST_S, SECOND_S, THIRD_S, FOURTH_S, FIFTH_S, FIRST_T, SECOND_T, THIRD_T, FOURTH_T, FIFTH_T,
 SIXTH_T, SEVENTH_T, EIGHTH_T, NINTH_T, TENTH_T, ELEVENTH_T, TWELFTH_T, THIRTEENTH_T,
 FOURTEENTH_T, FIFTEENTH_T, SIXTEENTH_T, SEVENTEENTH_T, EIGHTEENTH_T, NINTEENTH_T, END) = (
    range(26))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(FIRST_S)),
            InlineKeyboardButton("2", callback_data=str(SECOND_S)),
            InlineKeyboardButton("3", callback_data=str(THIRD_S)),
            InlineKeyboardButton("4", callback_data=str(FOURTH_S)),
            InlineKeyboardButton("6", callback_data=str(FIFTH_S)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text("Выберите комплект",
                                    reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(FIRST_S)),
            InlineKeyboardButton("2", callback_data=str(SECOND_S)),
            InlineKeyboardButton("3", callback_data=str(THIRD_S)),
            InlineKeyboardButton("4", callback_data=str(FOURTH_S)),
            InlineKeyboardButton("6", callback_data=str(FIFTH_S)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    await query.edit_message_text(text="Выберите комплект", reply_markup=reply_markup)
    return START_ROUTES


# async def first_set(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Show new choice of buttons"""
#     query = update.callback_query
#     await query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("1", callback_data=str(TWO)),
#             InlineKeyboardButton("2", callback_data=str(THREE)),
#             InlineKeyboardButton("3", callback_data=str(FOUR)),
#             InlineKeyboardButton("4", callback_data=str(FIVE)),
#             InlineKeyboardButton("6", callback_data=str(SIX)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await query.edit_message_text(
#         text="Выберите комплект", reply_markup=reply_markup
#     )
#     return START_ROUTES


async def first_set(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(FIRST_T)),
            InlineKeyboardButton("2", callback_data=str(SECOND_T)),
            InlineKeyboardButton("3", callback_data=str(THIRD_T)),
            InlineKeyboardButton("4", callback_data=str(FOURTH_T)),
            InlineKeyboardButton("5", callback_data=str(FIFTH_T)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(BACK))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Первый комплект, выберите задание", reply_markup=reply_markup
    )
    return END_ROUTES


async def second_set(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons. This is the end point of the conversation."""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("6", callback_data=str(SIXTH_T)),
            InlineKeyboardButton("7", callback_data=str(SEVENTH_T)),
            InlineKeyboardButton("8", callback_data=str(EIGHTH_T)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(BACK))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Второй комплект, выберите задание", reply_markup=reply_markup
    )
    return END_ROUTES


async def third_set(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("9", callback_data=str(NINTH_T)),
            InlineKeyboardButton("10", callback_data=str(TENTH_T)),
            InlineKeyboardButton("11", callback_data=str(ELEVENTH_T)),
            InlineKeyboardButton("12", callback_data=str(TWELFTH_T)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(BACK))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Третий комплект, выберите задание", reply_markup=reply_markup
    )
    return END_ROUTES


async def fourth_set(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("13", callback_data=str(THIRTEENTH_T)),
            InlineKeyboardButton("14", callback_data=str(FOURTEENTH_T)),
            InlineKeyboardButton("15", callback_data=str(FIFTEENTH_T)),
            InlineKeyboardButton("16", callback_data=str(SIXTEENTH_T)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(BACK))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Четвёртый комплект, выберите задание", reply_markup=reply_markup
    )
    return END_ROUTES


async def sixth_set(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("17", callback_data=str(SEVENTEENTH_T)),
            InlineKeyboardButton("18", callback_data=str(EIGHTEENTH_T)),
            InlineKeyboardButton("19", callback_data=str(NINTEENTH_T)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(BACK))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Шестой комплект, выберите задание", reply_markup=reply_markup
    )
    return END_ROUTES


async def first_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('>')
    return END_ROUTES
# async def first_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Show new choice of buttons"""
#     # query = update.callback_query
#     # await query.answer()
#     #
#     # await query.edit_message_text(text="Шестой комплект, выберите задание")
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("🤓 Экспериментальное задание №17")
#     btn2 = types.KeyboardButton("📖 Ресурсы для подготовки")
#     btn3 = types.KeyboardButton("✍️ О проекте")
#     markup.add(btn1, btn2, btn3)
#     bot.send_message(message.chat.id,
#                      text="Привет, {0.first_name}! "
#                           "Я бот для подготовки к ОГЭ по физике".format(
#                          message.from_user), reply_markup=markup)
#     return END_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5550694022:AAFlilrQkeRHCkA6CMRalFx5YK6YOa5-ueo").build()

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(first_set, pattern="^" + str(FIRST_S) + "$"),
                CallbackQueryHandler(second_set, pattern="^" + str(SECOND_S) + "$"),
                CallbackQueryHandler(third_set, pattern="^" + str(THIRD_S) + "$"),
                CallbackQueryHandler(fourth_set, pattern="^" + str(FOURTH_S) + "$"),
                CallbackQueryHandler(sixth_set, pattern="^" + str(FIFTH_S) + "$"),
                CallbackQueryHandler(first_task, pattern="^" + str(FIRST_T) + "$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(BACK) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(END) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()