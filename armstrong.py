#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  armstrong.py
#  
#  Armstrong number, in a given number base b, is a number that is the sum of its own digits each raised to the power of the number of digits

def arm_process(a): # a is a list of digits of an integer
	a_p = 0
	for x in a:
		a_p += x ** len(a)
	return a_p

def armstrong(n):
	if 0 <= n <= 9:
		print(n,"is an Armstrong number. All single digits are.")
	elif n>= 10:
		digits = [int(x) for x in str(n)]
		if n == arm_process(digits):
			# print(n, "is an Armstrong number.")
			return True
		else:
			# print(n,"is not narcissistic.")
			return False
		
print('This program checks whether an integer is an Armstrong number.\n')
# armstrong(int(input('Type an integer: ')))

for x in range(10_000_001):
	if armstrong(x) == True:
		print(x)
