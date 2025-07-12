def to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary
def egg_count(display_value):
    return str(to_binary(display_value)).count('1')