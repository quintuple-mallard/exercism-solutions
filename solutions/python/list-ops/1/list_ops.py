def append(list1, list2):
    return list1+list2


def concat(lists):
    total_list=[]
    for list in lists:
        total_list=append(total_list, list)
    return total_list


def filter(function, list):
    valid=[]
    for item in list:
        if function(item):
            valid=append(valid,[item])
    return valid

def length(list):
    list_len=0
    for item in list:
        list_len+=1
    return list_len


def map(function, list):
    mapped=[]
    for item in list:
        mapped=append(mapped,[function(item)])
    return mapped


def foldl(function, list, initial):
    for item in list:
        initial=function(initial,item)
    return initial


def foldr(function, list, initial):
    for item in reverse(list):
        initial=function(initial,item)
    return initial


def reverse(list):
    return list[::-1]
