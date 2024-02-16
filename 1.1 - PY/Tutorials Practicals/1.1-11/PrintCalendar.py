#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 26 June 2023
#Status: Completed

#Get Input
num = int(input("Enter number of days: "))
day = input("When is the first day of the week: ")

#List
week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
date = 1

#Find Start
print()
for d in week:
    if d == day.capitalize():
        pos = week.index(d)
    print("{:>4}".format(d), end = "")
print()

#Display
while date <= num:
    for t in range(7):
        if date == 1 and t != pos:
            print("{:>4}".format(" "), end = "")
        else:
            print("{:>4}".format(date), end = "")
            date += 1
        if date > num:
            break
    print()
