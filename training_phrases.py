import json
import os
import argparse
from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_text):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)

    training_phrases = []
    for part_text in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=part_text)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_text])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )
    print(f"Интент '{display_name}' успешно создан.")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Создание интента в Dialogflow.")
    parser.add_argument("--file", default="questions.json", help="Путь к JSON-файлу с фразами.")
    parser.add_argument("--topic", required=True, help="Тема диалога в файле.")
    parser.add_argument("--intent-name", required=True, help="Имя создаваемого интента.")

    args = parser.parse_args()

    project_id = os.environ["PROJECT_ID"]

    try:
        with open(args.file, "r", encoding="utf8") as file:
            questions = json.load(file)
    except FileNotFoundError:
        print(f"Файл {args.file} не найден.")
        return

    if args.topic not in questions:
        print(f"Тема '{args.topic}' не найдена в файле.")
        return

    topic_data = questions[args.topic]
    training_phrases = topic_data["questions"]
    message_text = topic_data["answer"]

    create_intent(project_id, args.intent_name, training_phrases, message_text)


if __name__ == "__main__":
    main()
