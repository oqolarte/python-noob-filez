def displayInventory(inventory): #inventory is a dictionary parameter containing the player's inventory
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ' ' + k + '/s')
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems): #addedItems is a list parameter containing the loot from the slain enemy
    for i in addedItems:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby','ruby','ruby','ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
