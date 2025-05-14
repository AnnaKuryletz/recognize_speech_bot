import json
import os

from dotenv import load_dotenv


def create_intent(project_id, display_name, training_phrases_parts, message_text):
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_text])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


if __name__ == "__main__":
    load_dotenv()
    project_id = os.getenv("PROJECT_ID")

    with open("questions.json", "r", encoding="utf8") as my_file:
        questions_json = my_file.read()

    questions = json.loads(questions_json)

    work_questions = questions["Устройство на работу"]["questions"]
    work_answer = questions["Устройство на работу"]["answer"]

    create_intent(
        project_id, "Как устроиться к вам на работу", work_questions, work_answer
    )
