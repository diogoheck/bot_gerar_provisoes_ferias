import pyautogui
import time


def acessar_processo_apuracao_provisao(tipo):
    # Processos
    time.sleep(5)
    pyautogui.click(423, 31, duration=1)
    time.sleep(2)
    # Apuracao da provisao das ferias
    pyautogui.move(0, 270)
    time.sleep(1)
    pyautogui.click()
