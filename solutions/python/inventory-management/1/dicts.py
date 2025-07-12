"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory={}
    for item in items:
        if not item in inventory:
            inventory.update({item:1})
        else:
            inventory[item]+=1
    return inventory


def add_items(inventory, items):
    for item in items:
        if not item in inventory:
            inventory.update({item:1})
        else:
            inventory[item]+=1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if not item in inventory :
            "code"
        elif inventory[item]==0 :
            "more code"
        else:
            inventory[item]=inventory[item]-1
    return inventory


def remove_item(inventory, item):
    if item in inventory.keys():
        inventory.pop(item)
        return inventory
    return inventory
def list_inventory(inventory):
    listed=[]
    for item in inventory:
        if inventory[item]>=1:
            listed.append((item, inventory[item]))
    return listed