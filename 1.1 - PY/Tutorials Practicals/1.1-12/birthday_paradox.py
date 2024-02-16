#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

#Start
print("This program demonstrates the birthday paradox.")

import random
date_list = []
duplicate = False

def check_date(duplicate):
    date = random.randint(1,365)
    print("{} was randomly generated.".format(date))
    if date in date_list:
        duplicate = True
    date_list.append(date)
    no_try = len(date_list)
    return duplicate, no_try

while not(duplicate):
    duplicate, n = check_date(duplicate)

print("Duplicate day! This took {} tries.".format(n))
    
