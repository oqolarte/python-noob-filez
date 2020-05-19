# list of prime numbers, the index of which is by user input
import sys

primes = [] #list of primes
x = int(input('How many prime numbers do you want listed? '))

def factors(x):
	a = []
	for i in range(1, x + 1):
		if x % i == 0:
			a.append(i)
	return a

while len(primes) == x:
	n = 2
	f = factors(n)
	while len(f) != 2:
		n += 1
		primes.append(n)
print(primes)
