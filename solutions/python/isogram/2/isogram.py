def is_isogram(string):
    string = string.lower()
    letters=[]
    for char in string:
        if char.isalpha():
            letters.append(char)
    return sorted(letters)==sorted(list(set(letters)))