import time
import requests
from config import JOKES_URL, HEADERS
from utils import SpeakText, play_sound


def dad_joke():
    response = requests.get(JOKES_URL, headers=HEADERS)
    SpeakText(response.json()['body'][0]['setup'])
    time.sleep(0.3)
    SpeakText(response.json()['body'][0]['punchline'])
    play_sound("assets/haha.mp3")
