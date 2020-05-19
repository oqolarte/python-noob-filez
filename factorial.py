import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
	logging.debug('Start of factorial (%s)' % (n))
	total = 1
	for i in range(1, n+1):
		total *= i
		logging.debug('i is %s, total is %s' % (i, total))
	
	logging.debug('Return value of %s' % (total))
	return total
	
print(factorial(int(input('Input any number to get its factorial: '))))

logging.debug('End of Program')
