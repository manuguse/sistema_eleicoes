import json
from abc import ABC, abstractmethod


class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__cache = []
        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, cache):
        if isinstance(cache, list):
            self.__cache = cache

    def dump(self):
        with open(self.__datasource, 'w') as file:
            json.dump(self.__cache, file)

    def load(self):
        with open(self.__datasource, 'r') as file:
            self.__cache = json.load(file)

    def add(self, obj):
        self.__cache.append(obj)
        self.dump()

    #def get(self, key):
    #    try:
    #        return self.__cache[key]
    #    except KeyError:
    #        pass

    #def remove(self, key):
    #    try:
    #        del self.__cache[key]
    #        self.dump()
    #    except KeyError:
    #        pass

    def get_all(self):
        return self.__cache