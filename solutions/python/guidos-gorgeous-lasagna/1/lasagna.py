"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(bake_time_elapsed):

    """Calculate the elapsed cooking time.

    """
    bake_time_remaining = EXPECTED_BAKE_TIME - bake_time_elapsed 
    return bake_time_remaining 



#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(layer_num):
    """
    docstring
    """
    preparation_time_in_minutes = layer_num * 2
    return preparation_time_in_minutes

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layer_num, elapsed_bake_time):
    """
    docstring
    """
    elapsed_time_in_minute = layer_num * 2 + elapsed_bake_time
    return elapsed_time_in_minute
    
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
