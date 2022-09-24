#!/usr/bin/python3
def multiple_returns(sentence):
    num = len(sentence)
    if (len(sentence) > 0):
        c = sentence[0]
    else:
        c = None
    my_tuple = (num, c)
    return(my_tuple)

