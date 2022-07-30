vazamentos = int(input('Digite a quantidade de vazamentos: '))
total = 0

for i in range(0, vazamentos):
    hora = int(input('Digite a quantidade de horas que ficou com vazamento: '))
    qntAgua = int(input('Digite a quantidade de água em litros que foi desperdiçada: '))    
    litros = qntAgua * hora
    total += litros
print(total)

