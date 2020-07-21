# Imagine that your friend is a cashier, but has a hard time counting back change to customers.
# Create a program that allows him to input a certain amount of change, and then print how 0.01, 0.05,0.25, 1.00, 5.00, 10.00 Philippine peso coins.


def sukli_calc(s): # s for sukli
	s01 = 0 # qty of 0.01 php, 1 sentimo
	s05 = 0 # qty of 0.05 php, 5 sentimo
	s25 = 0 # qty of 0.25 php, 25 sentimo
	p1 = 0 # qty of 1.00 php
	p5 = 0 # qty of 5.00 php
	p10 = 0 # qty of 10.00 php
	
	while s >= 10:
		s -= 10
		p10 += 1
		
	while s >= 5:
		s -= 5
		p5 += 1
		
	while s >= 1:
		s -= 1
		p1 += 1
		
	while s >= 0.25:
		s -= 0.25
		s25 += 1
		
	while s >= 0.05:
		s -= 0.05
		s05 += 1
		
	while s>= 0.01:
		s -= 0.01
		s01 += 1
		
	print('The coin denominations would be: ')
	print('Php 10 coin: ', p10)
	print('Php 5 coin: ', p5)
	print('Php 1 coin: ', p1)
	print('Php 0.25 coin: ', s25)
	print('Php 0.05 coin: ', s05)
	print('Php 0.01 coin: ', s01)


while True:
	sukli = float(input('\nInput the amount of change (or Ctrl + C to quit): '))
	sukli_calc(sukli)
