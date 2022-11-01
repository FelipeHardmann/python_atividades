dic = {}
asteroide = input('Digite o nome do asteroide: ')
listaDistancia = []

for i in range(5):
    distancia = float(input('Digite as últimas distâncias que o asteroide passou pela terra: '))
    listaDistancia.append(distancia)

dic.update({asteroide: listaDistancia})

total = sum(listaDistancia) / len(listaDistancia)

for c, v in dic.items():
    print(f'O asteroide: {c} teve uma distância média de {total}')