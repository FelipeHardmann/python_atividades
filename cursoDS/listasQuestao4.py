impar = []
par = []

for i in range(0, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(par, end=' ')
print(min(par))
print(impar, end=' ')
print(min(impar))