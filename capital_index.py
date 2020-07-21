#Capital indexes
#Write a function named capital_indexes.
# The function takes a single parameter,
# which is a string. Your function should return a list
# of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(text):
   index_list = []
   item_list = []
   for index, item in enumerate(text):
       if item.isupper():
           index_list.append(index)
           item_list.append(item)
   print('The capitalized letters are: ', item_list)
   print('And their indices, respectively: ',index_list)

capital_indexes('sUpErcaLifrAgiListIceXpiAlijEjeMon') # Test Case
