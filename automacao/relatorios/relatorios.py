import time
import pyautogui

from automacao.acoes import clicar, pressionar, escrever, atalho
from automacao.coordenadas import coordenadas

coordenada = coordenadas()

# Passo 3: Lozalizar relatório de faturamento por tipo de pagamento
# Localiza o relatório descritivo
def abrir_relatorio():
    from automacao.lojas.selecao_lojas import selecao_tipo_data
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
    clicar("excel")

def apagar_loja():
    clicar("loc_loja")
    atalho("ctrl", "a")
    pressionar("delete")

def baixar_relatorio():
    clicar("gerar")