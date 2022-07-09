#Fahrenheit para celsius

tf = float(input('Digite a temperatura em Fahrenheit: '))

tc = ((tf - 32) * 5) / 9

print(f'A conversão da temperatura em Fahrenheit {tf}, para Celsius fica {tc:.2f}')
