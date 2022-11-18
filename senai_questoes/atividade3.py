# Questão 1

# Guardar um número sorteado entre 1 e 10 e pedir para 
# que o usuário tente  acertar este valor. Avise a ele se 
# o número que ele informou é maior ou  menor do número 
# sorteado e mostre a mensagem quando ele acertar!

from random import randint

def sortear():
    num = randint(1, 10)
    while True:
        num_usuario = int(input('Digite um número entre 1 e 10: '))
        if num_usuario == num:
            print('Acertou')
            break
        elif num > num_usuario:
            print('O número é maior')
        elif num < num_usuario:
            print('O número é menor')
        

# ======================================================

# Questão 2
# Uma empresa de exportação de Eletrodos vende contêineres com
# valores fixos  por toneladas. Um caminhão pode sair com várias
# toneladas e foi preciso  desenvolver um sistema para calcular 
# o valor mensal faturado.
# Desenvolva este sistema que irá solicitar o valor fixo da 
# tonelada no início do  programa e peça para o usuário quantas 
# vezes forem necessárias a  quantidade de toneladas que saiu 
# (cada mês pode sair quantidade diferente).  Ao final, mostre 
# o valor total faturado.

def calcula_toneladas():
    toneladas = []
    while True:    
        valor = float(input('Digite o valor da tonelada: '))
        toneladas.append(valor)
        print(f'O valor das toneladas durante o mês está {sum(toneladas)}')


# ==========================================================

# Questão 3

# Você foi convidado a desenvolver um módulo de um sistema  
# acadêmico. Você precisa capturar quantas notas o usuário  
# necessitar e calcular a média dela, exibindo o resultado final.

def calcular_notas():
    notas = []
    qtd_notas = int(input('Digite a quantidade de notas: '))
    for i in range(1, qtd_notas + 1):
        nota = float(input(f'{i}° nota: '))
        notas.append(nota)
    print(f'A média do aluno foi de {sum(notas)/len(notas)}')


# ==========================================================

# Questão 4

# Um instituto de pesquisa entre portadores de 
# COVID-19 selecionou uma amostra de 10 pacientes em 
# uma  região no intuito de saber a porcentagem de:
# Pacientes com sintomas leves da doença;
# Pacientes assintomáticos;
# Pacientes com sintomas graves da doença.
# Ao final, o intuito é obter uma porcentagem de cada uma 
# das classificações acima. Crie um algoritmo para  
# auxiliar o instituto a registrar e calcular este percentual.


def covid():
    grave = []
    leve = []
    assitomatico = []
    while True:
        doente = input('Digite se o paciente tem sintoma Leve/Assintomático/Grave: ').title()
        if doente == 'Leve':
            leve.append(doente)
        elif doente == 'Assintomático':
            assitomatico.append(doente)
        elif doente == 'Grave':
            grave.append(doente)
        print(f'A quantidade de pessoas com sintomas leves é de: {len(leve)}')
        print(f'A quantidade de pessoas com sintomas graves é de: {len(grave)}')
        print(f'A quantidade de pessoas Assintomáticas é de: {len(assitomatico)}')
        print(f'A quantidade de pessoas pesquisadas é de: {len(leve) + len(grave) + len(assitomatico)}')
        print('#' * 50)


# ################################################################
def contarVogais():
    palavra = input('Palavra: ').lower()
    vogal = "aeiou"
    totalVogal = 0

    for letra in palavra:
        if letra in vogal:
            totalVogal += 1

    print(totalVogal)

contarVogais()