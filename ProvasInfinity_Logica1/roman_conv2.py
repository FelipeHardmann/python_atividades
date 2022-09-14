'''num_romanos = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 
'XII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI']

anoNascimento = int(input('Digite o ano que você nasceu: '))

num = num_romanos[anoNascimento // 100]
print(num)'''



def converterRoman():
    num_romanos = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 
    'XII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI']

    anoAtual = input('Digite o ano: ')
    if anoAtual.isdigit():
        anoAtual = int(anoAtual)
    else:
        print('Digite um ano')
        pass

    numero = num_romanos[anoAtual // 100]

    print(numero)

converterRoman()