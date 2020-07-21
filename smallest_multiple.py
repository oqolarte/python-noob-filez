# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#least common multiple will be the product of multiplying the highest power of each prime number together.

def primes(n): #returns a dictionary of prime factors. key = prime factor, value = the number of instances
	primfac = [] #initializes a list to which prime factors will be appended
	d = 2
	while d*d <= n:
		while (n % d) == 0:
			primfac.append(d)  # supposing you want multiple factors repeated
			n //= d
		d += 1
	if n > 1:
		primfac.append(n)
		
	primDict = dict()
	for i in primfac:
		primDict[i] = primDict.get(i,0) + 1
	return primDict
	
def dict_compare(d1, d2):
	d1_keys = set(d1.keys())
	d2_keys = set(d2.keys())
	shared_keys = d1_keys.intersection(d2_keys)
	added = d1_keys - d2_keys
	modified = {o : d2[o] for o in shared_keys if d2[o] >= d1[o]}
	same = set(o for o in shared_keys if d1[o] == d2[o])
	return modified

x = {2:3, 3:1, 5:7, 7:1}
y = {2:2, 3:3, 5:2, 7:1}
modified = dict_compare(x, y)
print(modified)

# print(primes(int(input('Type an integer to get its prime factors: '))))

primeNums = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}
#primeCurrent = 

sum = 1
for k,v in primeNums.items():
	sum *= k**v
print(sum)
	
