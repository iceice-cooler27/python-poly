#Programming I

#####################################
#            Mission 2.1            #
#           Coin Converter          #
#####################################

#Background
#==========
#Tom has 2 50-cent coins, 4 20-cent coins, 6 10-cent coins and 9 5-cent coins.
#He would like calculate the total amount in dollars.

#Requirements
#============
#Develop a pseudocode and Python program to solve the following problem:
#   -Given a number of 50-cent coins, 20-cent coins, 10-cent coins
#    and 5-cent coins, calculate the amount in dollars, print the
#    output with proper description and the amount in proper format

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of your program.
#2) You MUST (at least) use the following variables:
#   - cent50 (number of 50-cent coins)
#   - cent20 (number of 20-cent coins)
#   - cent10 (number of 10-cent coins)
#   - cent5  (number of 5-cent coins)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Get values of the number of 50-cent, 20-cent, 10-cent, 5-cent coins from Tom.
#Assign the values of the number of 50-cent, 20-cent, 10-cent, 5-cent coins to variables
#cent50, cent20, cent10, and cent5 respectively.
#Compute the amount of money Tom has in dollars using the following formula:
#amount = 0.50*Number 50-cent coins + 0.20*Number 20-cent coins +
#         0.10*Number 10-cent coins + 0.05*Number 5-cent coins
#Display the amount of money Tom has in dollars, with a breakdown of the amount each type of coin contributes to the value.

#TYPE YOUR PYTHON CODE BELOW
#===========================
#Input
cent50 = 2
cent20 = 4
cent10 = 6
cent5 = 9

#Process
amount50 = cent50*0.50
amount20 = cent20*0.20
amount10 = cent10*0.10
amount5 = cent5*0.05
amount = amount50 + amount20 + amount10 + amount5

#Output
print("Total amount in dolllars: ${:.2f}".format(amount))
print("Value of 50-cent coins: ${:.2f}".format(amount50))
print("Value of 20-cent coins: ${:.2f}".format(amount20))
print("Value of 10-cent coins: ${:.2f}".format(amount10))
print("Value of 5-cent coins: ${:.2f}".format(amount5))
