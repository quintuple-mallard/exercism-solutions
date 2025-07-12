def is_armstrong_number(number):
    number=str(number)
    armstrong_check=0
    for digit in number:
        armstrong_check+=int(digit)**len(number)
    if armstrong_check==int(number):
        return True
    return False
