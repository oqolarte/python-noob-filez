# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

n = 1
apsf = [] #all primes so far

while True:
	print('Do you want to know the next prime number? y/n')
	response = str(input(''))
	if response == 'y': # start of Yes block
		pass
	elif response == 'n': # start of No block
		print('\nDone.')
		sys.exit()
	else: 
		print("\nPlease type only y or n\n")
