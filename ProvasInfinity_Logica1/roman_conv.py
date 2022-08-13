def converte_romanos(numero: int) -> str:
    '''Esta função recebe um número inteiro positivo e retorna seu
    correspondente romano

    param:
        numero: inteiro positivo

    return:
        retorna uma string formatada em algarismo romano'''

    # Definição dos números romanos
    M = ['', 'M', 'MM', 'MMM']
    C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    # Cálculo para a conversão
    if numero == 0:
        return False, f'Não há correspondente para {numero}'

    milhares = M[numero // 1000]
    centenas = C[(numero % 1000) // 100]
    dezenas = X[(numero % 100) // 10]
    unidades = I[numero % 10]

    romano = milhares + centenas + dezenas + unidades

    return True, romano

num: int = int(input('Número: '))
conversao_valida, retorno = converte_romanos(num)
if conversao_valida:
    print(f'{num} = {retorno}')
else:
    print(f'{retorno}')

