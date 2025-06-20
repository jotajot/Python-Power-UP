import pyautogui
import time
import pygetwindow as gw
from dotenv import load_dotenv
import os

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

def coordenadas() : 
    return {
       "usuario": [900, 580],  #seleciona usuário chrome
        "relatorios": [273, 383],  #seleciona relatórios
        "rel_desc": [273, 510],  #seleciona relatórios descritivos
        "pesquisa": [500, 286],  #barra de pesquisa do relatório
        "faturamentos": [500, 338],  #seleciona aba faturamentos
        "tipo_pag": [500, 358],   #seleciona opção faturamento por tipo de pagamento
        "excel": [1040, 648],  #escolhe o formato do relatório
        "data": [1069, 254],    #seleciona a data do dia anterior
        "gerar": [940, 728],    #baixa o relatório da loja
        "loc_loja": [1467, 280],    #pesquisa a loja
        "checkbox": [1380, 340]    #marca a loja escolhida para download
}

coordenada = coordenadas()


def selecao_tipo_data():
    pyautogui.moveTo(coordenada["excel"])
    pyautogui.click(coordenada["excel"])
    pyautogui.moveTo(coordenada["data"])
    pyautogui.click(coordenada["data"])
    
def baixar_relatorio():
    pyautogui.moveTo(coordenada["gerar"])
    pyautogui.click(button="left")

def apagar_loja():
    pyautogui.moveTo(coordenada["loc_loja"])
    pyautogui.click(coordenada["loc_loja"])
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

# Passo 1: Entrar no chrome
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
pyautogui.moveTo(coordenada["usuario"])
pyautogui.click(coordenada["usuario"])


time.sleep(1)


# Passo 2: Fazer login
# digitar o site
pyautogui.write("https://app.swfast.com.br")
pyautogui.press("Enter")
time.sleep(2)

#carrega a leitura de dados sensíveis 
load_dotenv()

usuario = os.getenv('DB_USER')
senha = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
banco = os.getenv('DB_NAME')

#executando o login
pyautogui.write(usuario)
pyautogui.press("Tab")
pyautogui.write(senha)
pyautogui.press("Enter")
time.sleep(3)

# Passo 3: Lozalizar relatório de faturamento por tipo de pagamento
# Localiza o relatório descritivo 
pyautogui.moveTo(coordenada["relatorios"])
pyautogui.click(coordenada["relatorios"])
pyautogui.moveTo(coordenada["rel_desc"])
pyautogui.click(button="left")
pyautogui.moveTo(coordenada["pesquisa"])
time.sleep(1)
pyautogui.click(coordenada["pesquisa"])
pyautogui.write("faturamento por tipo de pagamento")
pyautogui.press("Enter")
pyautogui.click(coordenada["faturamentos"])
pyautogui.moveTo(coordenada["tipo_pag"])
pyautogui.click(coordenada["tipo_pag"])

selecao_tipo_data()

dicionario = {
    "cohafuma nova": 6627,
    "olho dagua": 7406,
    "reviver": 7493,
    "aeroporto": 9249,
    "cohab": 9250,
    "patio norte": 9464,
    "cohama": 9465,
    "são luis": 9468
}

def selecao_lojas():
    pyautogui.moveTo(coordenada["loc_loja"])
    pyautogui.click(button="left")
    
    for valor in dicionario.values():
        pyautogui.write(str(valor))
        pyautogui.press("Enter")
        pyautogui.moveTo(coordenada["checkbox"])
        pyautogui.click(coordenada["checkbox"])
        
        baixar_relatorio()
        apagar_loja()
        

selecao_lojas()

