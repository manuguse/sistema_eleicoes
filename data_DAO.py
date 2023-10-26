from voto import Voto
from DAO import DAO

class VotoDAO(DAO):
    def __init__(self, database) -> None:
        super().__init__(database)

    def add(self, voto: Voto) -> None:
        if isinstance(voto, Voto) and (voto is not None):
            super().cache[voto.codigo] = voto.nome
            print(self.cache)
            self.dump()

    def get(self, key: int) -> Voto:
        print(key)
        if (type(key) == int):
            print('entrou')
            return super().get(key)
        
    def get_name(self, name):
        for key, val in self.cache.items():
            if val == name:
                return key
        return None
        
    def remove(self, key: int) -> None:
        if (isinstance(key, int)):
            return super().remove(key)