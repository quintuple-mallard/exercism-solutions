def convert(number):
    sound='Pling'*(not number%3)+'Plang'*(not number%5)+'Plong'*(not number%7)
    return sound or str(number)