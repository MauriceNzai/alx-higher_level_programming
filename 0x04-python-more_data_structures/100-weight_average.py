#!/usr/bin/python3
def weight_average(my_list = []):
    if (my_list):
        scores = [score * weight for (score, weight) in my_list]
        return sum(scores) / sum([weight for (score, weight) in my_list])
    else:
        return (0)
