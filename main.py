from chatGPT import chatGPT
from camera import *
from message import *
from jokes import dad_joke
import pyautogui as pg
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

            elif ("open" and "gallery") in text_list:
                open_gallery()

            elif ("joke" and "dad") in text_list:
                dad_joke()

            elif ("change" and "name") in text_list:
                update_name()

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


with sr.Microphone() as source:
    listen_for_wake_word(source)
