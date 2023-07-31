import os
import toml

toml_file_path = "assets/name.toml"

NAME = toml.load(open(toml_file_path, "r"))['NAME']
GREETINGS = [f"Hello Mr. {NAME}",
             "yeah? what's up?",
             "Well, hello there boss",
             f"Namaste, {NAME} ji! Hope you're doing amazing",
             f"Hello {NAME}, "
             ]

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_MAIL = 'arpitsengar99@gmail.com'
SMTP_PASSWORD = os.getenv("GMAIL_APP_PASS")

# GPT configuration
GPT_KEY = os.getenv("OPENAI_API")
PREDEFINED_PROMPT = os.getenv("GPT_PROMPT")

# Dad Joke configuration
RAPID_API = os.getenv("RapidAPI")
JOKES_URL = "https://dad-jokes.p.rapidapi.com/random/joke"
HEADERS = {
    "X-RapidAPI-Key": RAPID_API,
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

DICTIONARY_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
GENDER_URL = "https://api.genderize.io?name="


WEATHERSTACK_API = os.getenv("WEATHERSTACK_API")
WEATHERSTACK_URL = f"httpS://api.weatherstack.com/current?access_key={WEATHERSTACK_API}&query="
