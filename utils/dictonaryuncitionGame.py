#!/usr/bin/env python3

def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	#Return key and value
	for k, v in inventory.items():
		print(str(v), k)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)