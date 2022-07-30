lista = []
for i in range(0, 10):
    num = int(input('Digite um número: '))
    lista.append(num)
print(lista)
lista.sort(reverse = True)
print(lista)
lista.sort(reverse = False)
print(lista)