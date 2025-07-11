from automacao.acoes import clicar, escrever, pressionar
from automacao.lojas.lojas import dicionario_gaia_cafe

def selecao_lojas_sub(dicionario_lojas):
    clicar("loc_loja")
    
    for valor in dicionario_lojas.values():
        from automacao.relatorios.relatorios import apagar_loja
        escrever(str(valor))
        pressionar("Enter")
        clicar("checkbox")
        
        baixar_relatorio()
        apagar_loja()

def selecao_gaia():
    from automacao.relatorios.relatorios import abrir_relatorio_gaia
    clicar("loc_gaia_cafe")
    escrever("7484")
    pressionar("Enter")
    clicar("trocar_loja")
    abrir_relatorio_gaia()
    clicar("loc_loja")

    for num_loja in dicionario_gaia_cafe.values():
        from automacao.relatorios.relatorios import apagar_loja
        escrever(str(num_loja))
        pressionar("Enter")
        clicar("checkbox")
        
        baixar_relatorio()
        apagar_loja()

def selecao_tipo_data():
    clicar("excel")
    clicar("data")
    
def baixar_relatorio():
    clicar("gerar")