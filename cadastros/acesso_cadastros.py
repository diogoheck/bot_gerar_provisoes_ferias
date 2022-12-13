import pyautogui
import time


def acessar_processo_apuracao_provisao(tipo):
    # Processos
    time.sleep(5)
    pyautogui.hotkey('alt', 'e')
    time.sleep(2)
    # Apuracao da provisao das ferias
    pyautogui.press(tipo)
