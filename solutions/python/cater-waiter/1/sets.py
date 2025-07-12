"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    for item in drink_ingredients:
        if item in ALCOHOLS:
            return drink_name+' Cocktail'
    return drink_name+' Mocktail'

def categorize_dish(dish_name, dish_ingredients):
    for item in[VEGAN,VEGETARIAN,KETO,PALEO,OMNIVORE]:
        if dish_ingredients.issubset(item):
            return dish_name+': '+['VEGAN','VEGETARIAN','KETO','PALEO','OMNIVORE'][[VEGAN,VEGETARIAN,KETO,PALEO,OMNIVORE].index(item)]
    


def tag_special_ingredients(dish):
    return dish[0],SPECIAL_INGREDIENTS.intersection(dish[1])

def compile_ingredients(dishes):
    master_list = set()
    for dish in dishes:
        master_list=set(master_list.union(dish))
    return master_list


def separate_appetizers(dishes, appetizers):
    return list(set(dishes).difference(set(appetizers)))

def singleton_ingredients(dishes, intersection):
    singletons = (dish - intersection for dish in dishes)
    return set.union(*singletons)
        

    
