#Enter a string and the program will reverse it and print it out.

def rev_string(string):
	reversed = ''
	for i in string:
		reversed = i + reversed #we call a function to reverse a string, which iterates to every element and intelligently join each character in the beginning so as to obtain the reversed string.
	print(reversed)
	

print(rev_string(str(input('Type a string and have its reverse printed out: '))))
