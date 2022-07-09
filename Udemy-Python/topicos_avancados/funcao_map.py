# Função Map

def dobro(x):
    return x * 2

valor = [1, 2, 3, 4, 5]
'''print(dobro(valor))'''
valor_dobrado =  map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)
