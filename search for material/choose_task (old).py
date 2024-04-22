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

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

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
(BACK, FIRST, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN,
 TWELVE, THIRTEEN, FOURTEEN, FIFTEEN, SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN,
 TWENTY, TWENTYONE, TWENTYTWO, TWENTYTHREE, TWENTYFOUR, TWENTYFIVE) = (
    range(25))


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
            InlineKeyboardButton("1", callback_data=str(FIRST)),
            InlineKeyboardButton("2", callback_data=str(THREE)),
            InlineKeyboardButton("3", callback_data=str(FOUR)),
            InlineKeyboardButton("4", callback_data=str(FIVE)),
            InlineKeyboardButton("6", callback_data=str(SIX)),
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
            InlineKeyboardButton("1", callback_data=str(FIRST)),
            InlineKeyboardButton("2", callback_data=str(THREE)),
            InlineKeyboardButton("3", callback_data=str(FOUR)),
            InlineKeyboardButton("4", callback_data=str(FIVE)),
            InlineKeyboardButton("6", callback_data=str(SIX)),
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
            InlineKeyboardButton("1", callback_data=str(SEVEN)),
            InlineKeyboardButton("2", callback_data=str(EIGHT)),
            InlineKeyboardButton("3", callback_data=str(NINE)),
            InlineKeyboardButton("4", callback_data=str(TEN)),
            InlineKeyboardButton("5", callback_data=str(ELEVEN)),
            InlineKeyboardButton("Назад", callback_data=str(BACK)),
        ]
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
            InlineKeyboardButton("6", callback_data=str(TWELVE)),
            InlineKeyboardButton("7", callback_data=str(THIRTEEN)),
            InlineKeyboardButton("8", callback_data=str(FOURTEEN)),
            InlineKeyboardButton("Назад", callback_data=str(BACK)),
        ]
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
            InlineKeyboardButton("9", callback_data=str(FIFTEEN)),
            InlineKeyboardButton("10", callback_data=str(SIXTEEN)),
            InlineKeyboardButton("11", callback_data=str(SEVENTEEN)),
            InlineKeyboardButton("12", callback_data=str(EIGHTEEN)),
            InlineKeyboardButton("Назад", callback_data=str(BACK)),
        ]
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
            InlineKeyboardButton("13", callback_data=str(NINETEEN)),
            InlineKeyboardButton("14", callback_data=str(TWENTY)),
            InlineKeyboardButton("15", callback_data=str(TWENTYONE)),
            InlineKeyboardButton("16", callback_data=str(TWENTYTWO)),
            InlineKeyboardButton("Назад", callback_data=str(BACK)),
        ]
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
            InlineKeyboardButton("17", callback_data=str(TWENTYTHREE)),
            InlineKeyboardButton("18", callback_data=str(TWENTYFOUR)),
            InlineKeyboardButton("19", callback_data=str(TWENTYFIVE)),
            InlineKeyboardButton("Назад", callback_data=str(BACK)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Шестой комплект, выберите задание", reply_markup=reply_markup
    )
    return END_ROUTES


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
    application = Application.builder().token("TOKEN").build()

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
                CallbackQueryHandler(first_set, pattern="^" + str(FIRST) + "$"),
                CallbackQueryHandler(second_set, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(third_set, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(fourth_set, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(sixth_set, pattern="^" + str(SIX) + "$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(BACK) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(FIRST) + "$"),
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