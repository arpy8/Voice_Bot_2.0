import pyautogui as py  # Import pyautogui
import time  # Import Time

while True:  # Start loop
    print(f'pg.click{str(py.position()).replace("Point", "")}')
    time.sleep(1)
