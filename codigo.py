import pyautogui
import time
import pygetwindow as gw

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

def coordenadas() : 
    return [
        [900, 580],
        [350, 72],
        [273, 383],
        [273, 510],
        [500, 286],
        [500, 338],
        [500, 358]
]

coordenada = coordenadas()


# Passo 1: Entrar no chrome
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
pyautogui.moveTo(coordenada[0])
pyautogui.click(coordenada[0])
#pyautogui.click(button = 'left')

time.sleep(1)

#pyautogui.moveTo(coordenada[1])
#pyautogui.click(coordenada[1])
#time.sleep(1)

# Passo 2: Fazer login
# digitar o site
pyautogui.write("https://app.swfast.com.br")
pyautogui.press("Enter")

pyautogui.write("joao@grupotsm.com.br")
pyautogui.press("Tab")
pyautogui.write("Josejoaojj_17")
pyautogui.press("Enter")
time.sleep(3)

# Passo 3: Lozalizar relatório de faturamento por tipo de pagamento
# Localiza o relatório descritivo 
pyautogui.moveTo(coordenada[2])
pyautogui.click(coordenada[2])
pyautogui.moveTo(coordenada[3])
pyautogui.click(button="left")
pyautogui.moveTo(coordenada[4])
time.sleep(1)
pyautogui.click(coordenada[4])
pyautogui.write("faturamento por tipo de pagamento")
pyautogui.press("Enter")
pyautogui.click(coordenada[5])
pyautogui.moveTo(coordenada[6])
pyautogui.click(coordenada[6])



# Passo 4: Cadastrar 1 produto
# Passo 5: Cadastrar o restante dos produtos
