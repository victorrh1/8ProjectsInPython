import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Não sei, você que sabe',
            'Não faz isso',
            'Acho que está na hora certa'
        ]

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        # Criar janela
        self.janela = sg.Window('Decida por mim', layout=layout)
        while True:
            # Ler valores
            self.eventos, self.valores = self.janela.Read()
            # Verificar se a janela foi fechada
            if self.eventos == sg.WINDOW_CLOSED:
                break
            # Objetivo
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))

        self.janela.close()

decida = DecidaPorMim()
decida.Iniciar()
