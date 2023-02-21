from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

# unozinho = Carro('Amarelo', 'Flex', 200, 4)
# unozinho.abastecer(50)
# unozinho.ligar()
# unozinho.acelerar(50)

# xr = Moto('preta', 'flex', 200, 2)
# xr.abastecer(50)
# xr.acelerar(20)
# print(xr.ligar())
# xr.desligar()
# print(xr.acelerar())
# xr.ligar()
# print(xr.acelerar(50))

moto = Moto('preta', 'flex', 200, 2)
moto.abastecer(60)
moto.abastecer(30)
print(moto.__dict__)

# print(unozinho.__dict__)
# print(xr.__dict__)
