# Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, 
#  while those that do not end in 1 are unhappy numbers. Display an example of your output here. 
#  Find first 8 happy numbers.


num = int(input('Enter a positive integer to start looking for happy numbers: '))

def digitize(x): #breaks down a number into its digits and returns a list
	digits = [int(d) for d in str(x)]
	return digits #digits is a list


print(digitize(num))
print('\n***\n') #visual divider

happy_list = [] #actual list of happy numbers

def happy_loop(y):
	sumA = 0
	sumB = 0
	digits = digitize(y)
	for i in digits:
		sum = sum + i ** 2
		if sum == 1: #checker if the n is already a happy number
			happy_list.append(y) #n will be appended in the happy_list
			#return 1
		else:
			return happy_loop(sum)


			
while len(happy_list) <= 8:
	if happy_checker(num):
		happy_list.append(num)
	else:
		print(num,' is not a happy number.')
	num += 1
	
print(happy_list)


