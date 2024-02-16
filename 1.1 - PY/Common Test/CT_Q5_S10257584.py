#Chia Wei En Wayne (S10257584) - CSF02(P07)

#Input
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

#Checking for Errors
if num1 > num2:
    num1, num2 = num2, num1

skip_num = int(input("Enter a number between {} and {}: ".format(num1, num2)))
skip_count = 0

#Sort Possibily and Display
if skip_num < num1 or skip_num > num2:
    print("Invalid number entered")
else:
    for num_n in range(num1, num2 + 1):
        if num_n % skip_num == 0:
            print("{:>5}".format("skip"))
            skip_count += 1
        else:
            print("{:5}".format(num_n))
    print("{} integers skipped".format(skip_count))
