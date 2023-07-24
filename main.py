import random

import pyttsx3
from utils import *
from config import *
from camera import *
from message import *
import pyautogui as pg
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init("dummy")
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
GREETINGS = [f"Hello Mr. {NAME}",
             "yeah?",
             "Well, hello there, Master of Puns and Jokes - how's it going today?",
             f"Ahoy there, Captain {NAME}! How's the ship sailing?",
             f"Bonjour, Monsieur {NAME}! Comment ça va? Wait, why the hell am I speaking French?"]


def custom_call(source):
    audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        pass


def listen_for_wake_word(source):
    print("Listening for 'Hey'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_list = [word.lower() for word in text.lower().split()]
            print(text_list)
            if "hey" or "hi" or "hello" or "over" in text_list:
                print("Wake word detected.")
                SpeakText(random.choice(GREETINGS))
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass


def listen_and_respond(source):
    r = sr.Recognizer()

    while True:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You: {text}")

            if not text:
                continue

            text_list = text.split()

            if "pause" in text_list:
                speak_print("Session paused\n")
                listen_for_wake_word(source)

            if not audio:
                listen_for_wake_word(source)

            if "write" in text_list or "type" in text_list:
                pg.write(text)

            elif "whatsapp" in text.lower() or "contact" in text.lower():
                phone = contact_extractor(text)
                if phone is None:
                    print("Invalid contact")
                else:
                    speak_print("What message should I send?")
                    send_whatsapp(phone, custom_call(source))
                    speak_print("Message sent successfully.\n")

            elif "camera" in text_list or "click" in text_list:
                speak_print("Opening camera\n")
                click_picture()

            elif "gallery" in text_list:
                speak_print("Opening gallery\n")
                open_gallery()

            else:
                # gonna embed chatgpt here
                speak_print(text)

        except sr.UnknownValueError:
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            listen_for_wake_word(source)
            break


with sr.Microphone(device_index=1) as source:
    listen_for_wake_word(source)
