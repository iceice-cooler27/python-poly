#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def find_even(n):
    if n%2 == 0:
        even = True
        print(n)
    else:
        even = False
    return even

"""
def find_even(n):
    if n%2 == 0:
        print(n)
"""

num_list = [ 10, -13, 50, 5, 7, 24, 65, -40, 44, 30 ]
even_list = []

#Display
for i in num_list:
    even = find_even(i)
    if even == True:
        even_list.append(i)
print(even_list)
    

