#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 25 June 2023
#Status: Completed

#Get Input
char = input("Enter a character: ")
num = int(input("Enter a number: "))

#Display
for level in range(num):
    start_pos = num - level - 1
    #print("start_pos {}".format(start_pos), end = " ")

    #Print the leading spaces
    for i in range(start_pos):
        print(" ", end = "")
        #print("{}".format(i), end = " ")

    #Print the symbols
    for i in range(level+1):
        print(char, end = " ")
    print()
print("Merry Christmas!")

#Display (Using Nested Loop)
"""
space = len(char)*num + num - 1
for r in range(num):
    fill = "{}".format(char)
    for c in range(r):
        fill += " {}".format(char)
    print("{:^{s}}".format(fill, s=space))
print("Merry Christmas!")
"""
#Not Using Nested Loop
"""
fill = "{}".format(char)
space = num*2 - 1
for r in range(num):
    if r != 0:
        fill += " {}".format(char)
    print("{:^{s}}".format(fill, s=space))
print("Merry Christmas!")   
"""

#print(fill.rjust(space))
