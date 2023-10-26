from voto import Voto
from DAO import DAO

class DataDAO(DAO):
    def __init__(self, database) -> None:
        super().__init__(database)
        self.__data = []
        
    def add_votes(self):
        for vote in super().cache:
            self.__data.append(Voto(vote['candidato'], vote['cidade'], vote['estado'], vote['num']))