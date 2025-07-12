def is_isogram(string):
    string = string.lower()
    letters=[]
    for char in string:
        if char.isalpha():
            if char in letters:
                return False
            letters.append(char)
    return True
