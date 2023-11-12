from MVC.model import Model
from MVC.view import View
from MVC.model import Model

import PySimpleGUI as sg

import json

from OBSERVER.observable import Observable
from OBSERVER.observer import Observer


class Controller(Observer, Observable):
    def __init__(self, view, model):
        super().__init__()
        self.__view = view
        self.__model = model
        self.__state = None
    
    def update(self, model):        
        if model.state == "Controller pronto":
            self.mudar_estado()
            self.notificar_observadores()
        if len(self.__model.vencedor) > 1:
            sg.popup("O(s) vencedor(es) é(são)", [candidato for candidato in self.__model.vencedor])
        else:
            sg.popup("O vencedor atual é", self.__model.vencedor[0])
    
    def mudar_estado(self):
        self.state = "Controller pronto"
        self.notificar_observadores()

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, val):
        self.__state = val

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
            candidatos = self.__model.obter_candidatos()
            votos_por_regiao = [self.__model.obter_votos_por_regiao(candidato) for candidato in self.__model.obter_candidatos()]
            total_de_votos = [self.__model.obter_total_de_votos(candidato) for candidato in self.__model.obter_candidatos()]
            regioes = self.__model.obter_regioes()
            len_candidatos = len(candidatos)

            if event == sg.WIN_CLOSED or event == "Sair":
                break
            
            elif event == "Mostrar Tabela de Votos por Região":
                self.__view.window.close()
                self.__view.resultado(candidatos, votos_por_regiao)

            elif event == "Abrir arquivo para somar votos":
                self.__view.window.close()
                self.__view.import_arquivo()
            
            elif event == "Abrir":
                try:
                    file_path = values['file_path']
                    self.__model.receber_arquivo(file_path)
                    self.__view.window.close()
                    self.__view.menu()
                    self.mudar_estado()
                except json.JSONDecodeError:
                    sg.popup('O aplicativo não consegue abrir o arquivo selecionado pois ele não é um arquivo compatível, tente outro arquivo .json!', title='Arquivo errado')
                # except:
                #     sg.popup('Esse arquivo ja foi somado anteriormente, e não será somado novamente, tente outro arquivo .json', title='Arquivo ja foi somado a base de dados')
            
            elif event == "Voltar ao menu":
                self.__view.window.close()
                self.__view.menu()
            
            elif event == "Pesquisar votos por região por candidato":
                self.__view.window.close()
                self.__view.pesquisa()
            
            elif event == "Mostrar Gráfico do Resutado Final":
                self.__view.window.close()
                cor = [self.__model.escolher_cor() for _ in range(len_candidatos)]
                self.__view.mostrar_graficos_resultado(candidatos, total_de_votos, cor)

            if event == "Mostrar Pesquisa de Votos por Região por Candidato":
                self.__view.window.close()
                self.__view.mostrar_pesquisa_candidato_regioes(candidatos, regioes)

            if event == "Confirmar Candidato e Região":
                candidato_escolhido = values['combo_candidato']
                regiao_escolhida = values['combo_regiao']
                votos = self.__model.obter_votos_em_regiao(candidato_escolhido, regiao_escolhida)
                sg.popup(f"Votos do candidato {candidato_escolhido} na região {regiao_escolhida}: {votos}", title="Resultado")

        self.__view.window.close()
