notas = []
dados = {}

nome = input('Digite seu nome: ').strip().title()
for i in range(4):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)
dados['Nome'] = nome
dados['Notas'] = notas
dados['maior_nota'] = max(notas)
dados['menor_nota'] = min(notas)
dados['media'] = sum(notas) / len(notas)
media = dados['media']
maiorNota = dados['maior_nota']
menorNota = dados['menor_nota']


if media >= 7:
    print(f'{nome} está aprovado com a média: {media}')
else:
    print(f'{nome} está reprovado com a média {media}')

print(f'A maior nota de {nome}, foi {maiorNota} e a menor nota foi {menorNota}', sep=' -------------- ')
print(dados)


