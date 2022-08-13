nomes = []
listaDistancia = []
dados = {}
distanciaMedia = 0

for i in range(1, 6):
    nome = input(f'Digite o nome do {i}° asteroide: ').strip().title()
    distancia = float(input(f'Digite a distância entre {nome} e a terra: '))
    nomes.append(nome)
    listaDistancia.append(distancia)

dados = dict(zip(nomes, listaDistancia))
distanciaMedia = sum(listaDistancia) / len(listaDistancia)

print(f'A distância média entre os asteroides registrados foi de {distanciaMedia}')
print(dados)