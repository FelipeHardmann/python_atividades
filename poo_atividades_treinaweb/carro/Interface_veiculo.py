'''
Duck-typing, método do python de criar uma interface
'''

from abc import ABC, abstractmethod

class InterfaceVeiculo(ABC):
    
    @abstractmethod
    def qtd_combustivel(self, qtd_abastecer):
        ...

    @abstractmethod
    def ligar(self):
        ...

    @abstractmethod
    def desligar(self):
        ...

    @abstractmethod
    def acelerar(self, velocidade = 10):
        ...

    @abstractmethod
    def nova_cor(self, nova_cor):
        ...