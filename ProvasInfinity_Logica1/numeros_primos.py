num = input('Número: ')
cont = 0

if num.isdigit():
    num = int(num)

for i in range(2, num + 1):
    if num % i == 0:
        cont += 1

if cont == 1:
    print('É primo')
else:
    print('Não é primo')