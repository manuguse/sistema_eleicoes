class Candidato:
    def __init__(self, nome, votos):
        self.nome = nome
        self.votos = votos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def votos(self):
        return self.__votos

    @votos.setter
    def votos(self, votos):
        self.__votos = votos

    def atualizar_votos(self, regiao, quantidade):
        if regiao in self.votos:
            self.votos[regiao] += quantidade
        else:
            self.votos[regiao] = quantidade

    def __str__(self):
        return f"Nome: {self.nome}, Votos: {self.votos}"
