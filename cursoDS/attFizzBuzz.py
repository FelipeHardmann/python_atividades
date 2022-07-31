fizz = []
buzz = []
fizzbuzz = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        fizzbuzz.append(num)
        print(f'FizzBuzz -----> {fizzbuzz}')
    elif num % 3 == 0:
        fizz.append(num)
        print(f'Fizz ------> {fizz}')
    elif num % 5 == 0:
        buzz.append(num)
        print(f'Buzz ------> {buzz}')


