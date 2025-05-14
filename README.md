# Text Chatbot with Dialogflow

Этот проект реализует чат-бота для **Telegram** и **VK**, который использует **Google Dialogflow** для обработки пользовательских сообщений. 
Боты снижают нагрузку на администраторов, отвечая на подготовленные заранее вопросы без участия человека.


### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Далее добавьте в папку с проектом файл `.env` и скопируйте туда следующий код:

```
VK_API_KEY=''
TELEGRAM_BOT_TOKEN=''
PROJECT_ID=''
GOOGLE_APPLICATION_CREDENTIALS=''
```

`VK_API_KEY` - необходимо получить на сайте [Devman](https://vk.com/) во вкладке API в настройках созданной группы. 

`TELEGRAM_BOT_TOKEN` - необходимо получить у FatherBot.

`PROJECT_ID` - id проекта, созданного на Dialogflow

`GOOGLE_APPLICATION_CREDENTIALS` - переменная окружения, где лежит путь до файла с ключами от Google, credentials.json. Подробнее читать [здесь](https://cloud.google.com/docs/authentication/api-keys).

### Как включить
Запуск скрипта осуществляется через консоль. 
Телеграм бот:
```
python tg_bot.py
```
ВКонтакте бот:
```
python vk_bot.py
```

Телеграм бот отвечает на каждое сообщение пользователя, а вк, только на те, на которые он обучен. Обучение ботов осуществляется.

### Обучение ботов

Обучение осуществляется через сервис [DialogFlow](https://dialogflow.cloud.google.com/#/login). Так же необходимо создать [агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent), которого нужно подключить к проекту DialogFlow Для автоматизации обучения используйте скрипт `dialog_flow_instruments`. Функция `create_api_key` используется для создания api ключа, а функция `create_intent` для обучения бота. Более подробное описание работы функций можно прочитать [здесь](https://cloud.google.com/dialogflow/es/docs/how/manage-intents#create_intent).


### Цель проекта

Проект создан в образовательных целях.