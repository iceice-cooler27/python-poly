#Programming I

#####################################
#            Mission 2.2            #
#           Saving Calculator       #
#####################################

#Background
#==========
#Tom remembers the compound interest calculator that he did in Mission 1.
#Instead of calculating the compound interest of a given principal sum after
#x number of years, he would like to calculate the number of years needed to
#reach a certain final amount with an initial savings at a fixed interest rate.
#You may refer to the question in Coursemology for the formula

#Requirements
#============
#Write a Python program to get the input for the final amount and initial saving,
#calculate the number of years needed to reach the final amount. Assume that
#the annual interest rate is 5% and the interest is compounded monthly.
#Display the result as a smallest integer number that is just bigger than the
#result calculated. E.g. print 6, if it is bigger than 5 but less than 6.

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Do you need to import any module?
import math

#Input
principal = float(input("Please enter your inital principal amount: $"))
final = float(input("Please enter the final amount you want: $"))
rate = 0.05
n = 12

#Process
time = (math.log(final/principal)) / (n*math.log(1 + rate/n))
time = math.ceil(time)

#Output
print("The number of years needed to reach ${:.2f}, is at least {}.".format(final, time))
