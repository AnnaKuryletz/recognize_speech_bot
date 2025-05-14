import vk_api
from dotenv import load_dotenv
import os
from vk_api.longpoll import VkLongPoll, VkEventType


load_dotenv()
token_vk=os.getenv("VK_API_KEY")
vk_session = vk_api.VkApi(token=token_vk)

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')
        if event.to_me:
            print('Для меня от: ', event.user_id)
        else:
            print('От меня для: ', event.user_id)
        print('Текст:', event.text)