#ler times

time1 = int(input('Digite a quantidade de gols do time 1: '))
time2 = int(input('Digite a quantidade de gols do time 2: '))

if time1 > time2:
    print('Time 1 foi o vencedor!')
elif time1 < time2:
    print('Time 2 foi o vencedor!')
else:
    print('Empate')