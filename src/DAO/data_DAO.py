from DAO.DAO import DAO


class DataDAO(DAO):
    def __init__(self):
        super().__init__('JSON/votos.json')
