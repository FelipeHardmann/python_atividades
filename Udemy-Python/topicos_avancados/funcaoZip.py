# função Zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ['abacate', 'Bola', 'cachorro', 'dinheiro', 'elefante']

for numero, nome in zip(lista1, lista2):
    print(numero, nome)