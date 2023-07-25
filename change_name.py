import requests
import toml
import speech_recognition as sr

from config import GENDER_URL
from utils import speak_print, custom_call


def get_gender(new_name):
    data = requests.get(GENDER_URL + new_name).json()
    if data['gender'] == "female":
        return "Ms."
    elif data['gender'] == "male":
        return 'Mr.'
    else:
        return ''


def update_name():
    speak_print("Okay what shall I call you?")
    with sr.Microphone() as source:
        new_name = custom_call(source)

    existing_data = toml.load(open("assets/name.toml", 'r'))
    existing_data["NAME"] = new_name
    toml.dump(existing_data, open("assets/name.toml", 'w'))

    speak_print(f"Sure thing, I shall call you {get_gender(new_name)} {new_name} from now on.")


update_name()