from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, cor: str, tipo_combustivel: str, potencia: int, qtd_passageiros: int) -> None:
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def ligar(self):
        if not self.is_ligado:
            self.is_ligado = True
            return 'Moto ligado'
        return 'Moto já ta ligado'

    def abastecer(self, qtd_abastecer):
        print('O método foi chamado a partir da classe moto')
        if self.qtd_combustivel > 40:
            print('A quantidade máxima de combustível é de 40L')
            return self.qtd_combustivel    
        self.qtd_combustivel += qtd_abastecer

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

    def nova_cor(self, nova_cor):
        self.cor = nova_cor
