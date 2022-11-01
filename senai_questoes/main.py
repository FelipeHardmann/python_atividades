from re import X


def saudacao():
    print('Hello World')

def printNumber():
    x = int(input('Digite um número: '))
    print(f'O número é: {x}')

def somaNumeros():
    x = float(input('Digite um número: '))
    y = float(input('Digite outro número: '))
    z = x + y
    print(f'A soma de {x:.0f} + {y:.0f} é igual a: {z}')

def listaNotas():
    notas = []
    for i in range(1, 5):
        nota = float(input(f'Digite a {i}° nota: '))
        notas.append(nota)
        media = sum(notas) / len(notas)
    print(f'A média é {media}') 

def converterCm():
    metros = float(input('Digite o valor em metros: '))
    cm = metros * 100
    print(f'O valor em Centimetros é: {cm}')

def areaCirculo():
    raio = float(input('Digite o raio do circulo: '))
    area = 3.14 * (raio ** 2)
    print(f'A área tem o valor de: {area}')

def areaQuadrado():
    lado = float(input('Digite o lado do quadrado: '))
    area = (lado * area) * 2
    print(f'Área: {area}')

def salario():
    horas_trabalhas = float(input('Digite a quantidade de horas trabalhadas: '))
    valor_hora = float(input('Digite o seu valor hora: '))
    total = horas_trabalhas * valor_hora
    print(f'Total: R${total}')

def conversaoCelsius():
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = 5 * ((fahrenheit - 32) / 9)
    print(f'O temperatura em Celsius: {celsius}')

def conversaoFah():
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print(f'A temperatura em {fahrenheit}')

def numeros():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
