#Condicional meio ambiente

indice = float(input('Digite o índice de poluição da indústria: '))

if 0.05 <= indice <= 0.25:
    print('O índice de poluição está aceitável')
elif  0.3 <= indice <= 0.39:
    print('As indústrias do 1° grupo precisam suspender as atividades')
elif 0.4 <= indice <= 0.49:
    print('As indústrias do 1° e 2° grupo precisam suspender as atividades')
else:
    print('Todos os grupos precisam suspender as atividades')