alength = float(input("Enter the length of a: "))
blength = float(input("Enter the length of b: "))

import math
clength = math.sqrt(alength**2 + blength**2)
print("The length of c is " + str(clength))

radius = clength / 2
areac = math.pi * radius**2
print("The area of the circle is " + str(areac))
