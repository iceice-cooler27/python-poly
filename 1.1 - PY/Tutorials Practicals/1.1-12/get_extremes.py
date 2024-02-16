#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 1 July 2023
#Status: Completed, Checked

def get_extremes(nlist):
    """
    s = min(nlist)
    l = max(nlist)
    """
    s = num_list[0]
    l = num_list[0]
    for i in num_list:
        if i < s:
            s = i
        if i > l:
            l = i
    
    return s, l

import math
num_list = [ 10, -13, 50, 5, 7, 65, -40, 44, 30, math.inf, -math.inf ]
smallest, largest = get_extremes(num_list)
print(smallest)
print(largest)
