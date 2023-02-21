from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, cor: str, tipo_combustivel: str, potencia: int, qtd_portas: int) -> None:
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas
    
    def ligar(self):
        if not self.is_ligado:
            self.is_ligado = True
            return 'Veiculo ligado'
        return 'Veiculo já ta ligado'

    def abastecer(self, qtd_abastecer):
        self.qtd_combustivel += qtd_abastecer
        return f'O método foi chamado a partir da classe carro' 
