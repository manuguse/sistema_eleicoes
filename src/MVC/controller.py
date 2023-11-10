from MVC.model import Model
from MVC.view import View
from MVC.model import Model
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
            candidatos = self.__model.obter_candidatos()
            votos_por_regiao = [self.__model.obter_votos_por_regiao(candidato) for candidato in self.__model.obter_candidatos()]
            total_de_votos = [self.__model.obter_total_de_votos(candidato) for candidato in self.__model.obter_candidatos()]
            regioes = self.__model.obter_regioes()

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
                except:
                    sg.popup('O aplicativo não consegue abrir o arquivo selecionado pois ou ele não é um arquivo compatível ou ele ja foi somado anteriormente, tente outro arquivo .json!', title='Arquivo errado')
            
            elif event == "Voltar ao menu":
                self.__view.window.close()
                self.__view.menu()
            
            elif event == "Pesquisar votos por região por candidato":
                self.__view.window.close()
                self.__view.pesquisa()
            
            elif event == "Mostrar Gráfico do Resutado Final":
                self.__view.window.close()
                self.__view.mostrar_graficos_resultado(candidatos, total_de_votos)

            if event == "Mostrar Pesquisa de Votos por Região por Candidato":
                self.__view.window.close()
                self.__view.mostrar_pesquisa_candidato_regioes(candidatos, regioes)

            if event == "Confirmar Candidato e Região":
                candidato_escolhido = values['combo_candidato']
                regiao_escolhida = values['combo_regiao']
                votos = self.__model.obter_votos_em_regiao(candidato_escolhido, regiao_escolhida)
                sg.popup(f"Votos do candidato {candidato_escolhido} na região {regiao_escolhida}: {votos}", title="Resultado")


        self.__view.window.close()
