import re
def count_words(sentence):
    words = [
        re.sub("[^a-zA-Z0-9']", "", word).strip("'").lower() for word in re.split("[^a-zA-Z0-9']", sentence)
    ]
    words = [word for word in words if word != ""]
    return dict(zip(list(set(words)), [words.count(word) for word in set(words)]))
    
