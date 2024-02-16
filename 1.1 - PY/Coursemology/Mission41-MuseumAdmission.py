#Programming I

###############################
#          Mission 4.1        #
#   Price of Museum Tickets   #
###############################

#Background
#==========
#Admission to Singapore museums is free for Singapore citizens (SC) and permanent residents (PR). 
#All others will have to pay $15 per entry.

#Write a Python program to calculate the price of tickets for a group of visitors consisting
#of SC, PR and others.

#The program is to prompt user for the total number visitors and the number of SCs and PRs.
#Calculate the total cost of the tickets and display this cost.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - total_no_visitors
#   - num_SC_PR
#   - total_cost
#   - num_others

#START CODING FROM HERE
#======================
#Calculate Ticket Cost
def calculate_cost(total_no_visitors, num_SC_PR):

    if total_no_visitors > num_SC_PR:                                                       #Check number of other visitors
        total_cost = (total_no_visitors - num_SC_PR) * 15                                   #Calculate total price of tickets
        print("The total cost of tickets visiting the museum is {}.".format(total_cost))    #Modify to display total price of tickets
    else:
        total_cost = 0                                                                      #calculate total price of tickets
        print("The total cost of tickets visiting the museum is free.".format(total_cost))  #Modify to display that Admission is free for all
        
    return total_cost #Do not remove this line that returns the result


#Prompt and accept data from user.
total_no_visitors = int(input("Enter the total number of visitors in the museum: "))
num_SC_PR = int(input("Enter the number of Singapore citizens and permanent residents among the visitors: "))
    
#Do not remove the next line that calls the function and store result return in total_cost
total_cost = calculate_cost(total_no_visitors, num_SC_PR) 
print("Tickets sold for {}.".format(total_cost))  #Modify to print the total cost of tickets

#input 75,50 output 375
#input 75,75 output 0
