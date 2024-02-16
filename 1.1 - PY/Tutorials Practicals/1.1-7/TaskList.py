#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 29 May 2023
#Status: Completed, Checked

#Input
days = int(input("Enter number of days: "))

#Loop Display
for i in range(days):
    if i%7 == 0:    #Find the remainder of dividing with 7
        print("Day | Task(s)")
    print("{:3d} |".format(i+1))
