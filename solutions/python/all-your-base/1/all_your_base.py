def to_base_ten(base, digits):
    number=0
    for i,digit in enumerate(reversed(digits)):
        number+=digit*(base**i)
    return number
def rebase(input_base, digits, output_base):
    if input_base<2:
        raise ValueError("input base must be >= 2")
    if not all(0<=digit<input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base<2:
        raise ValueError("output base must be >= 2")
    rebased=[]
    base_ten_num=to_base_ten(input_base,digits)
    while base_ten_num > 0:
        b = base_ten_num % output_base
        base_ten_num = base_ten_num - b
        base_ten_num = base_ten_num // output_base
        rebased.insert(0,b)
    return rebased or [0]
    