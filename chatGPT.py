import openai
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
    message = "".join(response.choices[0].text.split("\n\n")[1:])
    return message

    # if ":" in message:
    #     final_message.replace(".", "\n")
    # if len(message) == 1:
    #     final_message = message[0]
    # elif message.startswith("!"):
    #     final_message = f"{message[1:].lstrip('!')}"
    # else:
    #     final_message = f'{"".join(message)}'


