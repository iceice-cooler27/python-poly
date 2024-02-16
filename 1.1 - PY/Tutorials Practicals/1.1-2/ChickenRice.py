import math

#Input
price_cr = float(input("Enter the price of chicken rice: "))
no_side = int(input("Enter the number of side dishes: "))

#Process
total_cost = (price_cr + 1.20*no_side)*1.08
total_cost = round(total_cost, 1)

#Display
print("Total cost of the purchase is ${:.2f}".format(total_cost))
