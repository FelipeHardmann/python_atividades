
n = int(input('Digite um número para calcular o fatorial: '))
cont = n
result = 1

while cont > 0:
    print(f'{cont}*', end='')
    result *= cont
    cont -= 1
print(f'O fatorial de {n} é {result}')
