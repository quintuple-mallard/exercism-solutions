def abbreviate(words):
    words=words.replace("'",'')
    words=words.title()
    acronym=''
    for char in words:
        if char.isupper():
            acronym+=char
    return acronym