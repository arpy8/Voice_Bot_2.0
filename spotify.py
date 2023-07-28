import pyautogui as pg


def song_extractor(raw_string):
    if "from" in raw_string:
        song_name = raw_string.split("from")[0].replace("play", "").strip()
    else:
        song_name = raw_string.replace("play", "").strip()
    return song_name


def play_song(raw_string):
    song_name = song_extractor(raw_string)
    print(song_name)
    pg.hotkey('win', 'r')
    pg.write('spotify')
    pg.press('enter')


play_song("play after dark from spotify")
