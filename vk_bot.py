import os
import random

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_tools import detect_intent_texts_vk


def echo(event, vk_api):
    message = detect_intent_texts_vk(project_id, event.user_id, event.text, "ru")
    if message:
        vk_api.messages.send(
            user_id=event.user_id, message=message, random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()
    token_vk = os.getenv("VK_API_KEY")
    project_id = os.getenv("PROJECT_ID")
    vk_session = vk.VkApi(token=token_vk)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
