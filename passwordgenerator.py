import random

char = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
		'0','1','2','3','4','5','6','7','8','9',
		'!','@','#','$','%','^','&','*',] #total number of characters: 70

def pwGen(): #num is the number of characters the password has
	password = ''
	num = int(input('Enter the number of characters for your password: '))
	while True:
		password = password + char[random.randint(0,len(char) - 1)]
		if len(password) == num:
			break
	print('Here is the generated password: \n' + password)

pwGen()
