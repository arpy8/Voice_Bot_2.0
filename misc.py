import pyautogui as pg
import speech_recognition as s_r


def whatsapp_close_tab():
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")
    pg.keyDown("ctrl")
    pg.press("w")
    pg.keyUp("ctrl")
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")


def contact_extractor(string):
    phn = "".join([char for char in string if char.isdigit()])
    return phn if len(phn) == 10 else phn[:10] if len(phn) > 10 else None


def close_application():
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")