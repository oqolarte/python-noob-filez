import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'blade': 10 }

def displayInventory(inventory): #inventory is a dictionary parameter containing 'stuff'
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(str(v)+ ' ' + k + '/s')
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
