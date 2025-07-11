import pyautogui
import time

from automacao.coordenadas import coordenadas 

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

coordenada = coordenadas()
#Funções auxiliares
def clicar(nome):
    pyautogui.moveTo(coordenada[nome])
    pyautogui.click()

def escrever(texto):
    pyautogui.write(texto)

def pressionar(tecla): 
    pyautogui.press(tecla)

def atalho(*teclas):
    pyautogui.hotkey(*teclas)

def esperar(segundos = 1):
    time.sleep(segundos)
