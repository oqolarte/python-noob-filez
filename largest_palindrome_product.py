#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

# function which return reverse of a string 
def reverse(s): 
    return s[::-1]
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s)
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
    
for i in range(999, 100, -1):
	x = 0
	x_list = []
	for j in range(i-1, 100, -1):
		x = i * j
		palNum = isPalindrome(str(x))
		if palNum ==1:
			#x_list.append(x)
			print(x, i, j)
			break
