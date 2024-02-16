#Chia Wei En Wayne (S10257584) - CSF02(P07)
#Status: Completed

item_list = [["Curry puff", 2.40, 2], \
             ["Apple tart", 2.00, 4], \
             ["Tuna puff", 2.20, 5], \
             ["Egg tart", 1.80, 1], \
             ["Custard tart", 1.50, 2]]
total_tart = 0
total_puff = 0

#Display + Loop Extraction
print("{:16}{:>11}{:>11}{:>11}".format("Iten Name", "Unit Price", \
                                    "Quantity", "Amount"))

for item in item_list:
    item_name = item[0]
    unit_price = item[1]
    quantity = item[2]
    amount = unit_price * quantity
    print("{:16}{:11.2f}{:11}{:11.2f}".format(item_name, unit_price, \
                                              quantity, amount))   
    if "tart" in item_name:
        total_tart += amount
    else:
        total_puff += amount

print("\nTotal cost of tarts: ${:.2f}".format(total_tart))
print("Total cost of puffs: ${:.2f}".format(total_puff))
