nomes = []
listaDistancia = []
dados = {}

for i in range(1, 6):
    nome = input(f'Digite o nome do {i}° asteroide: ').strip().title()
    distancia = float(input(f'Digite a distância entre {nome} e a terra: '))
    nomes.append(nome)
    listaDistancia.append(distancia)
dados['Nome'] = nomes
dados['distancia_media'] = sum(listaDistancia) / len(listaDistancia)
dados['Distancia'] = listaDistancia

distanciaMedia = dados['distancia_media']

print(f'A distância média entre os asteroides registrados foi de {distanciaMedia}')
print(dados)