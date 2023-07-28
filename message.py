import time
import smtplib
import urllib.parse
from utils import *
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def contact_extractor(string):
    phn = "".join([char for char in string if char.isdigit()])
    if len(phn) == 10:
        print(f"accepted, {phn}")
        return phn
    elif len(phn) > 10:
        print(f"accepted, {phn}")
        return phn[:10]
    else:
        speak_print("No number detected. Please speak the number again")
        phone_number = custom_listen()
        print(phone_number)
        contact_extractor(phone_number)


def email_extractor(string):
    for word in string.split(" "):
        if "@" in str(word) and ".com" in str(word):
            return word


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
    driver.find_element(By.XPATH, '//*[@id="action-button"]/span').click()
    time.sleep(2.5)
    pg.click(x=1089, y=273)
    time.sleep(3)
    pg.click(760, 1050)
    pg.press("enter")
    time.sleep(2)

    pg.hotkey("alt", "f4")

# def send_whatsapp2(phone, message):
#     url_message = urllib.parse.quote(str(message))
#     whatsapp_url = f"https://wa.me/91{phone}?text={url_message}"
#     try:
#         webbrowser.open(whatsapp_url)
#         time.sleep(10)
#
#         send_button_pos = (760, 1050)
#         pg.click(*send_button_pos)
#         pg.press("enter")
#         time.sleep(1.5)
#
#         whatsapp_close_tab()
#
#         pg.click(*send_button_pos)
#         time.sleep(4)
#         pg.press("enter")
#
#         close_application()
#
#         print("\nMessage sent successfully")
#
#     except Exception as e:
#         print(f"\nError occurred while sending the message: {e}")


# def send_whatsapp3(hour_delay=0, minute_delay=0, second_delay=3):
#     speak_print('Okay, please speak the phone number')
#     phone_number = contact_extractor(custom_listen())
#     print(phone_number)
#     speak_print("what message should I send?")
#     message = custom_listen()
#
#     now = datetime.now().strftime("%H%M%S")
#     current_hour = now[:2]
#     current_minute = now[2:4]
#     current_second = now[4:]
#     wt.sendwhatmsg(phone_number, message, (int(current_hour) + int(hour_delay)),
#                    (int(current_minute) + int(minute_delay)),
#                    (int(current_second) + int(second_delay)), True, 2)
