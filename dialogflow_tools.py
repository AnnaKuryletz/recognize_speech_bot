import os

from dotenv import load_dotenv
from google.cloud import api_keys_v2
from google.cloud.api_keys_v2 import Key
from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, text, language_code, allow_fallback=True):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    if not allow_fallback and response.query_result.intent.is_fallback:
        return None
    return response.query_result.fulfillment_text


def create_api_key(project_id: str, suffix: str) -> Key:
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = f"My first API key - {suffix}"

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    response = client.create_key(request=request).result()

    return response


if __name__ == "__main__":
    load_dotenv()
    project_id = os.environ["PROJECT_ID"]

    session_id = input("Введите session_id (например, 'user1'): ")
    text = input("Введите фразу: ")
    response = detect_intent_texts(project_id, session_id, text, "ru")
    print(f"Ответ DialogFlow: {response}")

