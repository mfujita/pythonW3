import pyautogui
import time

faltas = [2, 0, 0, 0, 4, 0, 4, 4, 0, 0, 4, 0, 0, 2, 0, 0, 6, 0, 2, 0, 0, 2, 8, 4, 0, 0, 0, 4, 2, 2, 0, 0, 0, 2, 0, 0, 2, 4, 0, 2, 0, 2, 2, 0, 0, 2, 0, 2]

time.sleep(1)
pyautogui.PAUSE = 0.1

for i in faltas:
    pyautogui.write(str(i))
    pyautogui.press('TAB')