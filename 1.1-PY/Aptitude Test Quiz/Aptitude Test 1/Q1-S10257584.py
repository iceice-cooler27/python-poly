#Chia Wei En Wayne (S10257584G) - CSF02 (P07)
#Status: Complete, Checked

#Import math module
import math

#Input
height = float(input("Enter height of cylinder (in cm): "))
radius = float(input("Enter radius of base circle of cylinder (in cm): "))

#Calculation Process
total_area = 2*math.pi*(radius**2) + 2*math.pi*radius*height

#Display
print("\nTotal Surface Area is: {:.2f}cm squared".format(total_area))

"""
def calculateArea(height, radius):
    total_s_area = 2*math.pi*(radius**2) + 2*math.pi*radius*height
    return total_s_area
total_area = calculateArea(height, radius)
"""
