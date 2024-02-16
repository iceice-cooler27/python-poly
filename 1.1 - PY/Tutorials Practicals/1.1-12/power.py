#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Check

def power(x, n):
    num = 1
    if n >= 0:
        for i in range(n):
            num = num * x
    else:
        num = x**n
    return num

#Input
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
num = power(base, exponent)
print(int(num))
