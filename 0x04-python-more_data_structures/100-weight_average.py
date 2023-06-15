#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum_weights = 0
        sum_total = 0

        for score, weight in my_list:
            sum_weights += weight
            sum_total += score * weight
        return(sum_total/sum_weights)
