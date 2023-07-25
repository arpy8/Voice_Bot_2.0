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


def contact_extractor(string):
    phn = "".join([char for char in string if char.isdigit()])
    return phn if len(phn) == 10 else phn[:10] if len(phn) > 10 else None


def email_extractor(string):
    for word in string.split(" "):
        if "@" in str(word) and ".com" in str(word):
            return word


def close_application():
    pg.hotkey("alt", "f4")


def shutdown():
    pg.hotkey('ctrl', 'win', 'd')
    pg.hotkey('alt', 'f4')
    pg.press('enter')



# def custom_call(source):
#     r = sr.Recognizer()
#     audio = r.listen(source)
#     text = r.recognize_google(audio)
#     return text
#
#
