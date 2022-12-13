import pyautogui
import time


def preencher_tela_provisao_ferias(cod_empresa, competencia):
    time.sleep(2)
    pyautogui.write(cod_empresa)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(competencia)
    time.sleep(2)
    pyautogui.press('enter')


def preencher_tela_provisao_13(cod_empresa, competencia):
    time.sleep(2)
    pyautogui.write(cod_empresa)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(competencia)
    time.sleep(2)
    pyautogui.press('enter')
