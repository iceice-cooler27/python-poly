#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def print_square(side, char):
    for l in range(side):
        for b in range(side):
            print(char, end = " ")
        print()

#Input
character = input("Enter the character of the square: ")
length = int(input("Enter the length of the square: "))
print_square = print_square(length, character)
