#Programming I

#######################################
#            Mission 3.2              #
#   Calculate Daily Total Energy Cost #
#######################################

#Background
#==========
#The total energy cost is calculated using this formula: 
#   Total Energy Cost ($) = Total Energy consumed (kW) x Electricity tariff
#Note: Electricity tariff is $0.2743 as of April 2023 for SP group

#Write a Python program that calculates and displays the total energy cost
#based on the input of usage for various appliances and their Power rating
#entered by user and the displays a table of energy in watts/hour
#for various appliances and prompt user to enter the daily hours for
#each appliance. The program then displays the table again with the
#daily hours and calculated value of the total daily energy cost.


#Important Notes
#===============
#1) You are required to include a function called calculateEnergyCost(), which
#   accepts a list (appliance_list, which contains a list of appliances' names
#   together with their energy in watts per hour) and a string (hrs_input, which
#   contains the daily hours used for each appliances, separated in ';'),
#   calculates total daily energy cost and returns the result
#2) When testing the program in IDLE, you should prompt the user for the input
#   value. However, you must comment out the input prompt before submitting it
#   in coursemology


#START CODING FROM HERE
#======================
#Perform Calculation of Total Daily Energy Cost
def calculateEnergyCost(appliance_list,hrs_input):
    tariff = 0.2743 #define tariff
    
    #Code to parse the input string in hrs_input (Hint: Use the split() function)
    hr_list = hrs_input.split(";")

    #Display list of appliances and daily hours used
    print("{:18} {:16} {:14}".format("Name", "Energy(Watts/Hr)", "Daily Hrs used"))
    print("{:18} {:<16d} {:<14}".format(appliance_list[0][0], appliance_list[0][1], hr_list[0]))
    print("{:18} {:<16d} {:<14}".format(appliance_list[1][0], appliance_list[1][1], hr_list[1]))
    print("{:18} {:<16d} {:<14}\n".format(appliance_list[2][0], appliance_list[2][1], hr_list[2]))
    
    #Calculate total energy of all appliances    
    total_energy = (appliance_list[0][1]*int(hr_list[0]) + appliance_list[1][1]*int(hr_list[1]) + appliance_list[2][1]*int(hr_list[2])) / 1000
    
    #Calculate total daily energy cost
    total_energy_cost = total_energy * tariff
    
    #Display daily energy consumption and total daily energy cost    
    print("Total daily energy consumed (kW): {:.2f}".format(total_energy)) 
    print("Total daily energy cost ($): {:.2f}".format(total_energy_cost)) 

    #Return the total daily energy cost 
    return total_energy_cost #Do not remove/edit this line

#Create a list named appliance_list with the 3 appliances shown in the
#screenshot in Coursemology
appliance_list = [["Electric Fan",70], ["Air Con",1200], ["Refrigerator",200]]

#Display the list of appliances with energy in watts/hr
print("List of Electrical Appliances with Energy in Watts/Hr:")
print("{:18} {:16}".format("Name", "Energy(Watts/Hr)"))
print("{:18} {:<16d}".format(appliance_list[0][0], appliance_list[0][1]))
print("{:18} {:<16d}".format(appliance_list[1][0], appliance_list[1][1]))
print("{:18} {:<16d}\n".format(appliance_list[2][0], appliance_list[2][1]))

#Prompt and obtain input for daily consumption for appliances
hrs_input = input("Enter daily hours used for the above appliances separated by ';' : ")
    
#Do not remove the next line that calls the function
total_energy_cost = calculateEnergyCost(appliance_list,hrs_input)

#Modify the statement to display the decimal value
print("Total daily energy cost ($): {}".format(round(total_energy_cost,2)))

#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'5;4;24'
#output 2.73
#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'8;8;24'
#output 4.10
