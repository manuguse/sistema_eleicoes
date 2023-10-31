from model import Model
from view import View
class Controller:
    def __init__(self):
        self.model = Model([])
        self.view = View("Sistema de Eleições")
        self.view.init_window()