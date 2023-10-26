from data_DAO import data_DAO

class Model:
    def __init__(self) -> None:
        self.__candidatos = data_DAO('candidatos.json')
        
    def start(self):
        pass
        
    