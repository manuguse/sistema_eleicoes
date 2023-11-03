from view import View
from model import Model
from data_DAO import DataDAO
from controller import Controller

class Main:
    def __init__(self):
        data_dao = DataDAO()
        model = Model(data_dao)
        controller = Controller(view=None, model=model)
        view = View(controller)
        controller.view = view
        self.controller = controller

    def init(self):
        self.controller.iniciar_aplicativo()

if __name__ == "__main__":
    main = Main()
    main.init()
