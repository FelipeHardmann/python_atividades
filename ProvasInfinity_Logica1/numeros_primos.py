number1 = int(input('Digite um número inteiro e positivo: '))
number2 = int(input('Digite o segundo número inteiro e positivo: '))
total = 0

for c in range (number1, number2 + 1):
    if number1 and number2 % c == 0:
        print('\033[34m')
        total += 1
    if total == 0:
        print('É primo')
    else:
        print('Não são primos')
