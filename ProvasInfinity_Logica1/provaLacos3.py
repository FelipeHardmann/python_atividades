nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
presenca = int(input('Digite a presença do aluno: '))

media = (nota1 + nota2 + nota3) / 3


if media >= 6 and presenca >= 40:
    print(f'O aluno está aprovado com {media} na média e com a presença de {presenca}')
elif media < 6 and presenca >= 40:
    print(f'O aluno está reprovado pela média ter ficado {media}')
elif media >= 6 and presenca < 40:
    print(f'O aluno está reprovado por possui apenas {presenca} de presença em sala')
else:
    print(f'Aluno reprovado por {media} na média e apenas {presenca} marcas de presença')
