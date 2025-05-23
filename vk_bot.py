import os
import random

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_tools import detect_intent_texts

def handle_vk_message(event, vk_api):
    session_id = f"vk-{event.user_id}"  
    message = detect_intent_texts(
        project_id, session_id, event.text, "ru", allow_fallback=False
    )
    if message:
        vk_api.messages.send(
            user_id=event.user_id,
            message=message,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()
    token_vk = os.environ["VK_API_KEY"]
    project_id = os.environ["PROJECT_ID"]
    vk_session = vk.VkApi(token=token_vk)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_vk_message(event, vk_api, project_id)
