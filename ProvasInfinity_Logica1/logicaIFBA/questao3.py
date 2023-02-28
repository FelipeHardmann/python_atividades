idade = int(input('Idade: '))

anos = int(idade / 365)
saldo = idade - anos * 365
mes = int(saldo / 30)
dias = saldo - mes * 30
print(f'Anos: {anos}\nMes: {mes}\nDias: {dias}')
