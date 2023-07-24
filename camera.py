import time
import pyautogui as pg


# Camera functions
def click_picture(number_of_photos=1, timer=1.5):
    time.sleep(0.2)
    pg.press("win")
    time.sleep(0.3)
    pg.write("camera")
    pg.press("enter")
    time.sleep(timer)
    for _ in range(number_of_photos):
        pg.press("space")
        time.sleep(0.3)


def open_gallery():
    time.sleep(0.2)
    pg.press("win")
    time.sleep(0.3)
    pg.write("photos")
    pg.press("enter")
    for _ in range(19):
        pg.press("tab")
    pg.press("space")



