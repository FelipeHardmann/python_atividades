totalPessoas = 1
crianca = 1
adolescente = 1
semiAdulto = 1
adulto = 1
idoso = 1

while totalPessoas < 15:
    idade = int(input('Digite a sua idade: '))
    totalPessoas += 1
    if idade <= 15:
        print(f'Possuem {crianca} pessoas com a faixa etária menor que 15 anos')
        crianca += 1 
    elif 16 <= idade <= 30:
        print(f'Possuem {adolescente} pessoas com a faixa etária entre 16 e 30 anos')
        adolescente += 1
    elif 31 <= idade <= 45:
        print(f'Possuem {semiAdulto} pessoas com a faixa etária entre 31 e 45 anos')
        semiAdulto += 1
        totalPessoas += 1
    elif 46 <= idade <= 60:
        print(f'Possuem {adulto} pessoas com a faixa etária entre 46 e 60 anos')
        adulto += 1
    else:
        print(f'Possuem {idoso} pessoas com a idade maior que 60!')
        idoso += 1
        
    
print(f'Existem {crianca} crianças, {adolescente} entre 16 e 30, {semiAdulto} entre 31 e 45, {adulto} entre 46 e 60 e {idoso} maior do que 60')