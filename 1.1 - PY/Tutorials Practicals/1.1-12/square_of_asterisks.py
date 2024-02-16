#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def print_square(side):
    for l in range(side):
        for b in range(side):
            print("*", end = " ")
        print()

#Input
length = int(input("Enter the length of the square: "))
print_square = print_square(length)
