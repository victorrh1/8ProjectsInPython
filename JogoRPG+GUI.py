# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas
# Eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa
# O personagem receberá várias perguntas para ir adiante, com base em suas respostas

import PySimpleGUI as sg

class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no Norte ou Sul (N/S)' # norte Lado1, sul Lado2
        self.pergunta2 = 'Você prefere a Espada ou Arco (Espada/Arco)' # espada Lado1, arco Lado2
        self.pergunta3 = 'Qual é sua especialidade (Linha de Frente/Longa Distância)' # linhaF1, longaD2
        self.finalHistoria1 = 'Você será um heroi de linha de Frente'
        self.finalHistoria2 = 'Você será um heroi de longa Distância, para proteger as tropas'
        self.finalHistoria3 = 'Você irá sacrificar na batalha'
        self.finalHistoria4 = 'Você deve ter visão e informar a tropa'
        self.respostas = []
        self.janela = None

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Output(size=(50,20))],
            [sg.Input(key='resposta', size=(25,10))],
            [sg.Button('Iniciar'), sg.Button('Responder')]
        ]
        
        # Criar janela
        self.janela = sg.Window('Jogo de Aventura', layout=layout)
        
        while True:
            # Ler dados
            self.evento, self.valores = self.janela.Read()
            
            if self.janela is None or self.evento == sg.WINDOW_CLOSED:  # Verifica se a janela foi fechada ou evento de fechamento
                break
            
            # Condicionais
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.respostas = []
            
            elif self.evento == 'Responder':
                resposta = self.valores['resposta']
                self.respostas.append(resposta)
                
                if len(self.respostas) == 1:
                    if resposta == 'N':
                        print(self.pergunta2)
                    elif resposta == 'S':
                        print(self.pergunta3)
                
                elif len(self.respostas) == 2:
                    if resposta == 'Espada':
                        print(self.finalHistoria1)
                    elif resposta == 'Arco':
                        print(self.finalHistoria2)
                    elif resposta == 'Linha de Frente':
                        print(self.finalHistoria3)
                    elif resposta == 'Longa Distância':
                        print(self.finalHistoria4)
        
        # Fechar janela
        if self.janela is not None:
            self.janela.Close()

jogo = JogoAventura()
jogo.Iniciar()



