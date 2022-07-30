num1 = int(input('Quantos termos você deseja mostrar? '))
fib1 = 0
fib2 = 1
print(f'{fib1} {fib2}', end=' ')

for i in range(num1):
    total = fib1 + fib2
    fib1 = fib2
    fib2 = total
    print(f'{total}', end=' ')
     