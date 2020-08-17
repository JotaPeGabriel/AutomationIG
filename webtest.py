from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep, localtime, strftime
from openpyxl import load_workbook
from random import choice

""" Projeto de automação - Python + Selenium + OpenPyXL teste"""

url = 'https://www.instagram.com/p/CD7fSDyn7WA/'
navegador = Chrome()  # Define o Navegador como variavel
navegador.get(url)

folha = load_workbook('arrobas.xlsx')
plan = folha['Planilha1']
lista = plan['A']
listat = [45, 120, 135, 203, 374, 407, 500, 600]
print('ANTES DE COMEÇAR ESTEJA LOGADO E NA TELA DO SORTEIO')
start = input("Quando estiver pronto digite algo: ")


def comentar():
    for click in range(1500):
        arroba = choice(lista)
        tempo = int(choice(listat))
        balao = navegador.find_element_by_class_name('_15y0l')  # Encontrar e Clicar no Balao,Passando a vareavel arroba
        marcar = balao.find_element_by_class_name('wpO6b')
        marcar.send_keys('a', Keys.ENTER)
        campo = navegador.find_element_by_class_name('Ypffh')
        if campo.text != '':
            campo.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        marcar.send_keys('', Keys.ENTER, str(arroba.value))
        sleep(1)
        classe = navegador.find_element_by_class_name('RxpZH')  # Encontrar e Clicar no botão ENVIAR e comentar
        classe.find_element_by_class_name('sqdOP').send_keys(Keys.ENTER)
        t = localtime()  # Pegar a hora e data que esta sendo comentado
        agora = strftime("%H:%M:%S", t)
        print(f'{click + 1} - Voce Marcou: {arroba.value} as {agora}')
        print(f'O proximo vai ser daqui a >> {tempo} Segs OU {tempo / 60:.2f} Minutos <<\n')
        sleep(tempo)


comentar()
