from num2words import *
from PySimpleGUI import  PySimpleGUI as sg
user = []
#layout
sg.theme('Black')
layout_coluna = [

    [sg.Text('NÚMERO POR EXTENSO', font=('Arial', 11, 'bold'))],
    [sg.Text('Digite um número:', font=('Arial', 10, 'bold')), sg.Input(key='numero', size=20)],
    [sg.Button('Verificar número')],

]
layout = [[sg.Column(layout_coluna, element_justification='center')]]
janela = sg.Window('V1.0', layout)

#ler eventos
while True:
    try:
        eventos , valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Verificar número':
            user = num2words(valores['numero'], lang='pt_BR')
            sg.popup(f'Número digitado foi {user}', title='Resultado: ')
    except:
        sg.popup_ok('DIGITE APENAS NÚMEROS, EM CASO DE O ERRO PERSISTE, ENTRE EM CONTANTO COM O PROGRAMADOR @juanpb1_')

