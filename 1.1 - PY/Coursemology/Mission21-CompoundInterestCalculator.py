#Programming I

#####################################
#            Mission 2.1            #
#    Compound Interest Calculator   #
#####################################

#Background
#==========
#Tom won a lottery amounting to $10000, and he is deciding if he should
#deposit it into a bank account to accumulate interest.

#Tom wishes to find out how much he will have in the bank account after
#a specified number of years, given his input.

#Requirements
#============
#1) Write pseudocode that sets the principal amount of $10000 to variable P,
#   annual nominal interest rate of 8% to variable r, number of times the
#   interest is compounded per year of 12 to variable n. The number of years
#   that the money will be compounded, t, is given by the user. Calculate
#   and print the final amount (up to 3 decimal places) after t years.
#   Note: Refer to the question in Coursemology for the formula.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - P (principal amount)
#   - r (annual nominal interest rate [as a decimal])
#   - n (number of times the interest is compounded per year)
#   - t (number of years)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Assign the value of the principal amount, 10000, to variable P
#Assign the value of the annual interest rate, 0.08, to variable r
#Assign the value of the number of times interest is compounded per year, 12, to variable n
#Prompt user to input the number of years the money will be compounded.
#   Assign that value to t
#Compute the total compounded amount of money at the end using the following formula:
#Final amount = Principal amount * (1 + Interest rate/Number of times compounded per year)**(Number of times compounded per year*Number of years compounded)
#Display the final amount earned with compound interest in dollars, up to 3 decimal places.

#TYPE YOUR PYTHON CODE BELOW
#===========================
#Input
P = 10000.00
r = 0.08
n = 12
t = float(input("Enter the number of years the money will be compounded: "))

#Process
comp_amount = P * (1 + r/n)**(n*t)

#Output
print("Final amount after {} years: {:.3f}".format(t, comp_amount))
