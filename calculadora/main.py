# Após vários dias tentando solucionar um erro dado no aplicativo da calculadora de um computador de uma
# empresa, o técnico de TI e seu estagiário  decidiram fazer um código na linguagem Python que tivesse
# as funcionalidades de uma calculadora, porém ao não obtiveram êxito nesse projeto. Para resolver esse
# problema lhe foi solicitado que você que desenvolvesse uma programa de uma  calculadora em Python. 
# Como você faria? Então desenvolva uma calculadora em Python que tenha como funções: soma, divisão,
# subtração e adição, a calculadora tem que ter um menu para as operações e mostrar o resultado final.
# Além dessas funcionalidades lhe foi solicitado que o arquivo principal do programa fosse diferente
# do(s) arquivo da funcionalidade da calculadora. 
# Importante: use o assunto de módulos e caso seja necessário suba a pasta dos arquivos da questão
# no drive e disponibilizando o link da questão.

from calculadora import Calculadora


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

operacao = Calculadora(num1, num2)

escolha = input('Digite qual operação você deseja realizar: ')

if escolha == '*':
    print(operacao.multiplicar())
elif escolha == '/':
    print(operacao.dividir())
elif escolha == '+':
    print(operacao.somar())
elif escolha == '-':
    print(operacao.subtrair())