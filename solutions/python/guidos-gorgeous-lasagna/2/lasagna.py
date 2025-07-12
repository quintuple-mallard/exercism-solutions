"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
MINS_PER_LAYER = 2
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(bake_time_elapsed):
    """Calculate the elapsed cooking time.""" 
    return EXPECTED_BAKE_TIME - bake_time_elapsed 



#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(layer_num):
    """Calculates the time to prepare n layers at 2 min per layer"""
    return layer_num * MINS_PER_LAYER

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layer_num, elapsed_bake_time):
    """Calculates the time elapsed making lasagna"""
    return elapsed_bake_time+preparation_time_in_minutes(layer_num)
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)