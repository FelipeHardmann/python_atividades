x = 'continuar'
contKm = 0

while x != 'pare':
    direcao = int(input('Digite um número para mudar de direção, se for para direita digite 1, se for para a esquerda digite 2, se quiser seguir em frente digite 3: '))
    if direcao == 1:
        contKm += 1
    elif direcao == 2:
        contKm += 1
    elif direcao == 3:
        contKm += 1
    x = input('Deseja continuar? Se sim digite "continuar", se não digite "pare" ')
print(f'Você pecorreu {(contKm * 100)} metros')
