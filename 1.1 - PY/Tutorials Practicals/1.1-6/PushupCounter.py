#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 22 May 2023
#Status: Completed

#Initial Input
target_pu = int(input("Enter target number of pushups: "))
total_pu = 0
day_no = 0

#Loop Input
while total_pu < target_pu:
    day_no += 1
    day_pu = int(input("Day {}: How many pushups did you do today? ".format(day_no)))
    total_pu += day_pu

#End of Loop
print("You did a total of {} pushups.".format(total_pu))
print("You hit your target in {} days!".format(day_no))
