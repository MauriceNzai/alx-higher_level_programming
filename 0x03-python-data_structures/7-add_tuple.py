#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()

    if(len(tuple_a) < 2 and len(tuple_a) > 0):
        idx_0 = tuple_a[0] + tuple_b[0]
        idx_1 = tuple_b[1] + 0
        new_tuple = (idx_0, idx_1)
        return (new_tuple)
    elif (len(tuple_b) < 2 and len(tuple_b) > 0):
        idx_0 = tuple_a[0] + tuple_b[0]
        idx_1 = tuple_a[1] + 0
        new_tuple = (idx_0, idx_1)
        return (new_tuple)
    elif (len(tuple_a) < 1):
        idx_0 = tuple_b[0]
        idx_1 = tuple_b[1]
        new_tuple = (idx_0, idx_1)
        return (new_tuple)
    elif (len(tuple_b) < 1):
        idx_0 = tuple_a[0]
        idx_1 = tuple_a[1]
        new_tuple = (idx_0, idx_1)
        return (new_tuple)
    elif (len(tuple_a) > 2 or len(tuple_b) > 2 or 
            len(tuple_a) and len(tuple_b) == 2):
        idx_0 = tuple_a[0] + tuple_b[0]
        idx_1 = tuple_a[1] + tuple_b[1]
        new_tuple = (idx_0, idx_1)
        return (new_tuple)
