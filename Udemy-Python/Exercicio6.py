#Crie um sistema que calcula o preço da passagem a partir da quilometragem, quando a viagem for menor que 250 km  valor do  Km será R$ 0,85 quando for maior R$ 0,65

x = float(input("Digite a distância da viagem: "))
if(x>=250):
    valor = x*0.65
    print("O valor da viagem será", valor)
else:
    valor = x*0.85
    print("O valor da viagem será", valor)