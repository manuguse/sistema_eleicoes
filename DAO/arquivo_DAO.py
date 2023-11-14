from DAO.DAO import DAO


class ArqDAO(DAO):
    def __init__(self):
        super().__init__('JSON/arquivos.json')
