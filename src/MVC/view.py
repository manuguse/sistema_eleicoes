import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


class View:
    def __init__(self, controller):
        self.__controller = controller
        self.__layout = None
        self.__window = None
        self.__size = (800, 600)

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, val):
        self.__window = val

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, val):
        self.__controller = val

    def menu(self):
        self.__layout = [
            [sg.Text("Seja Bem-Vindo ao sistema de Eleições")],
            [sg.Button("Abrir arquivo para somar votos")],
            [sg.Button("Mostrar Gráfico do Resutado Final")],
            [sg.Button("Mostrar Pesquisa de Votos por Região por Candidato")],
            [sg.Button("Mostrar Tabela de Votos por Região")],
            [sg.Button("Sair")]
        ]

        self.__window = sg.Window("Sistema de Eleições", self.__layout)

    def resultado(self, candidatos, votos_por_regiao):
            self.__layout = [
                [sg.Text("Resultado da Eleição")],
                [sg.Text("Candidato", size=(20, 1)), sg.Text("Região", size=(20, 1)), sg.Text("Votos", size=(20, 1))],
            ]

            i = 0
            for candidato, itens in zip(candidatos, votos_por_regiao):
                for regiao, votos in itens.items():
                    if i == 0:
                        self.__layout.append([sg.Text(candidato, size=(20, 1)), sg.Text(regiao, size=(20, 1)), sg.Text(votos, size=(20, 1))])
                    else:
                        self.__layout.append([sg.Text("", size=(20, 1)), sg.Text(regiao, size=(20, 1)), sg.Text(votos, size=(20, 1))])
                    i += 1
                i = 0


            self.__layout.append([sg.Button("Voltar ao menu")])

            self.__window = sg.Window("Resultado da Eleição", self.__layout)

    def import_arquivo(self):
        self.__layout = [
            [sg.Text('Selecione um arquivo JSON:')],
            [sg.InputText(key='file_path'), sg.FileBrowse(file_types=(("JSON Files", "*.json"),))],
            [sg.Button('Abrir')],
            [sg.Multiline(size=(40, 10), key='json_output', disabled=True)],
            [sg.Button("Voltar ao menu")],
        ]

        self.__window = sg.Window('Abrir Arquivo JSON', self.__layout)
    
    def mostrar_graficos_resultado(self, candidatos, total_de_votos):
        x = 10  # Define a posição inicial em X
        escala = 20

        self.__layout = [
            [sg.Graph(canvas_size=(500, 200), graph_bottom_left=(0, 0), graph_top_right=(500, 200), key='graph', background_color="black")],
            [sg.Button("Voltar ao menu")]
        ]


        self.__window = sg.Window('Total de votos por candidato', self.__layout, finalize=True)
        graph = self.__window['graph']

        cores = ["blue", "red", "green", "purple", "orange", "pink"]
        cores_usadas = []

        def escolher_cor(cores_usadas):
            cores_disponiveis = [cor for cor in cores if cor not in cores_usadas]

            if cores_disponiveis:
                cor = random.choice(cores_disponiveis)
                cores_usadas.append(cor)
            else:
                cores_usadas.clear()
                cor = random.choice(cores)
                cores_usadas.append(cor)

            return cor

        for candidato, votos in zip(candidatos, total_de_votos):
            cor = escolher_cor(cores_usadas)
            graph.draw_rectangle((x, 10), (x + 30, votos / escala), line_color=cor, fill_color=cor)

            # Adicione a legenda relacionando a cor ao candidato
            legenda_x = x + 15  # A posição X da legenda é o centro da barra
            legenda_y = 5  # A posição Y da legenda (ajuste conforme necessário)
            graph.draw_text(candidato, (legenda_x, legenda_y), font="any 12", color="white")
            graph.draw_text(votos, (legenda_x, legenda_y+10), font="any 12", color="white")

            x += 50  # Aumenta a posição em X para a próxima barra

    def mostrar_pesquisa_candidato_regioes(self, candidatos, regioes):
        self.__layout = [
            [sg.Text("Escolha o candidato e a região para pesquisar a quantidade de votos")],
            [sg.Combo(candidatos, key='combo_candidato')],
            [sg.Combo(regioes, key='combo_regiao')],
            [sg.Button("Confirmar Candidato e Região")],
            [sg.Button("Voltar ao menu")]
        ]
        self.__window = sg.Window('Total de votos por candidato por região', self.__layout)
