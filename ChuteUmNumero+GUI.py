# Chute o numero
# Objetivo: Criar um algoritmo que gera um valor aleatorio até o usuario acertar
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = False

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(39, 0))],
            [sg.Input(size=(18, 0), key='ValorChute', enable_events=True, focus=True)],
            [sg.Button('Chutar!', bind_return_key=True)],
            [sg.Output(size=(39, 10))]
        ]

        # Criar uma Janela
        self.janela = sg.Window('Chute o número!', layout=layout)

        self.GerarNumeroAleatorio()

        while True:
            evento, valores = self.janela.Read()

            if evento == sg.WINDOW_CLOSED:
                break

            if evento == 'Chutar!':
                self.valor_do_chute = valores['ValorChute']
                self.tentar_novamente = True
                self.VerificarChute()

        self.janela.close()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

    def VerificarChute(self):
        if self.tentar_novamente:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo')
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto')
            else:
                print('Acertou!')
                self.tentar_novamente = False

chute = ChuteONumero()
chute.Iniciar()