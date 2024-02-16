#Optional

#Name: Chia Wei En Wayne
#Student ID: Chia Wei En Wayne
#Date: 13 May 2023
#Checked

#Input
path = "C:\\1.1\\Text Files\\"
datafile = open(path + "data.txt", "r")

#Retrieve
data = datafile.readline()
data = data.split(",")

weight = float(data[0])
height = float(data[1])
gender = data[2]
age = int(data[3])

#Sort and Calculate
if gender == "Female":
    bmr = 10*weight + 6.25*height*100 - 5*age - 161
else:
    bmr = 10*weight + 6.25*height*100 - 5*age + 5

#Display
print("Weight: {}".format(weight))
print("Height: {:.1f}m".format(height))
print("Age: {}".format(age))
print("Gender: {}".format(gender))
print("BMR: {:.1f} kcal/day".format(bmr))
