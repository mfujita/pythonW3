import time
import pyautogui

time.sleep(1)
pyautogui.PAUSE = 2

for i in range(3):
    pyautogui.click(x=1058, y=371)
    pyautogui.click(x=1462, y=521)
    pyautogui.write("Validado.")
    pyautogui.click(x=1351, y=774)
    pyautogui.click(x=1536, y=79)
