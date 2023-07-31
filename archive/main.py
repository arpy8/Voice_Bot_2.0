from datetime import datetime
from camera import *
from message import *
import pyautogui as pg
from jokes import dad_joke
from clock import set_timer
from chatGPT import chatGPT
import speech_recognition as sr

playing_song = False


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
                speak_print(f"""It's {datetime.now().strftime("%H:%M")} right now.""")

            elif any((word in text_list) for word in ["play", "spotify", "song"]):
                play_song(text_list)

            elif any(word in text_list for word in ["shutdown", "system"]):
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


def main():
    try:
        with sr.Microphone(device_index=3) as source:
            listen_for_wake_word(source)
    except Exception:
        print("Seems like your headphones aren't connected. Switching mic")
        with sr.Microphone() as source:
            listen_for_wake_word(source)


if __name__ == "__main__":
    main()

# try:
#     with sr.Microphone(device_index=3) as source:
#         listen_for_wake_word(source)
# except Exception:
#     speak_print("Seems like your headphones aren't connected. Switching mic\n")
#     with sr.Microphone() as source:
#         listen_for_wake_word(source)

