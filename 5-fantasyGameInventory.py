# Fantasy Game Inventory


def displayInventory(inventory):
    # displays number of each item in inventory, plus total number of items
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # adds items from item list into inventory dictionary
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
displayInventory(stuff)  # before loot
stuff = addToInventory(stuff, dragonLoot)  # add loot items to inventory
displayInventory(stuff)  # after loot
