inicio = int(input('Digite o número inicial: '))
final = int(input('Digite o número final: '))

for num in range(inicio, final + 1):
    if num == 1:
        continue
    for numero in range(2, num):
        if num % numero == 0:
            break
    else:
        print(num, end=' ')