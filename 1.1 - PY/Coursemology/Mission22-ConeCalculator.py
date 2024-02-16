#Programming I

#####################################
#            Mission 2.2            #
#           Cone Calculator         #
#####################################

#Background
#==========
#Tom has learnt that if he knows the radius of the base circle and height
#of a right circular cone, he is able to calculate the volume and the surface
#area of the cone (refer to the question in Coursemology for the formulae)

#Requirements
#============
#Write a Python program to calculate the volume and surface area (including
#the base circle) of a right circular cone whose base circle radius and heeight
#are entered by the user. Display the results in a nicely formatted string,
#like the following:
#    For a cone with base circle radius 3.0 and height 4.0:
#    Slant height is 5.00
#    Volume is 37.6991
#    Surface area (including base circle) is 75.3982
#Note: values shown above are just examples

#TYPE YOUR PYTHON CODE BELOW
#===========================
#Do you need to import any module?
import math

#Input
radius = float(input("Please enter the radius of the base circle of the cone: "))
height = float(input("Please enter the height of the cone: "))

#Process
slant_h = math.sqrt(radius**2 + height**2)

volume = 1/3 * math.pi * (radius**2) * height

area = math.pi*(radius**2) + math.pi * radius* slant_h

#Output
print("Given that the cone has a base circle radius {:.2f} and height {:.2f}:".format(radius, height))
print("Slant height is {:.2f}".format(slant_h))
print("Volume is {:.4f}".format(volume))
print("Surface area (including base circle) is {:.4f}".format(area))
