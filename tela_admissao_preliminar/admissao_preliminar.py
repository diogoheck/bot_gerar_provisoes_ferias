import pyautogui
import time
from planilha_cliente.ler_dados_admissao_prelim import ler_pasta


def preencher_tela_admissao_preliminar(dados_funcionario):

    pyautogui.write('2330')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')  # colaborador
    pyautogui.write(dados_funcionario.get('NOME'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('CLASSE'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('CPF'))
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('PIS'))
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('NASCIMENTO'))
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('ADMISSÃO'))
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('TIPO DE ADMISSAO'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('CATEGORIA'))
    pyautogui.press('enter')
    time.sleep(0.05)
    # pyautogui.write(dados_funcionario.get('FUNÇÃO'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('TIPO DO COLABORADOR'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('SALARIO'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('TIPO CONTRATO'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.write(dados_funcionario.get('PRAZO'))
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.press('enter')
    time.sleep(0.05)
    pyautogui.hotkey('alt', 'N')


    # Nome
if __name__ == '__main__':
    dados_funcionario = ler_pasta()
    preencher_tela_admissao_preliminar(dados_funcionario)
