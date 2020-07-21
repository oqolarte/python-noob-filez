#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
def isPrime(n) : 
	# Corner cases 
	if (n <= 1) :
		return False
	if (n <= 3) :
		return True
		
	if (n % 2 == 0 or n % 3 == 0) :
		return False
	
	i = 5
	while(i * i <= n) :
		if (n % i == 0 or n % (i + 2) == 0) :
			return False
		i = i + 6
	return True
  
  
# Driver Program  
print(isPrime(int(input('Type an integer to check if it is prime: '))))
