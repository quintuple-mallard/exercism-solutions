def foldl(function, list, initial):
    for item in list:
        initial=function(initial,item)
    return initial
def largest_product(series, size):
    if len(series)<size:
        raise ValueError('span must not exceed string length')
    elif not series.isdigit():
        raise ValueError('digits input must only contain digits')
    elif size<0:
        raise ValueError('span must not be negative')
    substrings=[]
    for index,digit in enumerate(series): #main loop
        substrings.append(series[index:index+size])
    cleaned_substings=[]
    for substring in substrings: #cleaning up
        if len(substring)==size:
            cleaned_substings.append(substring)
    factors = [list(map(int,list(substring))) for substring in cleaned_substings]
    products = [foldl(lambda acc,item:acc*item, factor_list, 1) for factor_list in factors]
    return max(products)
    