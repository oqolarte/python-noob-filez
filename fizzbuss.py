for n in range(100_001):
    if n % 15 == 0:
        print('Fizzbuzz!')
    elif n % 5 == 0:
        print('Buzz!')
    elif n % 3 == 0:
        print('Fizz!')
    else:
        print(n)
