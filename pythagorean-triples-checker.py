a = int(input('what is the length of the first side? '))
b = int(input('what is the length of the second side? '))
c = int(input('what is the length of the third side? '))
trip = [a, b, c]

if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
	print(str(trip) + ' are pythagorean triples')
else:
	print(str(trip) + ' are not pythagorean triples')
