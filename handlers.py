import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext

from run import detect_intent_texts


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Напиши мне что-нибудь.")


def echo(update: Update, context: CallbackContext):
    load_dotenv()
    user_id = update.effective_user.id
    session_id = str(user_id)
    user_input = update.message.text
    language_code = "ru"
    project_id = os.getenv("PROJECT_ID")

    try:
        response = detect_intent_texts(
            project_id, session_id, user_input, language_code
        )
        update.message.reply_text(response)
    except Exception as e:
        update.message.reply_text("Произошла ошибка при обращении к Dialogflow.")
        print(f"[ERROR] {e}")
