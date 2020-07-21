#Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”


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
  
  
# Driver code 
s = str(input('Enter a string to check whether it is palindrome: '))
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes, it's palindrome.") 
else: 
    print("No, it's not a palindrome") 

