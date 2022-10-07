#com intuito de organizar o pasto, o fazendeiro que andava 
# estudando a linguagem Python queria fazer um arranjo em sua fazenda  usando o 
# método de listas, sabendo disso ajude o agrônomo a realizar essa mudança. 
# Levando em consideração que no pasto 1 (que também é uma lista)tem  4 listas 
# com um animal diferente em cada(animais da sua escolha)e dentro dessas listas 
# havia 4 cores de animais(cores da sua escolha porém sempre diferentes),faça 
# um código responsável por mudar 3 listas de animais do pasto 1 para o pasto 2 
# que estava vazio e imprimindo o resultado final dos animais do pasto 2 e os animais do pasto 1 

#Exemplo de lista de animal:zebras=['zebras=',"branca","bege","preta"],
#OBS :Use as funções de manipulação de listas 

lista1Pasto = ['Boi=', 'preto', 'branco', 'rosa'], ['vaca=', 'lilas', 'azul', 'roxo'], ['carneiro=', 'marrom', 'branco', 'rosa'], ['galinha=', 'laranja', 'branco', 'rosa'] 

lista2Pasto = []

for i in range(3):
    lista2Pasto.append(lista1Pasto[i])

print(lista1Pasto)
print('#'*100)
print(lista2Pasto)
