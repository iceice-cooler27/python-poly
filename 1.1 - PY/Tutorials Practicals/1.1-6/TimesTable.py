#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 22 May 2023
#Status: Completed

#Input
multiplier = int(input("Please enter a number: "))
count = 1

#Loop Display
while count <= 10:
    value = multiplier * count
    print("{:>4} x {:<2} = {:<3}".format(multiplier, count, value))
    count += 1
print("The End")
