def multiples_of_n(n,limit):
    if n==0:
        return ()
    multiples=tuple()
    for i in range(1,limit):
        if i%n==0:
            multiples=multiples+(i,)
    return multiples
def sum_of_multiples(limit, multiples):
    all_multiples=[]
    for multiple in multiples:
        if multiples_of_n(multiple,limit):
            all_multiples.extend(multiples_of_n(multiple,limit))
    return sum(set(all_multiples))
    
