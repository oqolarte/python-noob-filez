import pprint #a module that grants access to the  pprint() and pformat() functions that will "pretty print" a dictionary's values; a cleaner display of the items
message = str(input('Type any message here: \n'))
print('')
print('The count of each character in the\n\n', message, '\n\nis as follows:\n')
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)

