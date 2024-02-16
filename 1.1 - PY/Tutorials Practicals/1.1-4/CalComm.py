#Done by: Chia Wei En Wayne
#Date: 8 May 2023
#Checked

#Input
mthly_sale = float(input("Enter monthly sales of sales agent: "))

#Process
if mthly_sale >= 10000:
    comm_rate = 10
else:
    comm_rate = 5

#Calculation of commission paid
comm_paid = (comm_rate/100) * mthly_sale

#Display
print("The commission rate is : {}%".format(comm_rate))
print("The commission paid is : ${:.2f}".format(comm_paid))
