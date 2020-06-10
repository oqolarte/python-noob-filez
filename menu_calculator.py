# Imagine you have started up a small restaurant and are trying to make it easier to calculate orders.
# Since your resto only sells 9 different items, you assign each one to a number: 

def printMenu(itemsDict, leftWidth, rightWidth): # prints the menu neatly
    print("TODAY'S MENU".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
def printOrder(itemsDict, leftWidth, rightWidth): # prints the order neatly
    print("YOUR ORDER".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
menuItems = {'Food':'(in Php)',
'(0) Glass of Water': 0, 
'(1) Chicken strips':175, 
'(2) French Fries':75, 
'(3) Hamburger':110, 
'(4) Hotdog':69,
'(5) Drink (L)':75,
'(6) Drink (M)':55,
'(7) Milk shake':115,
'(8) Eggplant Salad':69,
'(9) Cupcake':33}

printMenu(menuItems, 45, 7)

# To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order.

print("""\nTo place order, type in the numbers of meals you like.\n
Example: Type '235' to order one meal each of french fries, hamburger, and large drink.
Example: Type '922926' to order two cupcakes, three french fries, and a medium drink. \n""")

o1, o2, o3, o4, o5, o6, o7, o8, o9, o0 = 175, 75, 110, 69, 75, 55, 115, 69, 33, 0 # initializing values of order variables

while True:
	orderList = list(str(input("\nType in your order here (or 'q' to quit): ")))
	if orderList[0] == 'q':
		break
	else:
		sum = 0
		for i in orderList: # computing the sum
			if i == '1':
				sum += o1
			elif i == '2':
				sum += o2
			elif i == '3':
				sum += o3
			elif i == '4':
				sum += o4
			elif i == '5':
				sum += o5
			elif i == '6':
				sum += o6
			elif i == '7':
				sum += o7
			elif i == '8':
				sum += o8
			elif i == '9':
				sum += o9
				
		orderList.sort()
				
		for f, i in enumerate(orderList): # replacing user input with actual names of Food
			if i == '1':
				orderList[f] = 'Chicken Strips'
			elif i == '2':
				orderList[f]= 'French Fries'
			elif i == '3':
				orderList[f]= 'Hamburger'
			elif i == '4':
				orderList[f]= 'Hotdog'
			elif i == '5':
				orderList[f]= 'Drink (L)'
			elif i == '6':
				orderList[f]= 'Drink (M)'
			elif i == '7':
				orderList[f]= 'Milk shake'
			elif i == '8':
				orderList[f]= 'Eggplant Salad'
			elif i == '9':
				orderList[f]= 'Cupcake'
			elif i == '0':
				orderList[f]= 'Glass of Water'

		orderFinal = dict((i, orderList.count(i)) for i in orderList) #creates a counter of ordered food
		printOrder(orderFinal, 45, 7)
		print('\nTOTAL: Php', str(sum))
