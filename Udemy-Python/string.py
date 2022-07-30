a = "Diego"
b = "Mariano"

concatenar = a + " " + b

print(concatenar)
print(concatenar.lower()) #Funçao que deixa tudo em minúsculo
print(concatenar.upper()) #Funçao que deixa tudo em maiúsculo


minha_string = 'O rato roeu a roupa do rei de Roma'

minha_lista = minha_string.split(" ") #Funçao que separa as strigns e serve também para retirar alguma letra
print(minha_lista)

busca = minha_string.find("rei")#Função para mostrar em que posição está a string
print(busca)


minha_string = minha_string.replace("do rei", "da rainha")
print(minha_string)