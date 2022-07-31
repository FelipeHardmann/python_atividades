dados = {}
nome = input('Digite seu nome: ').strip().title() #strip remove espaços em branco #title deixa a primeira letra maiúscula
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite a sua idade: '))
gmail = input('Digite o seu email: ')

dados['nome'] = nome
dados['sobrenome'] = sobrenome
dados['idade'] = idade
dados['email'] = gmail

for indice, dado in enumerate(dados.items(), start=1):
    print(indice, dado, sep=' - ')

'''print(list(enumerate(dados.items())))'''
