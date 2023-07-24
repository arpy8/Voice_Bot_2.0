import openai
from utils import speak_print
from config import PREDEFINED_PROMPT, GPT_KEY

openai.api_key = GPT_KEY


def chatGPT(USER_PROMPT, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=str(PREDEFINED_PROMPT) + str(USER_PROMPT),
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7
    )
    message = "".join(response.choices[0].text.split('\n\n'))
    final_message = message

    if ":" in message:
        final_message.replace(".", "\n")
    if len(message) == 1:
        final_message = f"{message[0].strip()}"
    elif message.startswith("!"):
        final_message = f"{message[2:].strip()}"
    else:
        final_message = f"{message[1:].strip()}"

    return final_message


