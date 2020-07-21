# a quadratic equation ax^2 + bx + c = 0 has either 0, 1, or 2 distinct solutions for real values of.
# given a, b, c, return the number of solutions to the equation.
# you do not have to calculate the solutions, just return how many there are.
# a will always be non-zero

def solutions(a, b, c):
	if a == 0:
		print('A must be non-zero\n')
	else:
		x1 = ((-b) + (b**2 - 4*a*c) ** 0.5)/(2*a)
		x2 = ((-b) - (b**2 - 4*a*c) ** 0.5)/(2*a)
		
		#print('x1 = ', x1)
		#print('x2 = ', x2)
		
		if isinstance(x1, complex) and isinstance(x2, complex):
			print('The eq has no solution\n')
		elif abs(x1)>0 and abs(x2)>0:
			print('The eq has 2 solutions\n')
		elif x1 == 0 and x2 ==0:
			print('The eq has 1 solution\n')
		else:
			print('The eq has no solutions\n')

print("Quadratic Equation Ax^2 + Bx+ C = 0 (press Ctrl + C to quit)\n")
		
while True:
	a = int(input('What is A? '))
	b = int(input('What is B? '))
	c = int(input('What is C? '))
	solutions(a, b, c)
