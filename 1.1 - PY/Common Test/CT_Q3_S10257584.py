#Chia Wei En Wayne (S10257584) - CSF02(P07)
#Status: Completed, Checked

#Input
y_book = int(input("Please enter the number of books that are late: "))
x_day = int(input("Please enter the number of days the books are late: "))

#Calculation Fine
if y_book == 1:
    if x_day == 1:
        fine = 1.20
    else:
        fine = (2**(x_day-1)) * 0.3 + 1
else:
    if x_day == 1:
        fine = 0.15*y_book + 1.20
    else:
        fine = (2**x_day) * 0.15*y_book + 1.2

#Display
print("The fine for {} book(s) for {} day(s) is ${:.2f}".format(y_book, x_day, fine))
