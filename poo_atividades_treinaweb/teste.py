import inspect
import abc

class Veiculo(abc.ABC):
    def __init__(self):
        self.__nome = None
        self.__tipo = None
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def tipo(self):
        return self.__tipo

    @nome.setter
    @abc.abstractmethod
    def nome(self, nome):
        pass

    @tipo.setter
    @abc.abstractmethod
    def tipo(self, tipo):
        pass


class Carro(Veiculo):
    def nome(self, nome):
        self.nome = nome

    def tipo(self, tipo):
        self.tipo = tipo
        


if __name__ == "__main__":
    [print(i) for i in list(map(lambda x: x[1].__qualname__,inspect.getmembers(Carro, lambda m: inspect.isfunction(m))))]

    c = Carro()

    c.nome = input()
    c.tipo = input()

    print(c.nome)
    print(c.tipo)