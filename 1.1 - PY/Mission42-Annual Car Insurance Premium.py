#Coursemology
#Side Quest 4.2

#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Status: Incomplete

#Initial Display
print("Car Insurance Calculator")
print("="*24)

#Input
gender = input("Enter gender [M/F]: ")
age = int(input("Enter age: "))
traffic = input("Have you been in a traffic accident before? [Y/N] ")

#Calculation Process
if gender == "M":
    if age < 25:
        mplier = 1.8
    elif 25 <= age < 35:
        mplier = 1.5
    elif 35 <= age < 45:
        mplier = 1.2
    elif 45 <= age < 55:
        mplier = 1.0
    elif 55 <= age < 65:
        mplier = 1.4
    else:
        mplier = 1.7
else:
    if age < 25:
        mplier = 1.4
    elif 25 <= age < 35:
        mplier = 1.3
    elif 35 <= age < 45:
        mplier = 1.1
    elif 45 <= age < 55:
        mplier = 0.9
    elif 55 <= age < 65:
        mplier = 1.2
    else:
        mplier = 1.4
base = 800
if traffic == "Y":
    premium = 300
else:
    premium = 0
    
final = base*mplier + premium

#Display
print("Your annual premium is: {:.1f}".format(final))
