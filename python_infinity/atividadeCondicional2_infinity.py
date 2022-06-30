#Condicional de idade

age = int(input('Digite a sua idade: '))

if age <= 1:
    print('Récem nascido')
elif 2 <= age <= 12:
    print('Criança')
elif 13 <= age <= 18:
    print('Adolescente')
elif 19 <= age <= 60:
    print('Adulto')
else:
    print('Idoso')