import pyautogui as pg


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
