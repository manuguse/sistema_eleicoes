import json
import random
import PySimpleGUI as sg

from OBSERVER.observable import Observable
from OBSERVER.observer import Observer


class Model(Observer, Observable):
    def __init__(self, DAO, DAO_arqs):
        super().__init__()
        self.__DAO = DAO
        self.__DAO_arqs = DAO_arqs
        self.__dados = None
        self.__cores = ["blue", "red", "green", "purple", "orange", "pink"]
        self.__cores_usadas = []
        self.__state = None
        self.__vencedor = None

    def update(self, model):
        self.__state = None
        if model.state == "Controller pronto":
            self.retornar_vencedor()
    
    def mudar_estado(self):
        self.state = "Model pronto"
        self.notificar_observadores()

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, val):
        self.__state = val

    @property
    def vencedor(self):
        return self.__vencedor

    @property
    def cores(self):
        return self.__cores
    
    @property
    def cores_usadas(self):
        return self.__cores_usadas

    def obter_candidatos(self):
        candidatos = []
        for candidatos_info in self.__DAO.cache:
            candidatos.append(candidatos_info["nome"])
        return candidatos
    
    def obter_regioes(self):
        list = []
        for candidato_info in self.__DAO.cache:
            x = candidato_info["votos"].keys()
            for elemento in x:
                if elemento not in list:
                    list.append(elemento)
        return list
            

    def obter_votos_por_regiao(self, candidato):
        for candidatos_info in self.__DAO.cache:
            if candidatos_info["nome"] == candidato:
                return candidatos_info["votos"]
        return {}

    def obter_total_de_votos(self, candidato):
        total_votos = 0
        votos_por_regiao = self.obter_votos_por_regiao(candidato)
        for item in votos_por_regiao.values():
            total_votos += int(item)
        return total_votos

    def obter_votos_em_regiao(self, candidato, local):
        votos_por_regiao = self.obter_votos_por_regiao(candidato)
        if local in votos_por_regiao:
            return int(votos_por_regiao[local])
        return 0

    def receber_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                self.__dados = json.load(arquivo)
                self.somar_votos()
                self.adicionar_arquivo_a_lista(nome_arquivo)
        except Exception:
            sg.popup("Arquivo incompatível")

    def somar_votos(self):
        for candidato in self.__dados:
            if candidato["nome"] not in self.obter_candidatos():
                self.__DAO.cache.append(candidato)
            else:
                for candidato_ofc in self.__DAO.cache:
                    if candidato["nome"] == candidato_ofc["nome"]:
                        for regiao in candidato["votos"].keys():
                            if regiao not in candidato_ofc["votos"].keys():
                                candidato_ofc["votos"][regiao] = candidato["votos"][regiao]
                            else:
                                candidato_ofc["votos"][regiao] = int(candidato_ofc["votos"][regiao])
                                candidato_ofc["votos"][regiao] += int(candidato["votos"][regiao])
                                candidato_ofc["votos"][regiao] = str(candidato_ofc["votos"][regiao])
        self.__DAO.dump()

    def adicionar_arquivo_a_lista(self, nome_arq):
        self.__DAO_arqs.add(len(self.__DAO_arqs.cache),nome_arq)

    def retornar_nome_arquivos(self):
        return self.__DAO_arqs.get_all()

    def escolher_cor(self):
        cores_disponiveis = [cor for cor in self.__cores if cor not in self.__cores_usadas]

        if cores_disponiveis:
            cor = random.choice(cores_disponiveis)
            self.__cores_usadas.append(cor)
        else:
            self.__cores_usadas.clear()
            cor = random.choice(self.__cores)
            self.__cores_usadas.append(cor)
        return cor
    
    def retornar_vencedor(self):
        vencedor_atual = [None]
        for candidato in self.obter_candidatos():
            votos_totais = self.obter_total_de_votos(candidato)
            if vencedor_atual == [None] or votos_totais > self.obter_total_de_votos(vencedor_atual[0]):
                vencedor_atual = [candidato]
            elif votos_totais == self.obter_total_de_votos(vencedor_atual[0]):
                vencedor_atual.append(candidato)
        if not self.__vencedor == vencedor_atual:
            self.__vencedor = vencedor_atual
            self.mudar_estado()
    