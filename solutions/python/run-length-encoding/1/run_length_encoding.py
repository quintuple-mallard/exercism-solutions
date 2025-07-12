def decode(string):
    current_num=''
    decoded=''
    for item in string:
        if item.isdigit():
            current_num+=item
        else:
            decoded+=item*int(current_num if current_num.isdigit() else 1)
            current_num=''
    return decoded
def encode(string):
    if not string:
        return ''
    
    encoded = ''
    num_of_char = 1
    prev_item = string[0]
    for item in string[1:]:
        if item == prev_item:
            num_of_char += 1
        else:
            encoded += str(num_of_char if num_of_char != 1 else '') + prev_item
            prev_item = item
            num_of_char = 1
    encoded += str(num_of_char if num_of_char != 1 else '') + prev_item
    return encoded
