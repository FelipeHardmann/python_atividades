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
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite um número inteiro: '))
    num3 = float(input('Digite um número real: '))
    a = ((num1 * num1) * 2) + (num2 / 2)
    b = (num1 * 3) + num3
    c = num3 ** 3

    print(f'Letra A: {a}\n')
    print(f'Letra B: {b}\n')
    print(f'Letra C: {c}')

def pesoIdeal():
    altura = float(input('Digite sua altura: '))
    peso_ideal = (72.7 * altura) - 58

    print(f'Seu calculo de peso ficou: {peso_ideal}')

def calcularPeixe():
    peso = float(input('Digite o peso do peixe: '))
    if peso > 50:
        valor_pagar = (peso - 50) * 4
    print(f'O valor a pagar é de {valor_pagar}')

def salario_total():
    horas_trabalhas = float(input('Digite a quantidade de horas trabalhadas: '))
    valor_hora = float(input('Digite o seu valor hora: '))
    valor_total = horas_trabalhas * valor_hora
    ir = valor_total * 0.11
    inss = valor_total * 0.08
    sind = valor_total * 0.05
    valor_total = valor_total - (ir + inss + sind)
    
    print(f'O salário bruto é: {valor_total}\n')
    
    print('#' * 100)

    print('Impostos: \n')
    print(f'INSS: {inss}\nImposto de Renda: {ir}\nSindicato: {sind}\n')

    print('#' * 100)

    print(f'Salário líquido: {valor_total}')

    print('#' * 100)

    print(f'Descontos: {ir + inss + sind}\n Salário Líquido: {valor_total}')

    print('#' * 100)

    print(f'+ Salário Bruto: R${valor_hora * horas_trabalhas}')
    print(f'- IR: R${ir}')
    print(f'- INSS: R${inss}')
    print(f'- Sindicato R${sind}')
    print(f'= Salário Líquido: R${valor_total}')

def loja_tintas():
    metros = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

    litro = metros / 3
    lata_tinta = litro / 18
    valor_total = lata_tinta * 80
    quantidade_latas = valor_total / 80 

    print(f'A quantidade de litros que será usado são: {litro:.2f}')
    print(f'A quantidade de latas será de: {lata_tinta:.2f}')
    print(f'O valor gasto será de: {valor_total:.2f}')
    print(f'A quantidade de latas de tinta será: {quantidade_latas :.2f}')