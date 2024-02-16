#Q2
#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Group: CSF02
#Status: Complete, Checked

#Input
vehicle_no = input("Enter the vehicle number to be validated: ")
string = vehicle_no[1:]
reference_location = "AZYXUTSRPMLKJHGEDCB"

#Function
def calculateAlpha(letter):
    num_alpha = ord(letter) - ord("A") + 1
    return num_alpha

#Process (Alphabets)
letter = string[0]
letter_num1 = calculateAlpha(letter)

letter = string[1]
letter_num2 = calculateAlpha(letter)

#Check Validity
num3 = int(string[2])
num4 = int(string[3])
num5 = int(string[4])
num6 = int(string[5])
total = 9*letter_num1 + 4*letter_num2 + 5*num3+ 4*num4 + 3*num5 + 2*num6
position = total%19

if string[6] == reference_location[position]:
    response = "Valid"
else:
    response = "Invalid"

#Display Validity
print("Validity of the vehicle number: {}".format(response))
