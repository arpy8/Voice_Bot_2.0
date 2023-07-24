import os

NAME = "Arpit"
GREETINGS = [f"Hello Mr. {NAME}",
             "yeah? what's up?",
             "Well, hello there, Master of Puns and Jokes - how's it going today?",
             f"Namaste, {NAME} ji! Mai aapki kaise sewa kar skti hu",
             f"Bonjour, Monsieur {NAME}! Comment ça va? Wait, why the hell am I speaking French?"]

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_MAIL = 'arpitsengar99@gmail.com'
SMTP_PASSWORD = os.getenv("GMAIL_APP_PASS")

# GPT configuration
GPT_API = os.getenv("OPENAI_API")
