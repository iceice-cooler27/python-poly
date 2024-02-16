#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def is_even(n):
    if n%2 == 0:
        even = True
    else:
        even = False
    return even
        
#Loop Extraction
num_list = [ 10, -13, 50, 5, 7, 24, 65, -40, 44, 30 ]
even_list = []

for i in num_list:
    even = is_even(i)
    if even == True:
        even_list.append(i)

#Display
print(even_list)
