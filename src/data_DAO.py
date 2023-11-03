from DAO import DAO


class DataDAO(DAO):
    def __init__(self):
        super().__init__('votos.json')
