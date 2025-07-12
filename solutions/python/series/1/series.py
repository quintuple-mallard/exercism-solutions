def slices(series, length):
    if length==0:
        raise ValueError('slice length cannot be zero')
    elif length<0:
        raise ValueError('slice length cannot be negative')
    elif series=='':
        raise ValueError('series cannot be empty')
    elif length>len(series):
        raise ValueError('slice length cannot be greater than series length')
    substrings=[]
    for index,digit in enumerate(series): #main loop
        substrings.append(series[index:index+length])
    cleaned_substings=[]
    for substring in substrings: #cleaning up
        if len(substring)==length:
            cleaned_substings.append(substring)
    return cleaned_substings