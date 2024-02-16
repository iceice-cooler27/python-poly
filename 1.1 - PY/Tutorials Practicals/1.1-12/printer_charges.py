#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def calculate_charge(num):
    if num <= 100:
        cost = num * 0.03
    elif num <= 300:
        cost = 100*0.03 + (num - 100)*0.02
    else:
        cost = 100*0.03 + 200*0.02 + (num - 300)*0.01
    return cost

def calculate_gst(cost):
    total = cost * 1.07
    return total

print("{:5}{:>13}{:>19}".format("Pages", "Charge($)", "Include GST($)"))
for n in range(500+1):
    if n % 50 == 0:
        charge = calculate_charge(n)
        total = calculate_gst(charge)
        print("{:<5}{:13.2f}{:19.2f}".format(n, charge, total))
