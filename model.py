from data_DAO import DataDAO

class Model:
    def __init__(self, sistema) -> None:
        self.__candidatos_exemplo = DataDAO('candidatos.json')
        self.__sistema = sistema #json