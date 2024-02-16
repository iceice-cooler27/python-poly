#Coursemology
#Side Quest 4.2

#Name: Chia Wei En Wayne
#Date: 23 May 2023
#Status: Complete

#Input
t_a = float(input("Please enter the outside temperature in Fahrenheit: "))
v = float(input("Please enter the wind speed in miles per hour: "))

#Filter Process
if -58 <= t_a <= 41 and v > 2:
    t_wc = 35.74 + 0.6215*t_a - 35.75*(v**0.16) + 0.4275*t_a*(v**0.16)
    print("The wind-chill index is {:.2f}".format(t_wc))
else:
    print("Incorrect input")
