def format_number(num): #num is a non-negative integer
	x = [n for n in str(num)]
	print(x)
	y = x.insert(0, 'a')
	print(y)
	for i, numbers in enumerate(x):
		if -i // 3 == 0:
			x = x.insert(-i, ',')
		
z = int(input('Enter a non-negative integer: '))		
format_number(z)
