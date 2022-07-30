minha_lista = ['abacaxi', 'melancia', 'abacate']
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ['abacaxi', 2, 9.89, True]

print(minha_lista[0]) #Quando for colocado entre [] quer dizer que posso navegar pelos elemetos da lista


for item in minha_lista:
    print(item) #Vai imprimir item por item sem os []


tamanho = len(minha_lista) #A função len verifica o tamanho da lista
print(tamanho)


minha_lista.append('limão') #Insere um novo item para a lista
print(minha_lista)


if 3 in minha_lista_2:
    print('3 está na lista')

del minha_lista[2:] #Serve para remover itens da lista
print(minha_lista)