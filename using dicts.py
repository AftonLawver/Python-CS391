from pprint import pprint

stuff = {'Axe': 1, 'Gold coin': 20, 'Shield': 1}

def display_inventory(inventory:dict):
    print('Inventory: ')
    for k,v in inventory.items():
        print('{}: {}'.format(k,v))
    count = 0
    for i in inventory.values():
        count = count + i
    print('Total number of items: {}'.format(count))

def add_to_inventory(inventory:dict, items:list):
    for i in items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    display_inventory(inventory)

print('Inventory before: ')
display_inventory(stuff)

print('Inventory after:')
add_to_inventory(stuff, ['Gold coin', 'Gold coin', 'Dagger', 'Dagger'])