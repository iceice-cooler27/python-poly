#Done by: Chia Wei En Wayne
#Date: 4 May 2023

#Define inputs
alength = float(input("Enter the length of a: "))
blength = float(input("Enter the length of b: "))
import math
clength = math.sqrt(alength**2 + blength**2)

#areac = math.pi * radius**2
#Define function
def calculate_circle(alength, blength):
    #diameter = clength = math.sqrt(alength**2 + blength**2)
    radius = clength/2
    area = math.pi * (radius)**2
    return area

carea = calculate_circle(alength, blength)

#Display
print("The length of c is {}.".format(clength))
print("The area of the circle is {}.".format(carea))

