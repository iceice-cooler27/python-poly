#Done by: Chia Wei En Wayne
#Date: 8 May 2023
#Checked

#Input
import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)

input_sum = int(input("Enter the sum of {:d} and {:d}: ".format(num1, num2)))

#Process
correct_sum = num1 + num2

#Display
if input_sum == correct_sum:
    print("Your answer is correct!")
else:
    print("Your answer is wrong.")
    print("The correct answer is {:d}.".format(correct_sum))
