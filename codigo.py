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
       "usuario": [1080, 580],  #seleciona usuário chrome
        "relatorios": [273, 383],  #seleciona relatórios
        "rel_desc": [273, 510],  #seleciona relatórios descritivos
        "pesquisa": [500, 286],  #barra de pesquisa do relatório
        "faturamentos": [500, 338],  #seleciona aba faturamentos
        "tipo_pag": [500, 358],   #seleciona opção faturamento por tipo de pagamento
        "excel": [1040, 648],  #escolhe o formato do relatório
        "data": [1069, 254],    #seleciona a data do dia anterior
        "gerar": [940, 728],    #baixa o relatório da loja
        "loc_loja": [1467, 280],    #pesquisa a loja
        "checkbox": [1380, 340],    #marca a loja escolhida para download
        "loc_gaia_cafe": [1525, 100],
        "trocar_loja": [920, 674]
}

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


def selecao_tipo_data():
    clicar("excel")
    clicar("data")
    
def baixar_relatorio():
    clicar("gerar")

# Passo 1: Entrar no chrome
# abrir o chrome
def abrir_chrome():
    pressionar("win")
    escrever("chrome")
    pressionar("Enter")
    clicar("usuario")

    esperar()

# Passo 2: Fazer login
# digitar o site
def login():
    escrever("https://app.swfast.com.br")
    pressionar("Enter")
    esperar(2)

    #carrega a leitura de dados sensíveis 
    load_dotenv()

    usuario = os.getenv('DB_USER')
    senha = os.getenv('DB_PASSWORD')

    #executando o login
    escrever(usuario)
    pressionar("Tab")
    escrever(senha)
    pressionar("Enter")
    esperar(3)

# Passo 3: Lozalizar relatório de faturamento por tipo de pagamento
# Localiza o relatório descritivo
def abrir_relatorio():
    clicar("relatorios")
    clicar("rel_desc")
    pyautogui.moveTo(coordenada["pesquisa"])
    time.sleep(1)
    pyautogui.click(coordenada["pesquisa"])
    escrever("faturamento por tipo de pagamento")
    pressionar("Enter")
    clicar("faturamentos")
    clicar("tipo_pag")
    selecao_tipo_data()

def abrir_relatorio_gaia():
    clicar("rel_desc")
    pyautogui.moveTo(coordenada["pesquisa"])
    time.sleep(1)
    pyautogui.click(coordenada["pesquisa"])
    escrever("faturamento por tipo de pagamento")
    pressionar("Enter")
    clicar("faturamentos")
    clicar("tipo_pag")
    selecao_tipo_data()

def apagar_loja():
    clicar("loc_loja")
    atalho("ctrl", "a")
    pressionar("delete")

def baixar_relatorio():
    clicar("gerar")

def selecao_lojas(dicionario_lojas):
    clicar("loc_loja")
    
    for valor in dicionario_lojas.values():
        escrever(str(valor))
        pressionar("Enter")
        clicar("checkbox")
        
        baixar_relatorio()
        apagar_loja()

def selecao_gaia():
    clicar("loc_gaia_cafe")
    escrever("7484")
    pressionar("Enter")
    clicar("trocar_loja")
    abrir_relatorio_gaia()
    clicar("loc_loja")

    for num_loja in dicionario_gaia_cafe.values():
        escrever(str(num_loja))
        pressionar("Enter")
        clicar("checkbox")
        
        baixar_relatorio()
        apagar_loja()

dicionario_lojas = {
    "cohafuma nova": 6627,
    "olho dagua": 7406,
    "reviver": 7493,
    "aeroporto": 9249,
    "cohab": 9250,
    "patio norte": 9464,
    "cohama": 9465,
    "são luis": 9468
}

dicionario_gaia_cafe = {
    "gaia holandeses": 7484,
    "gaia aeroporto": 9025
}
        
abrir_chrome()
login()
abrir_relatorio()
selecao_lojas(dicionario_lojas)
selecao_gaia()
