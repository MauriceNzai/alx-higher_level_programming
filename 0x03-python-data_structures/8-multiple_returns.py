#!/usr/bin/python3
def multiple_returns(sentence):
    num = len(sentence)
    if (len(sentence) == 0):
        c = None
    else:
        c = sentence[0]
    my_tuple = (num, c)
    return(my_tuple)

