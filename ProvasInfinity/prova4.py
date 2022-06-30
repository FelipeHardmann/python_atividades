tempo = float(input('Digite o tempo da viagem: '))
velocidade = float(input('Digite a valocidade média do automóvel: '))

distancia = tempo * velocidade

litros_usados = distancia / 12

print(f'A velocidade média do automóvel é {velocidade}, o tempo gasto será de {tempo}, a distância será de {distancia} e a quantidade de litros necessários é de {litros_usados}')