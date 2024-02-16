#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 31 May 2023
#Status: Completed

#Create List
name_list = ["Sharon", "Mic", "Josh", "Hannah", "Hanzel"]
height_list = [172, 166, 187, 200, 166]
weight_list = [59.5, 65.6, 49.8, 64.2, 47.5]
size_list = ["M", "L", "S", "M", "S"]
bmi_list =[]

#(a) Loop Display List
print("{:10}{:10}{:10}{:10}{}".format("Name", "Weight", "Height", "BMI", "Size"))
for count in range(5):
    bmi = weight_list[count] / (height_list[count]/100)**2
    bmi_list.append(bmi)
    print("{:10}{:<10}{:<10}{:<10.2f}{:10}".format(name_list[count], weight_list[count], \
                                             height_list[count], bmi_list[count], \
                                             size_list[count]))

#(b) Loop Predictive List and Display
predicted_list = []
accuracy = 0
print("\n{:10}{:10}{:10}{:10}".format("Name", "BMI", "Size", "Predicted"))
for count in range(5):
    if bmi_list[count] <= 18:
        size = "S"
    elif bmi_list[count] <= 21:
        size = "M"
    else:
        size = "L"
    predicted_list.append(size)
    if predicted_list[count] == size_list[count]:
        accuracy += 1
    print("{:10}{:<10.2f}{:10}{:10}".format(name_list[count], bmi_list[count], \
                                            size_list[count], predicted_list[count]))
rate = (accuracy/5)*100
print("Accuracy rate is {:.2f}".format(rate))

#(c) Combination of Lists
details_list = [["Sharon", "F", 33], ["Mic", "M", 24], \
                ["Josh", "M", 25], ["Hannah", "F", 30], \
                ["Hanzel", "M", 26]]

#Loop Extraction, Calculation and Display\
print("\n{:10}{:10}{:10}{:10}{:10}{:10}{:10}".format("Name", "Weight", "Height", "BMI", "Gender", "Age", "BMR"))
for count in range(5):
    gender = details_list[count][1]
    age = details_list[count][2]
    if gender == "M":
        bmr = 66.47 + (13.7*weight_list[count]) + (5*height_list[count]) - (6.8*age)
    else:
        bmr = 655.1 + (9.6*weight_list[count]) + (1.8*height_list[count]) - (4.7*age)
    print("{:10}{:<10.2f}{:<10}{:<10.2f}{:10}{:<10}{:<10.2f}".format(name_list[count], weight_list[count], \
                                                                     height_list[count], bmi_list[count], \
                                                                     gender, age, bmr))
    
