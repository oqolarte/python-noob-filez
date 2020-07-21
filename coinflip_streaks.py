import random
numberOfStreaks = 0
for experimentNumber in range(10001):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = 0
    list = []
    while True:
        coin = ''
        if random.randint(0, 1) == 0:
            coin = 'H'
        else:
            coin = 'T'
        list = list + [coin]
        # Code that checks if there is a streak of 6 heads or tails in a row.
        for i in list:
            n = 0
            currentStreak = 0
            if list[n] == 'H':
                currentStreak += 1
                if currentStreak >= 6:
                    numberOfStreaks += 1
            else:
                currentStreak == 0
            n += 1
            if n == 100:
                break       
        flips += 1
        if flips == 100:
            break
    print(list)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(experimentNumber)