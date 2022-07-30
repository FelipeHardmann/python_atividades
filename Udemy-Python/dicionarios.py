dicionario = {'A' : 'Ameixa', 'B': 'Bola', 'C': 'Cachorro'}

print(dicionario['A']) #Dicionário você só precisa colocar a chave, diferente da lista

for chave in dicionario:
    print(chave + '-' + dicionario[chave])

for i in dicionario.items(): #Função para separar o valor e a chave
    print(i)

for k in dicionario.keys(): #Função para mostrar as chaves 
    print(k)