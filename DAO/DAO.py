import json
from abc import ABC, abstractmethod


class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, cache):
        self.__cache = cache

    def dump(self):
        with open(self.__datasource, 'w') as file:
            json.dump(self.__cache, file)

    def load(self):
        with open(self.__datasource, 'r') as file:
            self.__cache = json.load(file)

    def add(self, key, obj):
        self.__cache[key] = obj
        self.dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            del self.__cache[key]
            self.dump()
        except KeyError:
            pass

    def get_all(self):
        return list(self.__cache.values())
