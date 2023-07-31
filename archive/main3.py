import datetime
from camera import *
from change_name import update_name
from message import *
import pyautogui as pg
from jokes import dad_joke
from clock import set_timer
from chatGPT import chatGPT
import speech_recognition as sr

from spotify import play_song

playing_song = True


def listen_for_wake_word(source):
    print("Bot: Listening for the wake word ...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_list = [word.lower() for word in text.lower().split()]
            print(text_list)
            if any(word in text_list for word in ["hey", "hi", "hello", "over"]):
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
    while True:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = str(recognizer.recognize_google(audio)).lower()
            print(f"You: {text}")

            if not text:
                continue

            text_list = text.split()

            if "pause" in text_list:
                print("Bot: Session paused")
                play_sound("assets/swoosh.mp3")
                listen_for_wake_word(source)

            if "write" in text_list or "type" in text_list:
                pg.write(text)

            elif any(word in text_list for word in ["whatsapp", "contact"]):
                send_message(text)

            elif any(word in text_list for word in ["camera", "open", "click", "picture"]):
                click_picture()

            elif "gallery" in text_list:
                open_gallery()

            elif any(word in text_list for word in ["joke", "dad"]):
                dad_joke()

            elif any(word in text_list for word in ["change", "name"]):
                update_name()

            elif any(word in text_list for word in ["set", "reminder"]):
                set_timer(text_list)

            elif any(word in text_list for word in ["time", "the"]):
                speak_print(f"It's {datetime.datetime.now().strftime('%H:%M')} right now.")

            elif any((word in text_list) for word in ["play", "spotify", "song"]):
                play_song(text)

            elif any(word in text_list for word in ["shutdown", "system"]):
                shutdown()

            elif any(word in text_list for word in ["lock", "system"]):
                lock_system()

            else:
                gpt_reply = chatGPT(text)
                speak_print(gpt_reply)

        except sr.UnknownValueError:
            print("Bot: Silence found, shutting up")
            play_sound("assets/swoosh.mp3")
            listen_for_wake_word(source)
            break

        except sr.RequestError as e:
            print(f"Bot: Could not request results; {e}")
            play_sound("assets/swoosh.mp3")
            listen_for_wake_word(source)
            break


try:
    with sr.Microphone(device_index=3) as source:
        listen_for_wake_word(source)
except AssertionError:
    with sr.Microphone(device_index=1) as source:
        listen_for_wake_word(source)
