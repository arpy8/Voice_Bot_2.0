import os
import gtts
import playsound
import pyautogui as pg


def SpeakText(text, lang="en"):
    sound = gtts.gTTS(str(text), lang=lang)
    sound.save("assets/temp.mp3")
    playsound.playsound("assets/temp.mp3")
    os.remove("assets/temp.mp3")


def speak_print(text):
    if "\n" in text:
        text.replace("\n", "")
        SpeakText(text)
    print(text)


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

