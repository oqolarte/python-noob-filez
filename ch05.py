while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print('Hello, ' + name + '. what is the password? (it is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')