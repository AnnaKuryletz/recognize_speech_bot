import os

from telegram.ext import CommandHandler, MessageHandler, Updater, Filters

from handlers import start, handle_telegram_message


def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_telegram_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
