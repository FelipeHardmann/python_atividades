from statistics import median


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media > 6:
    print(f'Sua nota foi {media:.2f} e você está aprovado!')
else:
    print(f'Sua nota foi {media:.2f} e você está reprovado')