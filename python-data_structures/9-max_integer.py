#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for number in my_list[1:]:
        if number > max_value:
            max_value = number
    return max_value
