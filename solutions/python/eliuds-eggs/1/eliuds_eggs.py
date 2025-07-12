def to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary
def egg_count(display_value):
    eggs=0
    egg_positions=to_binary(display_value)
    for item in egg_positions:
        if int(item):
            eggs+=1
    return eggs