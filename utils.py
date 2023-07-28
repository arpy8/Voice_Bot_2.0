import os
import gtts
import playsound
import pyautogui as pg
import speech_recognition as sr

r = sr.Recognizer()


def custom_call(source):
    audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        pass


def custom_listen():
    try:
        with sr.Microphone(device_index=3) as source:
            text = custom_call(source)
            if not None: return text
    except AttributeError:
        with sr.Microphone(device_index=1) as source:
            text = custom_call(source)
            if not None: return text



def play_sound(path):
    playsound.playsound(path)


def SpeakText(text, lang="en"):
    sound = gtts.gTTS(str(text), lang=lang, tld="us")
    sound.save("assets/temp.mp3")
    playsound.playsound("assets/temp.mp3")
    os.remove("assets/temp.mp3")


def speak_print(text, skip="", only_speak=False, skip_skip_value_while_printing=False):
    if skip_skip_value_while_printing:
        print(text)
    if skip in text:
        text = text.replace(skip, "")
    text = text.replace("\n", "")
    text = text.replace("Bot: ", "")
    if not only_speak:
        print(text)
    SpeakText(text)


def whatsapp_close_tab():
    pg.hotkey('alt', 'f4')
    pg.hotkey('alt', 'tab')
    pg.hotkey('ctrl', 'w')


def close_application():
    pg.hotkey("alt", "f4")


def shutdown():
    pg.hotkey('ctrl', 'win', 'd')
    pg.hotkey('alt', 'f4')
    pg.press('enter')
