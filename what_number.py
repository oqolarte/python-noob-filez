#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Between 1 and 1000, there is only 1 number that meets the following criteria:

# The number has two or more digits.
# The number is prime.
# The number does NOT contain a 1 or 7 in it.
# The sum of all of the digits is less than or equal to 10.
# The first two digits add up to be odd.
# The second to last digit is even and greater than 1.
# The last digit is equal to how many digits are in the number.
 
def sum_digits(int_list): # summation of digits of a number
	sum = 0
	for n in int_list:
		sum += n
	return sum
	
def isPrime(n): # prime checker
	# Corner cases 
	if (n <= 1):
		return False
	if (n <= 3):
		return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop
	if (n % 2 == 0 or n % 3 == 0) :
		return False
	
	i = 5
	while(i * i <= n) :
		if (n % i == 0 or n % (i + 2) == 0) :
			return False
		i = i + 6
	return True

for n in range(10,1001): # The number has two or more digits.
	if isPrime(n):
		no_1_7 = str(n) 
		if ('1' or '7') not in no_1_7: # The number does NOT contain a 1 or 7 in it.
			t = [int(x) for x in str(n)]
			s = sum_digits(t)
			if s <= 10: # The sum of all of the digits is less than or equal to 10.
				o = t[0] + t[1]
				if o % 2 != 0: # The first two digits add up to be odd.
					if (t[-2] % 2 == 0) and (t[-2] > 1):
						if t[-1] == len(t):
							print(n)
