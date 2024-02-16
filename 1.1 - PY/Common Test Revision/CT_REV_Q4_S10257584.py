#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 31 May 2023
#Status: Completed

#Input
number = int(input("Enter a number between 0 and 5000: "))
n = 1
correct = False

#Formula
while not(correct):
    Tn = ((n**2)+n)/2
    if Tn > 5000:
        print("{} is NOT a triangular number.".format(number))
        correct = True
    elif number == Tn:
        if n != 11 and str(n)[-1] == "1":
            post = str(n) + "st"
        elif n != 12 and str(n)[-1] == "2":
            post = str(n) + "nd"
        elif n != 13 and str(n)[-1] == "3":
            post = str(n) + "rd"
        else:
            post = str(n) + "th"
        print("{} is a triangular number and it is the {} number.".format(number, post))
        correct = True
    else:
        n += 1
