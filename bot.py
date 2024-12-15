import asyncio
import nest_asyncio
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = "7544228898:AAE_tpUGhahtR9OLtD1eB3_aSBqGypWXn4M"

# Функція обробки команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [
        ['Посилання', 'Меню 2'],
        ['Меню 3', 'Меню 4']
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text("Вітаю! Оберіть опцію з меню нижче або введіть /menu для доступу до інлайн-меню:", reply_markup=reply_markup)

# Функція обробки команди /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Посилання", callback_data="menu_1"),
         InlineKeyboardButton("Меню 2", callback_data="menu_2")],
        [InlineKeyboardButton("Меню 3", callback_data="menu_3"),
         InlineKeyboardButton("Меню 4", callback_data="menu_4")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Виберіть опцію з інлайн-меню:", reply_markup=reply_markup)

# Обробник текстових клавіш
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    if user_input == "Посилання":
        await update.message.reply_text(
            "Ось кілька посилань:\n"
            "1. [IT_College](https://it-college.kh.ua/)\n"
            "2. [Курс Основи програмування](https://few-scourge-629.notion.site/Python-1010ecd5aa3e809fb7d0ea3d7b6d913d?pvs=74)\n"
            "3. [Курс WEB програмування](https://few-scourge-629.notion.site/WEB-6948750be01e49ac9bf1a6bbbaa4f872?pvs=74)"
        )
    elif user_input == "Меню 2":
        await update.message.reply_text(
            "Меню 2: оберіть ресурс:\n"
            "1. [VirusTotal](https://www.virustotal.com/gui/home/upload)\n"
            "2. [Google Docs](https://docs.google.com/document/u/0/)"
        )
    elif user_input == "Меню 3":
        await update.message.reply_text(
            "Меню 3: оберіть ресурс:\n"
            "1. [Google Classroom](https://classroom.google.com/u/0/h?hl=ru)"
        )
    elif user_input == "Меню 4":
        await update.message.reply_text(
            "Меню 4: оберіть ресурс:\n"
            "1. [Discord](https://discord.com)"
        )

# Обробник інлайн-кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu_1":
        await query.edit_message_text(text="Ви обрали Посилання")
        keyboard = [
            [InlineKeyboardButton("IT_College", url="https://it-college.kh.ua/")],
            [InlineKeyboardButton("Курс Основи програмування", url="https://few-scourge-629.notion.site/Python-1010ecd5aa3e809fb7d0ea3d7b6d913d?pvs=74")],
            [InlineKeyboardButton("Курс WEB програмування", url="https://few-scourge-629.notion.site/WEB-6948750be01e49ac9bf1a6bbbaa4f872?pvs=74")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Виберіть одне з посилань:", reply_markup=reply_markup)

    elif query.data == "menu_2":
        await query.edit_message_text(text="Ви вибрали Меню 2")
        keyboard = [
            [InlineKeyboardButton("VirusTotal", url="https://www.virustotal.com/gui/home/upload")],
            [InlineKeyboardButton("Google Docs", url="https://docs.google.com/document/u/0/")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Виберіть одне з посилань:", reply_markup=reply_markup)

    elif query.data == "menu_3":
        await query.edit_message_text(text="Ви вибрали Меню 3")
        keyboard = [
            [InlineKeyboardButton("Google Classroom", url="https://classroom.google.com/u/0/h?hl=ru")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Виберіть посилання:", reply_markup=reply_markup)

    elif query.data == "menu_4":
        await query.edit_message_text(text="Ви вибрали Меню 4")
        keyboard = [
            [InlineKeyboardButton("Discord", url="https://discord.com")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Виберіть посилання:", reply_markup=reply_markup)

# Налаштування логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Застосування nest_asyncio для роботи з існуючим циклом подій
nest_asyncio.apply()

# Основна функція для запуску бота
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    await application.bot.delete_webhook(drop_pending_updates=True)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(MessageHandler(filters.TEXT, menu_handler))
    application.add_handler(CallbackQueryHandler(button_handler))

    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())