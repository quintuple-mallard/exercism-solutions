"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add: 
        if item in current_cart:
            current_cart[item]+=1
        else:
            current_cart[item]=1
    return current_cart
        


def read_notes(notes):
    return dict.fromkeys(notes,1)

def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    new_cart={}
    for item in cart.keys():
        new_cart[item]=[cart[item],aisle_mapping[item][0],aisle_mapping[item][1]]
    return dict(sorted(new_cart.items(), reverse=True))

def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart.keys():
        store_inventory[item][0]-=fulfillment_cart[item][0]
        if store_inventory[item][0]<=0:
            store_inventory[item][0]='Out of Stock'
    return store_inventory