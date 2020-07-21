def collatz(n): # collatz conjecture
	collatz_steps = []
	while n != 1:
		if n % 2 == 0:
			n = n // 2
		elif n % 2 == 1:
			n = 3 * n + 1
		print(n)
		collatz_steps.append(n)
	print('\nIt took', len(collatz_steps), 'steps to reach n = 1.')

print("Collatz conjecture: Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.\n")
collatz(int(input('Enter positive integer: ')))
