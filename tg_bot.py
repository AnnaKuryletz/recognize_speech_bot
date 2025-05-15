import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters

from handlers import start, handle_telegram_message


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    project_id = os.environ["PROJECT_ID"]

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    def handler_with_project_id(update, context):
        return handle_telegram_message(update, context, project_id)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handler_with_project_id))

    updater.start_polling()
    updater.idle()
