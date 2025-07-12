def is_flat(array):
    for item in array:
        if type(item) is list:
            return False
    return True
def flatten(iterable):
    while not is_flat(iterable):
        flattened=[]
        for item in iterable:
            if type(item) is list:
                flattened.extend(item)
            else :
                flattened.append(item)
        iterable=flattened
    flat_and_no_none=[]
    for item in iterable:
        if not (item is None):
            flat_and_no_none.append(item)
    return flat_and_no_none