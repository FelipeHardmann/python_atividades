valor = float(input('Digite seu valor por hora trabalhada: '))
hora = int(input('Digite sua quantidade de horas trabalhadas por mês: '))

salario_bruto = valor * hora


inss = 0.10
fgts = 0.11

if salario_bruto <= 900:
    desconto1 = salario_bruto * inss
    print(f'(-) INSS(10%)        :R${desconto1}')
    desconto2 = salario_bruto * fgts
    print(f'FGTS(11%)         :R${desconto2}')
    total_desconto = desconto1 + desconto2
    print(f'Total de descontos:     :R${total_desconto}')
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário líquido:     :R$:{salario_liquido}')
elif salario_bruto <= 1500:
    ir = 0.05
    desconto1 = salario_bruto * ir
    print(f'(-)IR(5%)       :R${desconto1}')
    desconto2 = salario_bruto * inss
    print(f'(-) INSS(10%)        :R${desconto2}')
    desconto3 = salario_bruto * fgts
    print(f'FGTS(11%)         :R${desconto3}')
    total_desconto = desconto1 + desconto2
    print(f'Total de descontos:     :R${total_desconto}')
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário líquido:     :R$:{salario_liquido}')
elif salario_bruto <= 2500:
    ir = 0.10
    desconto1 = salario_bruto * ir
    print(f'(-)IR(10%)       :R${desconto1}')
    desconto2 = salario_bruto * inss
    print(f'(-) INSS(10%)        :R${desconto2}')
    desconto3 = salario_bruto * fgts
    print(f'FGTS(11%)         :R${desconto3}')
    total_desconto = desconto1 + desconto2
    print(f'Total de descontos:     :R${total_desconto}')
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário líquido:     :R$:{salario_liquido}')
elif salario_bruto > 2500:
    ir = 0.20
    desconto1 = salario_bruto * ir
    print(f'(-)IR(20%)       :R${desconto1}')
    desconto2 = salario_bruto * inss
    print(f'(-) INSS(10%)        :R${desconto2}')
    desconto3 = salario_bruto * fgts
    print(f'FGTS(11%)         :R${desconto3}')
    total_desconto = desconto1 + desconto2
    print(f'Total de descontos:     :R${total_desconto}')
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário líquido:     :R$:{salario_liquido}')
