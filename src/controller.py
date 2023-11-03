from model import Model
from view import View
from model import Model
import PySimpleGUI as sg


class Controller:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, val):
        self.__model = val

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, val):
        self.__view = val

    def iniciar_aplicativo(self):
        self.__view.menu()
        while True:
            event, values = self.__view.window.read()

            if event == sg.WIN_CLOSED or event == "Sair":
                break
            
            elif event == "Ver resultado final":
                candidatos = self.__model.obter_candidatos()
                votos_por_regiao = [self.__model.obter_votos_por_regiao(candidato) for candidato in self.__model.obter_candidatos()]
                self.__view.window.close()
                self.__view.resultado(candidatos, votos_por_regiao)

            elif event == "Adicionar novo arquivo de contagem de votos":
                self.__view.window.close()
                self.__view.import_arquivo()
            
            elif event == "Abrir":
                try:
                    file_path = values['file_path']
                    self.__model.receber_arquivo(file_path)
                except:
                    pass # não vai acontecer nada se não for escolhido nenhum arquivo novo
            
            elif event == "Voltar":
                self.__view.window.close()
                self.__view.menu()
            
        self.__view.window.close()
