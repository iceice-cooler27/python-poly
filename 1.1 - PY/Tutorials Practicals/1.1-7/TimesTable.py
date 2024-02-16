#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 29 May 2023
#Status: Completed, Checked

#Input
multiplier = int(input("Please enter a number: "))

#Loop Display
for count in range(1, 11):
    value = multiplier * count
    print("{:>4d} x {:<2d} = {:<3d}".format(multiplier, count, value))

#End Display
print("The End")
