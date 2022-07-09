salario = float(input('Digite o salário: '))

if salario <= 280:
    salario = salario * 1.20
    print(salario)
elif 280 < salario <= 700:
    salario = salario * 1.15
    print(salario)
elif 700 < salario <= 1500:
    salario = salario * 1.10
    print(salario)
else:
    salario = salario * 1.05
    print(salario)