#Crie uma condição que avalie o salário da pessoa e calcule se o valor da parcela está no máximo 30% do 
# valor do salário e libere ou negue o crédito

x = float(input("Digite o valor do seu salário: "))
y = float(input("Digite o valor da sua parcela: "))

credit = (x * 30) / 100

if(credit>=y):
    print("O crédito será liberado")
else:
    print("Crédito negado")