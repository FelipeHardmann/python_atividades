from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

unozinho = Carro('Amarelo', 'Flex', 200, 4)
unozinho.abastecer(50)
print(unozinho.ligar())
unozinho.acelerar(50)

unozinho.qtd_combustivel = 200
print(unozinho.__dict__)

moto = Moto('preta', 'flex', 200, 2)
# moto.abastecer(60)
# moto.abastecer(30)
# print(moto.__dict__)

if isinstance(moto, Veiculo):
    print('A classe é um veículo')
else:
    print('A class não é')
# print(Carro.mro())

# veiculo = Veiculo('Azul', 'flex', 200)
# veiculo.cor('verde')
# print(veiculo.ligar())
# print(veiculo.__dict__)

# xr = Moto('preta', 'flex', 200, 2)
# xr.abastecer(50)
# xr.acelerar(20)
# print(xr.ligar())
# xr.desligar()
# print(xr.acelerar())
# xr.ligar()
# print(xr.acelerar(50))


# print(unozinho.__dict__)
# print(xr.__dict__)
