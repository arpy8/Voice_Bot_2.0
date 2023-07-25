import time
import smtplib
import webbrowser
from utils import *
import urllib.parse
import urllib.parse
from config import *
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def send_mail(recp_email, message):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(SMTP_MAIL, SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_MAIL,
            to_addrs=recp_email,
            msg=message
        )


def send_whatsapp(phone, message):
    url_message = urllib.parse.quote(str(message))
    whatsapp_url = f"https://wa.me/91{phone}?text={url_message}"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(whatsapp_url)
    pg.press("tab")
    pg.press("space")
    try:
        driver.find_element(By.XPATH, '//*[@id="action-button"]/span').click()

    except NoSuchElementException:
        return "Button not found"
    time.sleep(1)
    pg.click(x=1089, y=273)
    time.sleep(1)
    pg.click(760, 1050)
    pg.press("enter")
    time.sleep(1.5)

    pg.hotkey("alt", "f4")


def send_whatsapp2(phone, message):
    url_message = urllib.parse.quote(str(message))
    whatsapp_url = f"https://wa.me/91{phone}?text={url_message}"
    try:
        webbrowser.open(whatsapp_url)
        time.sleep(8)

        send_button_pos = (760, 1050)
        pg.click(*send_button_pos)
        pg.press("enter")
        time.sleep(1.5)

        whatsapp_close_tab()

        pg.click(*send_button_pos)
        time.sleep(2)
        pg.press("enter")

        close_application()

        print("\nMessage sent successfully")

    except Exception as e:
        print(f"\nError occurred while sending the message: {e}")


