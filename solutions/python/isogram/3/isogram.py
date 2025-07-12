import re
def is_isogram(string):
    return len(set(re.sub('[^a-z]','',string.lower())))==len(re.sub('[^a-zA-Z]','',string))