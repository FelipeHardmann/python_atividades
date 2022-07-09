# Função enumerate

lista = ['abacate', 'bola', 'cachorro']

'''for i in range(len(lista)):
    print(i, lista[i])'''

for i, nome in enumerate(lista):
    print(i, nome)