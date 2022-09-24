#!/usr/bin/python3
def max_integer(my_list=[]):
    #step1. Initalize idx 0 as the largest
    max_int = my_list[0]
    #step2. iterate list and check each if > than max_int
    for num in my_list[1:]:
        if num > max_int:
            # assign num to max_int
            max_int = num
    #return max_int
    return (max_int)
