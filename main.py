import datetime
from camera import *
from message import *
import pyautogui as pg
from jokes import dad_joke
from clock import set_timer
from chatGPT import chatGPT
import speech_recognition as sr


def listen_for_wake_word(source):
    print("Bot: Listening for the wake word ...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_list = [word.lower() for word in text.lower().split()]
            print(text_list)
            if "hey" or "hi" or "hello" or "over" in text_list:
                print("Bot: Wake word detected.")
                # play_sound("assets/init.mp3")
                SpeakText(random.choice(GREETINGS))
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass
        except AssertionError:
            print(text_list)


def listen_and_respond(source):
    r = sr.Recognizer()

    while True:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You: {text}")

            if not text:
                continue

            text_list = text.split()

            if "pause" in text_list:
                speak_print("Session paused\n")
                play_sound("assets/swoosh.mp3")
                listen_for_wake_word(source)

            if not audio:
                play_sound("assets/swoosh.mp3")
                listen_for_wake_word(source)

            if "write" in text_list or "type" in text_list:
                pg.write(text)

            elif "whatsapp" in text.lower() or "contact" in text.lower():
                phone = contact_extractor(text)
                if phone is None:
                    print("Invalid contact")
                else:
                    speak_print("What message should I send?")
                    send_whatsapp(phone, custom_call(source))
                    speak_print("Message sent successfully\n")

            elif ("camera" and "open") in text_list or "click" in text_list or "picture" in text_list:
                click_picture()

            elif "gallery" in text_list:
                open_gallery()

            elif ("joke" and "dad") in text_list:
                dad_joke()

            elif ("change" and "name") in text_list:
                update_name()

            elif ("set" and "reminder") in text_list:
                set_timer(text_list)

            elif ("time" and "the") in text_list:
                speak_print(f"""It's {datetime.now().strftime("%H:%M")} right now.""")

            elif (("play" or "spotify") and "song") in text_list:
                play_song(text_list)

            elif ("shutdown" and "system") in text_list:
                shutdown()

            else:
                gpt_reply = chatGPT(text)
                speak_print(gpt_reply)

        except sr.UnknownValueError:
            print("Silence found, shutting up")
            play_sound("assets/swoosh.mp3")
            listen_for_wake_word(source)
            break

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            play_sound("assets/swoosh.mp3")
            listen_for_wake_word(source)
            break


try:
    with sr.Microphone(device_index=3) as source:
        listen_for_wake_word(source)
except AssertionError:
    with sr.Microphone(device_index=1) as source:
        listen_for_wake_word(source)
