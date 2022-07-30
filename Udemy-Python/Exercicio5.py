#Crie uma condição que leia 3 números e diga qual deles é o maior eo menor.




x = int(input("Digite o 1° número: "))
y = int(input("Digite o 2° número: "))
z = int(input("Digite o 3° número: "))

if(x>y) and (x>z):
    print("O 1° número é o maior")
elif(y>x) and (y>z):
    print("O 2° número é o maior")
elif(z>x) and (z>y):
    print("O 3° número é o maior")



