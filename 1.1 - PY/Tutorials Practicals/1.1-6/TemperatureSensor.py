#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 22 May 2023
#Status: Completed

#Open and Get File
path = "C:\\1.1\\Text Files\\"
temp_datafile = open(path + "temperature.txt", "r")
temp_data = temp_datafile.read()    #Read all content and Store in string
temp = temp_data.split(",")

#Display Process
total_data = len(temp)
total_temp = 0
count = 0

print("The temperatures are")
while count < total_data:
    temp_value = float(temp[count])
    if temp_value > 29:
        print("{:>6} ** higher than 29".format(temp_value))
    else:
        print("{:>6}".format(temp_value))
    total_temp += temp_value
    count += 1

#End of Loop, Final Display
average_temp = total_temp / total_data

print("Number of readings: {}".format(total_data))
print("Average temperature: {:.2f}".format(average_temp))
