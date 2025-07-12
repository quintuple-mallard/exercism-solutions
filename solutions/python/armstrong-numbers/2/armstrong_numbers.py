def armstrong_sum(number):
    number=str(number)
    sum=0
    for digit in number:
        sum+=int(digit)**len(number)
    return sum
def is_armstrong_number(number):
    return armstrong_sum(number) == number
