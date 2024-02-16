#Programming I

#########################
#      Mission 10.1     #
#   HDB Resale Prices   #   
#########################

#Background
#==========
#Tom is conducting some research into HDB resale prices as part of his part-time work for a real estate agency.
#Write a program to find out the following:
#
#a) The 2022 average price for the 4-room flat type (in 2 decimal places)
#b) The number of transactions above the average resale prices in part (a)
#c) The town with the highest resale price for the 5-room flat type in 2022
#
#Return the result of the three parts in a list of 3 items (e.g., [34535.35,20,'Hougang']

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   four_room_average, above_average, town_highest

#Set the filename
#Remove this statement when submitting in Coursemology

filename = "HDB-Resale-Price.csv"

#START CODING FROM HERE
#======================

#Create your function here
def ReadCSV(filename):
    file = open(filename, "r")
    hdb_file = file.read()
    hdb_file = hdb_file.split("\n")
    
    #Part a
    total = 0
    count = 0
    for i in hdb_file:
        i =  i.split(",")
        if "2022" in i[0] and "4-room" in i[2]:
            if i[3] != "-" and not(i[3].isalpha()):
                total += int(i[3])
                count += 1
    four_room_average = round(total/count, 2)
    highest = four_room_average
    above_average = 0
    #Part b
    for i in hdb_file:
        i = i.split(",")
        if "2022" in i[0] and "4-room" in i[2]:
            if i[3] != "-" and not(i[3].isalpha()):
                cost = int(i[3])
                if cost > four_room_average:
                    above_average += 1
    #Part c
    for i in hdb_file:
        i = i.split(",")
        if "2022" in i[0] and "5-room" in i[2]:
            if i[3] != "-" and not(i[3].isalpha()):
                cost = int(i[3])
                if cost > highest:
                    highest = cost
                    town_highest = i[1]
    return [four_room_average, above_average, town_highest]

    
#Statements to call the function, save result in variable result and print out
#to double-check your result returned from function
#Remove these statements when submitting in Coursemology
result = ReadCSV(filename)
print(result)

#output [566969.47, 29, 'QUEENSTOWN']




