#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 1 July 2023
#Status: Completed, Checked

#Function
def convert_temperature(c):
    f = (c*9/5) + 32
    return f

c = int(input("Enter the temperature in degree celsius: "))
t = convert_temperature(c)
print("The temperature is equivalent to {:.1f} fahrenheit.".format(t))
    
