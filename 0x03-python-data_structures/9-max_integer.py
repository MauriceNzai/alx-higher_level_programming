#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (None)

    #step1. Initalize idx 0 as the largest
    max_int = my_list[0]
    #step2. iterate list and check each if > than max_int
    for num in range(1, len(my_list)):
        if my_list[num] > max_int:
            # assign num to max_int
            max_int = my_list[num]
    #return max_int
    return (max_int)
