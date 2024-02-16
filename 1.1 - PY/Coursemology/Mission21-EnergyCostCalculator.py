#Programming I

###############################
#       Mission 2.1           #
#    Energy Cost Calculator   #
###############################

#Background
#==========
#Ever wonder the energy cost of running an appliance or electronic device?
#Here is a simple calculation to get that figure.

#Step 1:
#Monthly electricity consumption =
#   (Power rating [Watts] of device * Number of hours used per day)/1000

#Step 2:
#Cost = Monthly electricity consumption * Electricity tariff
#                                         ($0.2743 as of April 2023 for SP group)

#Laptop computers may peak at a maximum draw of only 60 watts,
#whereas common desktops may peak around 175 watts.

#Requirements
#============
#1) Write pseudocode for the Energy Cost Calculator.
#   The solution should prompt user for the power rating of a device and the
#   number of hours used per day. After which, display the calculated cost in
#   4 decimal places.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - power_rating
#   - hours

#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Prompt user to input the value of the user's device's power rating in watts
#Get the value of the device's power rating in watts obtained, and assign value to variable power_rating
#Prompt user to input the number of hours the device is used for per day
#Get the value of the number of hours the device is used per day, and assign value to variable hours
#Calculate the monthly electricity consumption using the following formula:
#Monthly electricity consumption =
#   (Power rating [Watts] of device * Number of hours used per day)/1000
#Calculate the cost of the monthly electricity consumption using the following formula:
#Cost = Monthly electricity consumption * 0.2743
#                                         (assuming the electricity tariff is $0.2743)
#Display the calculated cost in dollars, in 4 decimal places

#TYPE YOUR PYTHON CODE BELOW
#===========================
#Input
power_rating = int(input("Enter your device's power rating in watts: "))
hours = float(input("Enter the number of hours your device is used for per day: "))

#Process
month_econsume = (power_rating * hours)/1000
ecost = month_econsume * 0.2743

#Output
print("Cost of your monthly electricity consumption is: ${:.4f}".format(ecost))

