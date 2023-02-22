from abc import ABC, abstractmethod
from Interface_veiculo import InterfaceVeiculo

class Veiculo(InterfaceVeiculo ,ABC):
    '''
    Classe pai que recebe os atributos principais
    E extends a classe InterfaceVeiculo
    '''
    def __init__(self, cor: str, tipo_combustivel: str, potencia: int) -> None:
        self._cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.__qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        '''Método que vai apagar objeto instanciado'''
        return f'O objeto foi removido'
    
    @property
    def qtd_combustivel(self):
        '''Decorator para buscar o atributo privado'''
        return self.__qtd_combustivel

    @qtd_combustivel.setter
    def qtd_combustivel(self, qtd_abastecer):
        '''Decorator para modificar o atributo'''
        self.__qtd_combustivel += qtd_abastecer

    @property
    def cor(self):
        return self.__cor

    def nova_cor(self, nova_cor):
        self.__cor = nova_cor

    def ligar(self):
        '''método para ligar o veículo'''
        if not self.is_ligado:
            self.is_ligado = True
            return f'{__class__.__name__} ligado'
        return 'Veiculo já ta ligado'

    def desligar(self):
        '''Método para desligar o véiculo'''
        if self.is_ligado:
            self.is_ligado = False
        return 'O veiculo já está desligado'

    def acelerar(self, velocidade = 10):
        '''Método para acelerar o veículo'''
        if not self.is_ligado:
            return f'O veiculo está desligado, ligue ele para poder acelerar'
        self.velocidade += velocidade
        return f'O veiculo está acelerando com {self.velocidade}'

