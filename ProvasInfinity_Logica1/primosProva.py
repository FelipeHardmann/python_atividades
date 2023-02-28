inicio = int(input('Numero 1: '))
final = int(input('Numero final: '))

for i in range(inicio, final):
    if i == 1:
        continue
    for num in range(2, i):
        if i % num == 0:
            break
    else:
        print(i, end=' ')
