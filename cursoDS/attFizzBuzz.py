fizz = []
buzz = []
fizzbuzz = []
num = int(input('Digite um número para ver se ele é Fizz, Buzz ou FizzBuzz: '))

if num % 3 == 0 and num % 5 == 0:
    fizzbuzz.append(num)
    print(fizzbuzz)
elif num % 3 == 0:
    fizz.append(num)
    print(fizz)
elif num % 5 == 0:
    buzz.append(num)
    print(buzz)


