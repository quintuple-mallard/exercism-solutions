"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
MINS_PER_LAYER = 2

def bake_time_remaining(bake_time_elapsed):
    """Calculate the elapsed cooking time.""" 
    return EXPECTED_BAKE_TIME - bake_time_elapsed 



def preparation_time_in_minutes(layer_num):
    """Calculates the time to prepare n layers at 2 min per layer"""
    return layer_num * MINS_PER_LAYER

def elapsed_time_in_minutes(layer_num, elapsed_bake_time):
    """Calculates the time elapsed making lasagna"""
    return elapsed_bake_time+preparation_time_in_minutes(layer_num)