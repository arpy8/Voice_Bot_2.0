import time
import pyautogui as pg


def song_extractor(raw_string):
    # Remove common prefixes and unnecessary whitespace from the raw_string
    prefixes_to_remove = ["can you play", "play", "from", "by", "on", "spotify"]
    song_name = "".join(raw_string).lower().strip()
    for prefix in prefixes_to_remove:
        song_name = song_name.replace(prefix, "").strip()

    # Handle cases where song name and artist/album are separated by ' - '
    if " - " in song_name:
        song_name = song_name.split(" - ")[0].strip()

    return song_name


def play_song(raw_string):
    try:
        # Extract the song name from the provided raw string
        song_name = song_extractor(raw_string)

        # Open Spotify
        pg.hotkey("win")
        time.sleep(1)
        pg.write("spotify")
        pg.press("enter")
        time.sleep(2)

        # Perform a Spotify search for the song
        pg.click(x=100, y=152)
        time.sleep(2.5)
        pg.click(x=633, y=98)
        time.sleep(2.5)
        pg.write(song_name)
        pg.press("enter")

        # Click on the song in the search results to play it
        pg.moveTo(x=1009, y=314)
        time.sleep(2)
        pg.click()

    except Exception as e:
        # Handle any exceptions that might occur during the automation process
        print("An error occurred:", e)


def pause_song():
    pg.click(x=967, y=1012)


def next_song():
    pg.click(x=1027, y=1004)


def show_lyrics():
    pg.click(x=1643, y=1026)


