def PermutationStep(num):
  temp = str(num)
  for i in range(len(temp)-1, 0, -1):
    if temp[i] > temp[i-1]:
      return temp[:i-1] + temp[i] + "".join(sorted(temp[i-1]+temp[i+1:]))
  return -1

num = input('Type any integer and the program shall return the next highest value using the same digits: ')
print(PermutationStep(num))
