from MVC.view import View
from MVC.model import Model
from DAO.data_DAO import DataDAO
from DAO.arquivo_DAO import ArqDAO
from MVC.controller import Controller

import sys
sys.dont_write_bytecode = True


class Main:
    def __init__(self):
        data_dao = DataDAO()
        arq_dao = ArqDAO()
        model = Model(data_dao, arq_dao)
        controller = Controller(view=None, model=model)
        view = View(controller)
        controller.view = view
        self.controller = controller
        model.registrar_observador(controller)
        controller.registrar_observador(model)

    def init(self):
        self.controller.iniciar_aplicativo()

if __name__ == "__main__":
    main = Main()
    main.init()
