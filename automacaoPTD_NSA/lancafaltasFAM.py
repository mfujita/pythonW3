import pyautogui
import time

faltas = ['MB', 'MB', 'MB']
# faltas = ['MB', 'MB', 'MB', 'MB', 'MB', 'B', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB', 'MB']

time.sleep(1)
pyautogui.PAUSE = 0.1

for i in faltas:
    pyautogui.write(i)
    pyautogui.press('Enter')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')