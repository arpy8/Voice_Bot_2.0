import datetime
from camera import *
from message import *
import pyautogui as pg
from jokes import dad_joke
from clock import set_timer
from chatGPT import chatGPT
import speech_recognition as sr
from spotify import *

playing_song = False


def listen_for_wake_word(source, recognizer):
    print("Bot: Listening for the wake word ...")

    while True:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            text_list = [word.lower() for word in text.lower().split()]
            print(text_list)
            wake_words = ["hey", "hi", "hello", "over"]
            if any(word in text_list for word in wake_words):
                print("Bot: Wake word detected.")
                SpeakText(random.choice(GREETINGS))
                listen_and_respond(source, recognizer)
                break
        except sr.UnknownValueError:
            pass
        except AssertionError:
            print(text_list)


def listen_and_respond(source, recognizer):
    while True:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")

            if not text:
                continue

            text_list = text.split()

            if "pause" in text_list:
                print("Bot: Session paused")
                play_sound("assets/swoosh.mp3")
                listen_for_wake_word(source, recognizer)

            if any(word in text_list for word in ["write", "type"]):
                pg.write(text)

            elif "whatsapp" in text.lower() or "contact" in text.lower():
                phone = contact_extractor(text)
                if phone is None:
                    print("Bot: Invalid contact")
                else:
                    print("Bot: What message should I send?")
                    send_whatsapp(phone, custom_call(source))
                    print("Bot: Message sent successfully")

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

            elif any(word in text_list for word in ["time", "right"]):
                speak_print(f"It's {datetime.datetime.now().strftime('%H:%M')} right now.")

            elif any((word in text_list) for word in ["play", "spotify", "song"]):
                global playing_song
                playing_song = True
                play_song(text_list)

            elif any(word in text_list for word in ["shutdown", "system"]):
                shutdown()

            elif "pause" in text_list:
                pause_song()

            else:
                gpt_reply = chatGPT(text)
                speak_print(gpt_reply)

        except sr.UnknownValueError:
            print("Bot: Silence found, shutting up")
            play_sound("assets/swoosh.mp3")
            listen_for_wake_word(source, recognizer)
            break

        except sr.RequestError as e:
            print(f"Bot: Could not request results; {e}")
            play_sound("assets/swoosh.mp3")
            listen_for_wake_word(source, recognizer)
            break


def main():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone(device_index=3) as source:
            listen_for_wake_word(source, recognizer)
    except Exception:
        print("No headphones detected. Switching mic")
        with sr.Microphone() as source:
            listen_for_wake_word(source, recognizer)


if __name__ == "__main__":
    main()
