#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# Hint: Use for loop to iterate all possible solutions.


heads = int(input('How many heads are there? '))

legs = 0
while True:
	legs = int(input('How many legs are there? '))
	if (legs % 2 == 0) and (legs > heads):
		break
	else:
		print('\nLegs must be an even number AND greater than number of heads.')

	

rabbits = int(legs/2) - heads
chickens = heads - rabbits

print('There are ', rabbits, ' rabbits.')
print('There are ', chickens, ' chickens.')
