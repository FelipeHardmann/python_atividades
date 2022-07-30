#Crie uma condição que avalie se o motorista está acima ou abaixo da velocidade média de uma via que tem como padrão 60 Km/h.

x = float(input("Digite a velocidade do carro: "))
if(x<60):
    print("A veículo estava abaixo da velocidade")
else:
    print("O veículo está acima da velocidade ideal", x)