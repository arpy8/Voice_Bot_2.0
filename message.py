import os
import time
import smtplib
import webbrowser
import urllib.parse
import pyautogui as pg
from misc import *

# CONSTANTS
MY_EMAIL = "arpitsengar99@gmail.com"
MY_PASSWORD = os.getenv("GMAIL_APP_PASS")


def send_mail(email, pswd):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email, pswd)
        connection.sendmail(
            from_addr=email,
            to_addrs=input("recipient's email: "),
            msg=input("message: ")
        )
    print("\nmessage sent successfully!")


def send_whatsapp(phone, message):
    try:
        url_message = urllib.parse.quote(message)

        webbrowser.open(f"https://wa.me/91{phone}?text={url_message}")
        time.sleep(5)
        pg.click(x=760, y=1050)
        pg.press("enter")
        time.sleep(1.5)
        whatsapp_close_tab()
        pg.click(x=760, y=1050)
        pg.press("enter")
        time.sleep(0.5)
        close_application()
        print("\n message sent successfully")

    except TypeError:
        pass


