num1 = input('Digite um número inteiro: ')

if num1.isdigit():
    num1 = int(num1)
    if num1 % 2 == 0:
        print(f'O número {num1} é par')
    else:
        print(f'O número {num1} é ímpar')
else:
    print('Você precisa digitar um número inteiro')