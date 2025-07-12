def square(number):
    if number>64 or number<1:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)
    
def total():
    grains=0
    for i in range(64):
        grains+=2**(i)
    return int(grains)
