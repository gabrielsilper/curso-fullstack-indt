from abc import ABC, abstractmethod


class IRepository(ABC):
    __nameTable: str

    def __init__(self, nameTable) -> None:
        self.__nameTable = nameTable

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findById(self):
        pass

    def getNameTable(self):
        return self.__nameTable
