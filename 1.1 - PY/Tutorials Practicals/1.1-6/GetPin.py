#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 22 May 2023
#Status: Complete

#Set Pin
correct_pin = "123"
locked = True
no_try = 3

#Loop Tries
while locked and no_try > 0:
    input_pin = input("Enter pin: ")
    if input_pin != correct_pin:
        no_try -= 1
        if no_try == 0:
            print("Invalid pin. You have no more tries.")
            print("Your account is locked.")
        else:
            print("Invalid pin. Please try again.")
            print("You have {} tries left.".format(no_try))
    else:
        print("Correct pin entered.")
        locked = False
