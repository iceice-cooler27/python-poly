#Programming I

#####################################
#            Mission 2.2            #
#           Triangle Calculator     #
#####################################

#Background
#==========
#Tom has learnt that if he knows the length of the 3 sides of a triangle,
#he is able to calculate the area by using the Heron's formula (please check
#it out in internet if you cannot remember the formula).

#Requirements
#============
#Write a Python program to calculate the perimeter and area of a triangle
#whose length of the 3 sides are entered by the user. Display the results
#in a nicely formatted string, like the following:
#    For a triangle with sides 3.0, 4.0 and 5.0
#    The perimeter is 12.00
#    The area is 6.00
#Note: values shown above are just examples

#TYPE YOUR PYTHON CODE BELOW
#===========================
#Do you need to import any module?
import math

#Input
lengtha = float(input("Please enter the length of the 1st side of the triangle: "))
lengthb = float(input("Please enter the length of the 2nd side of the triangle: "))
lengthc = float(input("Please enter the length of the 3rd side of the triangle: "))

#Process
perimeter = lengtha + lengthb + lengthc
semi_perimeter = perimeter/2
area = math.sqrt(semi_perimeter*(semi_perimeter - lengtha)*(semi_perimeter - lengthb)*(semi_perimeter - lengthc))

#Output
print("Given that the triangle has sides of lengths {:.2f}, {:.2f}, {:.2f} ;".format(lengtha, lengthb, lengthc))
print("Perimeter of the triangle is {:.2f} .".format(perimeter))
print("Area of the triangle is {:.2f} .".format(area))
