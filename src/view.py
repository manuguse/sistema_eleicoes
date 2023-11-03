import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class View:
    def __init__(self, controller):
        self.__controller = controller
        self.__layout = None
        self.__window = None

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
            [sg.Button("Ver resultado final")],
            [sg.Button("Adicionar novo arquivo de contagem de votos")]
        ]

        self.__window = sg.Window("Sistema de Eleições", self.__layout)

    def resultado(self, candidatos, votos_por_regiao):
            self.__layout = [
                [sg.Text("Resultado da Eleição")],
                [sg.Text("Candidato", size=(20, 1)), sg.Text("Região", size=(20, 1)), sg.Text("Votos", size=(20, 1))],
            ]

            for candidato, itens in zip(candidatos, votos_por_regiao):
                for regiao, votos in itens.items():
                    self.__layout.append([sg.Text(candidato, size=(20, 1)), sg.Text(regiao, size=(20, 1)), sg.Text(votos, size=(20, 1))])

            self.__layout.append([sg.Button("Voltar")])

            self.__window = sg.Window("Resultado da Eleição", self.__layout)

    def import_arquivo(self):
        self.__layout = [
            [sg.Text('Selecione um arquivo JSON:')],
            [sg.InputText(key='file_path'), sg.FileBrowse(file_types=(("JSON Files", "*.json"),))],
            [sg.Button('Abrir'), sg.Button('Sair')],
            [sg.Multiline(size=(40, 10), key='json_output', disabled=True)],
            [sg.Button("Voltar")],
        ]

        self.__window = sg.Window('Abrir Arquivo JSON', self.__layout)
    
    def mostrar_graficos(self):
        self.__layout = [
            [sg.Text("Gráfico de Pizza")],
            [sg.Column(layout=[[sg.Canvas(key='-PIE_CANVAS-')]])],
            [sg.Text("Gráfico de Colunas")],
            [sg.Column(layout=[[sg.Canvas(key='-BAR_CANVAS-')]])],
            [sg.Button('Gerar Gráficos'), sg.Button('Sair')],
        ]

        self.__window = sg.Window('Gráficos com PySimpleGUI', self.__layout, finalize=True)