num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    
sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]



ano = int(input('Digite o seu ano de nascimento para converter para século em números romanos: '))
seculo = ano // 100 + 1
print(seculo) 
