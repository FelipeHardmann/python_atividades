notaTotal = [] 

for i in range(1, 5):
    notas = int(input('Digite a sua nota: '))
    notaTotal.append(notas)
    media = sum(notaTotal) / 4
if media >= 7:
    print(f'A média desse aluno foi: {media} e ele está aprovado!')
elif 5 <= media < 7:
    print(f'A média desse aluno foi: {media} e ele está de recuperação!')
else:
    print(f'A média desse aluno foi {media} e ele está reprovado') 