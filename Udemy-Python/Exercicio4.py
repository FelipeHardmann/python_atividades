#Crie uma condição que através da média de 3 notas diga se o aluno está aprovado ou reprovado ou de recuperação.

x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
z = float(input("Digite a terceira nota: "))

media = (x+y+z)/3

if(media<7):
    print("O aluno está reprovado")
else:
    print("O aluno passou")



