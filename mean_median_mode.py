# In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically, the median is the number in the middle.
# Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.


def mean_funct(numList, d): # numList is a list of integers; d is number of decimal places
	sum = 0
	for i in numList:
		sum += float(i)
	return round(sum/len(numList), d)
	

def median_func(numList):
	numList.sort()
	if len(x) % 2 == 0:
		return (numList[int(len(x)/2)], numList[int(len(x)/2) + 1])
	else:
		return numList[int((len(x)-1)/2) + 1]
	
def mode_func(numList):
	return max(set(numList), key=numList.count)


print("This program gives mean, median, and mode of a set of integers.\n")	

# sample list only:
# x = [1,2,3,4,5,7,8,9,8,7,89,6,4,5,6,43,1,2,3,4,5,65,7,69,56,21,323,4,56,69,69,69,69,69,69,12,3,5,6,7,8,9,10]

x = []
while True:
	data = input('Input integer, or enter blank to end: ')
	if data == '':
		break
	else:
		x.append(int(data))
	print('Current number of data in the array is', len(x), ' \n')

print('Here is the array: ', x)
print("Length of the list is",len(x), ' \n')


# d = int(input('How many decimal places for mean? '))
print("mean : ", mean_funct(x, int(len(x))))
print("median: ", median_func(x))
print("mode : ", mode_func(x))
