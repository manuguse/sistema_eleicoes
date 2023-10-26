class Voto:
    def __init__(self, candidato:str, cidade:str, estado:str, num:int) -> None:
        self.__candidato = candidato
        self.__cidade = cidade
        self.__estado = estado
        self.__num = num
    
    @property
    def candidato(self):
        return self.__candidato
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def num(self):
        return self.__num
    