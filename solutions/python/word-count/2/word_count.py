import re
from collections import Counter
def count_words(sentence):
    words = [
        re.sub("[^a-zA-Z0-9']", "", word).strip("'").lower() for word in re.split("[^a-zA-Z0-9']", sentence)
    ]
    words = [word for word in words if word != ""]
    return Counter(words)
    
