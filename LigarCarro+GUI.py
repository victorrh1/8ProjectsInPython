# Um sistema que mostre o modelo, cor, ano do carro
# Precisa de um botao para ligar o carro

import PySimpleGUI as sg

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        # Layout
        self.layout = [
            [sg.Text('Ligar carro?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Ligar(self):
        print('Carro Ligado')

    def LigarCarro(self):
        # Criar Janela
        self.janela = sg.Window('Ligar Carro', layout=self.layout)
        while True:
            # Ler eventos
            self.evento, self.valores = self.janela.Read()

            # Verificar evento se foi fechado
            if self.evento == sg.WINDOW_CLOSED:
                break

            # Lidar com os eventos de clique
            if self.evento == 'Sim':
                print('Ligado')
                self.Ligar()
                break  # Encerrar o loop após o clique em 'Sim'
            elif self.evento == 'Não':
                self.Desligar()
                print('Carro Desligado')
                break  # Encerrar o loop após o clique em 'Não'

        self.janela.close()

    def Desligar(self):
        print('Desligue')

fiat = Carro('Uno', 'Amarelo', '2000')
fiat.LigarCarro()
