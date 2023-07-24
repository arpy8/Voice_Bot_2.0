import time
import pyttsx3
import numpy as np
import pyautogui as pg
import speech_recognition as sr
from misc import contact_extractor
from message import send_whatsapp

r = sr.Recognizer()
engine = pyttsx3.init("dummy")
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
name = "Arpit"
greetings = [f"Hello Mr. {name}",
             "yeah?",
             "Well, hello there, Master of Puns and Jokes - how's it going today?",
             f"Ahoy there, Captain {name}! How's the ship sailing?",
             f"Bonjour, Monsieur {name}! Comment ça va? Wait, why the hell am I speaking French?"]


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
            print(text.lower().split(" "))
            if "hey" or "hi" or "hello" or "over" in text.lower().split():
                print("Wake word detected.")
                engine.say(greetings[0])
                engine.runAndWait()
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass


def listen_and_respond(source):
    while True:
        audio = r.listen(source)
        try:
            print("Listening...")
            text = r.recognize_google(audio)
            text_list = text.split()
            print(f"You : {text}")

# --------  CONDITIONS GOES HERE --------
            if not text:
                continue
            if "pause" in text_list:
                listen_for_wake_word(source)
            if not audio:
                listen_for_wake_word(source)

            if "write" or "type" in text_list:
                pg.write(text)
            elif "whatsapp" or "contact" in text_list:
                phone = contact_extractor(text)
                if phone == "None":
                    print("Invalid contact")
                print("speak your message")
                send_whatsapp(phone, custom_call(source))
            else:
                print(text)
        except sr.UnknownValueError:
            time.sleep(2)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()
            listen_for_wake_word(source)
            break


with sr.Microphone(device_index=3) as source:
    listen_for_wake_word(source)
