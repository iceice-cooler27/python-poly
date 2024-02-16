#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 29 May 2023
#Status: Completed, Checked

oddlist = []
evenlist = []
total = 0

while True:
    number = int(input("Please enter a number (0 to end): "))
    if number == 0:
        break
    if number % 2 != 0:
        oddlist.append(number)  #Extraction
    else:
        evenlist.append(number)
    total += number

#Sort and Display
oddlist.sort()
evenlist.sort()
#You can use for loop to extract the items and add it to the total

if len(oddlist) + len(evenlist) > 0:
    print("Odd numbers: {}".format(oddlist))
    print("Even numbers: {}".format(evenlist))
    print("Average = {:.2f}".format(total / (len(oddlist) + len(evenlist))))
