import time
import pyautogui

time.sleep(1)
pyautogui.PAUSE = 0.5

def competencias():
    conta = 0
    yInicial= 427
    while conta < 6:
        pyautogui.click(x=46, y=yInicial+25*conta)
        pyautogui.click(x=391, y=235)
        pyautogui.write('1')
        pyautogui.press('TAB')
        pyautogui.write('Planejar o comércio eletrônico.')
        pyautogui.press('TAB')
        pyautogui.press('TAB')
        pyautogui.press('Enter')
        time.sleep(1)
        conta+=1

def habilidades():
    conta = 0
    yInicial= 424
    while conta < 6:
        pyautogui.click(x=46, y=yInicial+25*conta) # Data inicial/final
        pyautogui.click(x=343, y=440) # checkbox competências
        pyautogui.click(x=678, y=231) # Habilidades
        pyautogui.write('1')
        pyautogui.press('TAB')
        pyautogui.write('Utilizar ambientes de desenvolvimento de software mobile.')
        pyautogui.press('TAB')
        pyautogui.press('TAB')
        pyautogui.press('Enter')
        time.sleep(1)
        conta+=1

def basesTecnologicas():
    conta =0
    yInicial = 427
    while conta <6:
        pyautogui.click(x=46, y=yInicial+25*conta) # Data inicial/final
        pyautogui.click(x=971, y=239) # bases tecnológicas  
        pyautogui.write('Consumindo APIs e serviços Web: JSON.')
        pyautogui.press('TAB')
        pyautogui.press('TAB')
        pyautogui.press('Enter')
        time.sleep(1)
        conta+=1

def procedimentosDidaticos():
    conta = 0
    yInicial= 427
    while conta < 6:
        pyautogui.click(x=46, y=yInicial)
        pyautogui.click(x=1257, y=243)
        pyautogui.write('Aula dialogada')
        pyautogui.press('TAB')
        pyautogui.press('ENTER')
        yInicial +=25
        conta+=1

# competencias()
# habilidades()
# basesTecnologicas()
procedimentosDidaticos()