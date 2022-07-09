metros = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

litro = metros / 3
lata_tinta = litro / 18
valor_total = lata_tinta * 80
quantidade_latas = valor_total / 80 

print(f'A quantidade de litros que será usado são: {litro:.2f}')
print(f'A quantidade de latas será de: {lata_tinta:.2f}')
print(f'O valor gasto será de: {valor_total:.2f}')
print(f'A quantidade de latas de tinta será: {quantidade_latas :.2f}')



