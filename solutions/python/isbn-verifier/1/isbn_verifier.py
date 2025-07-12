def clean_isbn(raw_isbn):
    list_isbn = []
    for digit in raw_isbn:
        if digit != "-":
            list_isbn.append(digit)
    return list_isbn
def is_valid(isbn):
    multiplier = 10
    isbn_actual = clean_isbn(isbn)
    sum = 0
    
    if len(isbn_actual) != 10:
        return False
    
    for item in isbn_actual:
        if item == "X" and multiplier == 1:
            sum += 10 * multiplier
        elif item.isalpha() or (item == "X" and multiplier != 1):
            return False
        else:
            sum += int(item) * multiplier
        
        multiplier -= 1
    
    return sum % 11 == 0
