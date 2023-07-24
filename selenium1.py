import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def follower_scraper(user):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    phn = input("recipient's number: ")
    message = urllib.parse.quote(input("message: "))

    driver.maximize_window()
    driver.get(url=f"https://wa.me/+91{phn}?text={message}")
    try:
        if int(description.split(",")[0][0]) == 0:
            print("Couldn't fetch data, private account")
        else:
            return description.split(",")[0]

    except NoSuchElementException:
        return "User not found"


while 1:
    print(f"Description: {follower_scraper(input('Username: '))}\n")