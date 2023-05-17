import pyautogui
import time
from random import randint
#abrir o wow
"""
Usando para abrir o wow no meu pc Automaticamente, e inserir um conta de um servidor local de world of warcraft 3.3.5

"""
pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write(r"C:\Users\thali\Downloads\World of Warcraft 3.3.5a\Wow.exe")
time.sleep(2)
pyautogui.press("enter")
time.sleep(20)
pyautogui.write('mega123')
time.sleep(2)
pyautogui.press('tab')
pyautogui.write('30912650')
time.sleep(2)
pyautogui.click(x=972, y=710)
time.sleep(5)

pyautogui.click(x=1003, y=843)

# (x=480, y=283)          (x=1410, y=321)
"""
aqui serão os comandos para o personagem do wow, sugiro um hunter com o seguinte macro no botão 1

#showtooltip
/petattack
/startattack

com esse simples macro estando com um hunter seu pet vai atacar automaticamente, fazendo assim que você possa ter um leveling com um hunter
"""
count= 0
count_virar_lado = 0
castskill = False
castarcura = False
comer = False
beber = False

while True:
    time.sleep(4)
    vlrx = randint(1268, 1486)
    vlry = randint(384, 405)
    if count == 25: 
      # por conta de algumas arvores e estruturas do proprio game após fazer 25 movimentos ele fara uma volta de 2 segundos no eixo assim fazendo-o contornar ou começar a se virar para sair de algum obstaculo.
        pyautogui.keyDown("A")
        pyautogui.keyUp("A")
        count = 0
    else:
        if castskill:
            pyautogui.press('2')
        else:
            pyautogui.press('1')
        
        pyautogui.click(x=vlrx, y=vlry, button="right")
        count+= 1
        if count % 2 ==0:
            castskill  = True
        else:
            castskill = False
        
