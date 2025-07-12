def classify(number):
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors=[]
    for n in range(1,(number//2)+1):
        if not number%n:
            divisors.append(n)
    if sum(divisors)==number:
        return "perfect"
    elif sum(divisors)>number:
        return "abundant"
    return "deficient"