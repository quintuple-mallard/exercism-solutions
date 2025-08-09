def find(search_list, value):
    if len(search_list) == 0 or (len(search_list) == 1 and search_list[0] != value):
        raise ValueError("value not in array")
    middle = len(search_list) // 2
    if search_list[middle] == value:
        return middle
    elif search_list[middle] > value:
        return find(search_list[:middle], value)
    else:
        return middle + find(search_list[middle:], value)