bdays = {'Isya':'16 June', 'Mads':'9 Jan', 'Charles':'3 Nov'}
while True:
    name = input('Enter a name (blank to quit): ')
    if name == '':
        break
    if name in bdays:
        print(bdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have bday info for ' + name)
        bday = input('What is their birthday? ')
        bdays[name] = bday
        print('Birthday database updated.')
