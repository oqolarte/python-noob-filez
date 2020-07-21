myNum = int(input('Type in any positive integer: '))
fact = 1
while myNum:
	fact *= myNum
	myNum -= 1

print(fact)
