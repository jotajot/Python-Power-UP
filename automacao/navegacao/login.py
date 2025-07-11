import os
from dotenv import load_dotenv

from automacao.acoes import clicar, escrever, pressionar, esperar

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
