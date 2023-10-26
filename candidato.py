class Candidato:
    
    def __init__(self, nome, numero, partido) -> None:
        self.__nome = nome
        self.__numero = numero
        self.__total_votos = 0
        self.__partido = partido