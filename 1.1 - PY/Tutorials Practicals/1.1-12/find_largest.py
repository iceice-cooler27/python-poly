#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 1 July 2023
#Status: Completed, Checked

def find_larger(n1, n2):
    if n1 > n2:
        n = n1
    else:
        n = n2
    return  n
    
#Input
no1 = int(input("Enter the first integer number: "))
no2 = int(input("Enter the second integer number: "))
no3 = int(input("Enter the third integer number: "))
no4 = int(input("Enter the fourth integer number: "))

num1 = find_larger(no1, no2)
num2 = find_larger(no3, no4)
num = find_larger(num1, num2)

#Display
print("The largest integer is {}".format(num))
