from Login.login_unico import logar_unico
from modulo_DP.selecionar_mod_DP import acessar_modulo_folha
from cadastros.acesso_cadastros import acessar_processo_apuracao_provisao as acesso_provisao
from tela_apuracao_prov_ferias.tela_ferias import *
import datetime
from competencia.calcular_competencia import calcular_competencia_geracao
from processamento_provisoes.processar_provisoes import *
from planilha_cliente.ler_dados_admissao_prelim import ler_pasta
from openpyxl import load_workbook
import os

LOCAL_GRAVAR_LOGS = 'R:\Compartilhado\Ti\log_provisoes\log_prov_ferias.txt'

def salvar_logs(conteudo):
    with open(LOCAL_GRAVAR_LOGS, 'a', encoding='ansi') as log:
        print(conteudo, file=log)

if __name__ == '__main__':

    if os.path.exists(LOCAL_GRAVAR_LOGS):
        os.remove(LOCAL_GRAVAR_LOGS)

    competencia = calcular_competencia_geracao()

    pasta_provisoes = load_workbook('R:\\Compartilhado\\DP\\lista_provisoes\\plan_provisoes.xlsx')
    planilha = pasta_provisoes.active

    logar_unico()
    acessar_modulo_folha()
    acesso_provisao('s')
    for cod_empresa in planilha.values:
        preencher_tela_provisao_13(str(cod_empresa[0]), competencia)
        processamento_folha_1(
            str(cod_empresa[0]), competencia, 'Ferias')
        finalizar_tela_processamento()
    pyautogui.click(x=645, y=148)
    print('finalizando..........')
    time.sleep(5)
    pyautogui.click(x=1343, y=8)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    salvar_logs('FIM')
