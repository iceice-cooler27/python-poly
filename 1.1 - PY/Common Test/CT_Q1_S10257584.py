#Chia Wei En Wayne (S10257584) - CSF02(P07)
#Status: Complete

require_var = input('Do you require toppings? [Yes/No]: ')
toppings_set_var = int(input('Portions of toppings required: '))
loyalty_var = input('Do you have the \'loyalty\' card? [Yes / No]: ')

total_cost = 2.5

if require_var.capitalize() == "Yes":
    total_cost = toppings_set_var * 1.2 + total_cost
    
if loyalty_var.capitalize() == "Yes":
    total_cost *= 0.9
    
print("Total cost: ${:.2f}".format(total_cost))

