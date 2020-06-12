def printBday(itemsDict, leftWidth, rightWidth): # prints the birthdays neatly
    print("BIRTHDAY LIST".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

bdays = {'Isya':'16 Jun', 'Mads':'9 Jan', 'Charles':'3 Nov'}

while True:
	name = input('\nEnter a name (blank to quit): ')
	if name == '':
		break
	if name in bdays:
		print(bdays[name] + ' is the birthday of ' + name + ' \n')
	else:
		print('I do not have bday info for ' + name)
		bday = input('What is their birthday? (dd mmm) ')
		bdays[name] = bday
		print('Birthday database updated.\n')
		printBday(bdays, 35, 7)
