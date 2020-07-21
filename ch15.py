catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
print('The cat names are:')
for name in catNames:
    print ('' + name)

print('Enter a pet name:')
petName = input()
if petName not in catNames:
    print('I do not have a pet named ' + petName + '!')
else:
    print(petName + ' is my pet.')