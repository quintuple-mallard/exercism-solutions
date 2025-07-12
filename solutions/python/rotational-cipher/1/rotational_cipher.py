def rotate(text, key):
    alphabet_lower="abcdefghijklmnopqrstuvwxyz"
    alphabet_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotated=""
    for char in text:
        if char.islower():
            rotated+=alphabet_lower[(alphabet_lower.index(char)+key)%26]
        elif char.isupper():
            rotated+=alphabet_upper[(alphabet_upper.index(char)+key)%26]
        else:
            rotated+=char
    return rotated