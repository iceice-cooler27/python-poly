#Programming I

################################
#      Mission 3.2             #
#   Convert Binary to Decimal  #
################################

#Background
#==========
#A binary value can be converted to a decimal value by taking the sum of each 
#binary digit times their power of 2 (you may refer to the steps and example
#given in Coursemology.

#Write a Python program to convert a 4-digit binary value to a decimal value.


#Important Notes
#===============
#1) You are required to include a function called binaryToDecimal(), which
#   accepts a string of 4-digit binary value, converts it to decimal value
#   and returns the result
#2) When testing the program in IDLE, you should prompt the user for the input
#   value. However, you must comment out the input prompt before submitting it
#   in coursemology


#START CODING FROM HERE
#======================
#Prompt and obtain input of a 4-digit binary value and assign it to binary_value
#Note: Do not change the input to int type.


#Do not edit/remove the next line
def binaryToDecimal(binary_value):
    #Set values for conversion
    binary_value = binary_value[::-1]
    position = 0
    
    #Code to do the conversion
    currentdigit = int(binary_value[0])
    value0 = currentdigit * (2 ** position)

    position = position + 1
    currentdigit = int(binary_value[1])
    value1 = currentdigit * (2 ** position)
    
    position = position + 1
    currentdigit = int(binary_value[2])
    value2 = currentdigit * (2 ** position)

    position = position + 1
    currentdigit = int(binary_value[3])
    value3 = currentdigit * (2 ** position)

    decimal_value = value0 + value1 + value2 + value3
    print(value0)
    print(value1)
    print(value2)
    print(value3)
    #Return the result
    return decimal_value #Do not remove this line

#Prompt for a 4-digit binary value (do not convert it to int type) and assign it
#to binary_value. You must remove this statement when submitting in Coursemology
#binary_value = str(input("Enter the 4-digit binary value: "))

#Do not edit/remove the next line that calls the function 
decimal_value = binaryToDecimal(binary_value)

#Modify the statement to display the decimal value
print("The decimal value of the 4-digit binary value is {}.".format(decimal_value))

#input '1011' output 11
#input '1100' output 12
