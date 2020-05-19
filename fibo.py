def fibonacci(): #num is an integer representing the number of fibonacci numbers, and then prints them
    num = int(input("How many Fibonacci number to be generated? "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    return fib
#5702887
print(fibonacci())

