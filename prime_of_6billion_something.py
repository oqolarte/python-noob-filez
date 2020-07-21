#the prime factors of 13,195 are 5,7,13 and 29.
#what is the largest prime factor of the number 600,851,475,143 ?


num = 600851475143
for i in range(2, num+1):
	if num % i == 0:
		num = num // i
		print(i)
else:
	print(i)
print('\n***********************\n')

#8462696833 * 71
#10086647 * 839
#6857 * 1471
