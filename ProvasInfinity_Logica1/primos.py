inicio = int(input('Início: '))
final = int(input('Final: '))

# Faço a varredura no intervalo especificado
for numero in range(inicio, final+1):
    # Com o primeiro número lido,vejo se é divisível no intervalo de 2 até o
    # número sem incluí-lo, pois sempre será divisível por ele mesmo e por 1 
    for num in range(2, numero):
        if numero % num == 0:
            break
    # Acima testo se alguma divisão for válida, e aí saio desse laço e não
    # imprimo o número, mas se o if sempre for verdadeiro, o número é primo.
    # Executo o else
    else:
        print(numero, end=' ')

