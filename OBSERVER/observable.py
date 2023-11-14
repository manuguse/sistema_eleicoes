from abc import ABC, abstractmethod


# objeto observado, que armazena a lista de objetos que o observa e a logica de negocio
class Observable(ABC):
    def __init__(self):
        self.__observadores = [] # o model vai ser um observador que, quando o estado do controller(observado) ser de receber um arquivo, ele vai atualizar o vencedor 
        self.__state = "Inative" # quando o model retornar o novo ganhador, ele que tambem sera observavel, o controller vai soltar um popup avisando do novo ganhador

    def registrar_observador(self, observador):
        self.__observadores.append(observador)

    def remover_observador(self, observador):
        self.__observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.__observadores:
            observador.update(self)
    
    @abstractmethod
    def mudar_estado(self):
        pass #TODO
    
    @property
    def observadores(self):
        return self.__observadores
    
    @observadores.setter
    def observadores(self, val):
        if isinstance(val, list):
            self.__observadores = val
