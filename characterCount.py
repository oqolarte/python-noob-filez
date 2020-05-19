import pprint #a module that grants access to the  pprint() and pformat() functions that will "pretty print" a dictionary's values; a cleaner display of the items
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)

