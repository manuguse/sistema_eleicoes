from typing import Callable
from abc import ABC, abstractclassmethod


class Subject(ABC):
    def __init__(self) -> None:
        self.__obeservers: list[Callable] = []

    def subscribe(self, observer_callback: Callable) -> None:
        self.__obeservers.append(observer_callback)

    def unsubscribe(self, observer_callback: Callable) -> None:
        self.__obeservers.remove(observer_callback)

    @abstractclassmethod
    def handle_events(self) -> None:
        pass

    @abstractclassmethod
    def notify(self) -> None:
        pass

    def get_observers(self) -> list[Callable]:
        return self.__obeservers
