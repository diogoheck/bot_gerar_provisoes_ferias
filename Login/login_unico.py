from codecs import unicode_escape_decode
import pyautogui
from time import sleep
from funcao_locate.localizar_elemento import localizar_elemento_tela
import pyperclip


def logar_unico():

 # clicar no icone do unico na area de trabalho
    pyautogui.doubleClick(x=36, y=24, duration=2)
    sleep(120)
    # clicar no botao connect (ja com a senha salva da rede)
    pyautogui.click(x=820, y=359, duration=2)
    sleep(120)
    # clicar no input de usuario
    pyautogui.click(637, 373, duration=1)
    # inserir usuario
    pyperclip.copy('DIOGO RODRIGUES')
    # pyperclip.write('DIOGO RODRIGUES')
    pyautogui.hotkey('ctrl', 'v')
    sleep(2)
    # ir para o campo da senha
    pyautogui.press('tab')
    sleep(1)
    # Digitar a senha
    pyautogui.write('241708')
    sleep(1)
    # entrar no sistema
    pyautogui.press('enter')
    sleep(120)


if __name__ == '__main__':
    logar_unico()
