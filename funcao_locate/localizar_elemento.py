import pyautogui


def localizar_elemento_tela(imagem):
    elemento = pyautogui.locateOnScreen(imagem)
    while(elemento == None):
        # print(f'{elemento}')
        # print(f'{not not elemento}')
        elemento = pyautogui.locateOnScreen(imagem)
    return elemento
