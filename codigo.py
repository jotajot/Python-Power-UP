import pyautogui
import time
import pygetwindow as gw

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
pyautogui.moveTo(x = 900, y = 580)
pyautogui.click(x = 900, y = 580)
pyautogui.click(button = 'left')

time.sleep(1)

pyautogui.moveTo(x = 350, y = 100)
pyautogui.click(x = 350, y = 72)
#time.sleep(1)

# digitar o site
pyautogui.write("https://app.swfast.com.br")
pyautogui.press("Enter")

pyautogui.write("joao@grupotsm.com.br")
pyautogui.press("Tab")
pyautogui.write("Josejoaojj_17")
pyautogui.press("Enter")
time.sleep(3)
pyautogui.moveTo(x = 273, y=383)
pyautogui.click(x=273, y=383)
pyautogui.moveTo(x=273, y=510)
pyautogui.click(button="left")

# Passo 2: Fazer login
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Cadastrar o restante dos produtos
