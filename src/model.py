import json
from candidatos import Candidato


class Model:
    def __init__(self, DAO):
        self.__DAO = DAO
        self.__dados = None

    def obter_candidatos(self):
        candidatos = []
        for candidatos_info in self.__DAO.cache:
            candidatos.append(candidatos_info["nome"])
        return candidatos

    def obter_votos_por_regiao(self, candidato):
        for candidatos_info in self.__DAO.cache:
            if candidatos_info["nome"] == candidato:
                return candidatos_info["votos"]  # dicionário região:voto
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
        with open(nome_arquivo, 'r') as arquivo:
            self.__dados = json.load(arquivo)
            self.__DAO.cache = self.__dados
            self.__DAO.dump()
