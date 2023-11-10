import json


class Model:
    def __init__(self, DAO, DAO_arqs):
        self.__DAO = DAO
        self.__DAO_arqs = DAO_arqs
        self.__dados = None

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
        if nome_arquivo not in self.retornar_nome_arquivos():
            self.adicionar_arquivo_a_lista(nome_arquivo)
            with open(nome_arquivo, 'r') as arquivo:
                self.__dados = json.load(arquivo)
                self.somar_votos()
        else:
            raise Exception

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