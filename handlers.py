import os

from telegram import Update
from telegram.ext import CallbackContext

from dialogflow_tools import detect_intent_texts  


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Напиши мне что-нибудь.")


def handle_telegram_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session_id = str(user_id)
    user_input = update.message.text
    language_code = "ru"
    project_id = os.environ["PROJECT_ID"] 

    try:
        response = detect_intent_texts(
            project_id, session_id, user_input, language_code
        )
        if response:
            update.message.reply_text(response)
        else:
            update.message.reply_text("Извините, я не понял ваш вопрос.")
    except Exception as e:
        update.message.reply_text("Произошла ошибка при обработке вашего запроса.")
