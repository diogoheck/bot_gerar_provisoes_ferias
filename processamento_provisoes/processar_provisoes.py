import pyautogui
import time
from competencia.calcular_competencia import calcular_competencia_geracao_anterior

LOCAL_GRAVAR_LOGS = 'R:\Compartilhado\Ti\log_provisoes\log_prov_ferias.txt'


def salvar_logs(conteudo):
    with open(LOCAL_GRAVAR_LOGS, 'a', encoding='ansi') as log:
        print(conteudo, file=log)


def processamento_folha_2(cod_empresa, competencia):
    log = ''
    while(True):
        if not not pyautogui.locateOnScreen('processo_finalizado_sucesso.png'):
            
            salvar_logs(
                    f'processamento de ferias do cliente {cod_empresa} gerado com sucesso competencia{competencia}')
            break
        else:
            pass
            # print('processando folha do cliente....')


def processamento_folha_1(cod_empresa, competencia, tipo):
    
    while(True):
        if not not pyautogui.locateOnScreen('processo_finalizado_sucesso.png'):
            salvar_logs(
                f'processamento de provisao de {tipo} do cliente {cod_empresa} gerado com sucesso competencia {competencia}')
            break
        else:
            pass
            # salvar_logs(
            #     f'processando de provisao de {tipo} do cliente {cod_empresa} {competencia}....')

        if not not pyautogui.locateOnScreen('inconsistencia.png'):
            pyautogui.click(x=981, y=583)
            salvar_logs(
                f'erro no processamento de provisao de {tipo} do cliente {cod_empresa} competencia {competencia}')

            break
                # pyautogui.press('enter')
                # competencia = calcular_competencia_geracao_anterior(competencia)
                # pyautogui.write(competencia)
                # pyautogui.press('enter')
                # processamento_folha_1(cod_empresa, competencia)


def finalizar_tela_processamento():
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    if not not pyautogui.locateOnScreen('inconsistencia.png'):
        pyautogui.click(x=981, y=583)
    time.sleep(1)
    pyautogui.doubleClick(x=193, y=182)
    time.sleep(1)
    #    pyautogui.write('2040')
    # pyautogui.press('enter')
