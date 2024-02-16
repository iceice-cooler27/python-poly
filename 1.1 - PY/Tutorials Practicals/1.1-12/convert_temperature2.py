#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def fahr_to_cel(fahr):
    cel = 5.0/9.0 * (fahr - 32)
    return cel

def cel_to_fahr(cel):
    fahr = 9.0/5.0 * cel + 32
    return fahr

online = True
while online:
    print("Temperature Conversion")
    print("[1] Fahrenheit to Celsius")
    print("[2] Celsius to Fahrenheit")
    print("[3] Exit")
    option = int(input("Please enter your option: "))
    if option == 1:
        in_temp = float(input("Please enter the temperature in Fahrenheit: "))
        out_temp = fahr_to_cel(in_temp)
        print("The temperature in celsius is {:.1f} degrees". format(out_temp))
    elif option == 2:
        in_temp = float(input("Please enter the temperature in Celsius: "))
        out_temp = cel_to_fahr(in_temp)
        print("The temperature in fahrenheit is {:.1f} degrees". format(out_temp))
    else:
        online = False
    print()
