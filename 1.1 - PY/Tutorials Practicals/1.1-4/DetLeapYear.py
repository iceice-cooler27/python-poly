#Done by: Chia Wei En Wayne
#ID: S10257584
#Date: 8 May 2023
#Checked

#Input
year = int(input("Please enter the year: "))

#Calculation
divis4 = year % 4
divis100 = year % 100
divis400 = year % 400

#Process
if (divis4 == 0 and divis100 != 0) or divis400 == 0:    #multiple of 400
    condition = " "
else:
    condition = " not "

#Display
print("{} is{}a leap year.".format(year, condition))
