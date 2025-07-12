import re
VOWELS=['a','e','i','o','u']
def to_pig_latin(text):
    if text[0] in VOWELS or text.startswith('xr') or text.startswith('yt'):
        return text+'ay'
    qu_check=re.search('^[^qaeiou]*qu',text)
    if qu_check:
        return text[qu_check.span()[1]:]+text[qu_check.span()[0]:qu_check.span()[1]]+'ay'
    y_check=re.search('^[^yaeiou]+y',text)
    if y_check:
        return text[y_check.span()[1]-1:]+text[y_check.span()[0]:y_check.span()[1]-1]+'ay'
    consonant_span=re.search('[^aeiou]+',text).span()
    return text[consonant_span[1]:]+text[consonant_span[0]:consonant_span[1]]+'ay'
def translate(text):
    if isinstance(text.split(), list):
        return ' '.join([to_pig_latin(word) for word in text.split()])
    return to_pig_latin(text)
    