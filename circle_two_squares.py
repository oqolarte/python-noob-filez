#imagine a circle and two squares: a smaller and a bigger one.
#for the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

#create a function, that takes an integer (radius of the circle) and returns the square area of the square inside the circle.

import math, os, sys

def square_areas_difference(radius): #radius is an integer
	print(2 * radius ** 2)	


while True:
	x = input('Type an integer Radius, or blank to quit: ')
	if x == '':
            sys.exit()
	else:
		square_areas_difference(int(x))
