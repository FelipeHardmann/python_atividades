notas = []
dados = {}

nome = input('Digite seu nome: ')
for i in range(4):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)
dados['Nome'] = nome
dados['Notas'] = notas

maiorNota = max(notas)
menorNota = min(notas)
media = sum(notas) / 4

if media >= 7:
    print(f'O aluno está aprovado com a média: {media}')
else:
    print(f'O aluno está reprovado com a média {media}')

print(f'A maior nota de {nome}, foi {maiorNota} e a menor nota foi {menorNota}', sep=' -------------- ')
print(dados)


