import math

#Input
radius_cyl = float(input("Enter the radius of the cylinder (in m): "))
height_cyl = float(input("Enter the height of the cylinder (in m): "))

radius_sph = float(input("Enter the radius of the sphere (in m): "))

mass1 = float(input("Enter the mass of object 1 (in kg): "))
mass2 = float(input("Enter the mass of object 2 (in kg): "))
distance = float(input("Enter the distance between the objects (in m): "))
grav = 6.6743*(10**-11)

#Process
volume_cyl = math.pi*(radius_cyl**2)*height_cyl

area_sph = 4*math.pi*(radius_sph**2)

force = (grav * mass1 * mass2)/(distance**2)

#Display
print("Results:")
print("     Volume of the cylinder: {:.2f} cubic meters".format(volume_cyl))
print("     Surface area of the sphere: {:.2f} square meters".format(area_sph))
print("     Force of gravity between the objects: {:.2e} Newtons".format(force))
