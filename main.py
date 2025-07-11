import pygetwindow as gw

from automacao.navegacao.login import login, abrir_chrome
from automacao.relatorios.relatorios import abrir_relatorio
from automacao.lojas.selecao_lojas import selecao_lojas_sub, selecao_gaia
from automacao.lojas.lojas import dicionario_lojas

def main():
    abrir_chrome()
    login()
    abrir_relatorio()
    selecao_lojas_sub(dicionario_lojas)
    selecao_gaia()

if __name__ == "__main__":
    main()
