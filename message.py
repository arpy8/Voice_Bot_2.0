import os
import time
import smtplib
import webbrowser
import urllib.parse
import pyautogui as pg
from misc import whatsapp_close_tab

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


def send_whatsapp():
    phn = input("recipient's number: ")
    message = urllib.parse.quote(input("message: "))
    url = f"https://wa.me/91{phn}?text={message}"
    webbrowser.open(url)
    time.sleep(1.5)
    pg.click(x=760, y=1050)
    pg.press("enter")
    whatsapp_close_tab()
    pg.click(x=760, y=1050)
    pg.press("enter")


send_whatsapp()