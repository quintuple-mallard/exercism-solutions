def convert(number):
    sounds=""
    if not number%3:
        sounds+="Pling"
    if not number%5:
        sounds+="Plang"
    if not number%7:
        sounds+="Plong"
    if sounds:
        return sounds
    return str(number)