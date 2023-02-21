class Veiculo:
    def __init__(self, cor: str, tipo_combustivel: str, potencia: int) -> None:
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        return f'O objeto foi removido'

    def abastecer(self, qtd_abastecer):
        self.qtd_combustivel += qtd_abastecer

    def ligar(self):
        if not self.is_ligado:
            self.is_ligado = True
            return 'Veiculo ligado'
        return 'Veiculo já ta ligado'
    
    def desligar(self):
        if self.is_ligado:
            self.is_ligado = False
        return 'O veiculo já está desligado'

    def acelerar(self, velocidade = 10):
        if not self.is_ligado:
            return f'O veiculo está desligado, ligue ele para poder acelerar'
        self.velocidade += velocidade
        return f'O veiculo está acelerando com {self.velocidade}'

