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
		return True
		print(n,"is an Armstrong number. All single digits are.")
	elif n>= 10:
		digits = [int(x) for x in str(n)]
		if n == arm_process(digits):
			# print(n, "is an Armstrong number.")
			return True
		else:
			# print(n,"is not narcissistic.")
			return False
			
def arm_proof(n):
	digits = [int(x) for x in str(n)]
	print('PROOF:')
	print(n,'has',len(digits),'digit(s).')
	print(n, '= ', end='')
	i = 0
	while i != len(digits) - 1:
		print(digits[i],'^',len(digits), end=' + ')
		i += 1
	print(digits[-1],'^',len(digits))
	print(n, '= ', end='')
	j = 0
	while j != len(digits) - 1:
		print(digits[j] ** len(digits), end=' + ')
		j += 1
	print(digits[-1]** len(digits))
				

print('This program checks whether an integer is an Armstrong number.\n')
num = int(input('Type an integer: '))
if armstrong(num) == True:
	print(num,'is an Armstrong number.')
	arm_proof(num)
else:
	print('No')


