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
