#Optional
#Name: Chia Wei En Wayne
#Student ID: S10257584
#Date: 15 May 2023
#Status: Completed

#Read and Store
path = "C:\\1.1\\Text Files\\"
carsfile = open(path + "cars.txt", "r")

carsfile.readline()
carsfile.readline()

def readfile(carsfile):
    carmodel = carsfile.readline()
    carmodel = carmodel.strip()
    return carmodel

modelS = readfile(carsfile)
model3 = readfile(carsfile)
modelX = readfile(carsfile)
modelY = readfile(carsfile)

#Display
print("1. {}".format(modelS))
print("2. {}".format(model3))
print("3. {}".format(modelX))
print("4. {} \n".format(modelY))

#List
modelS = modelS.split(":")
model3 = model3.split(":")
modelX = modelX.split(":")
modelY = modelY.split(":")
car_list = [modelS[0], model3[0], modelX[0], modelY[0]]
price_list = [modelS[1], model3[1], modelX[1], modelY[1]]

#Input
order_no = input("Enter the order number: ")
order_name = input("Customer Name: ")
car_choice = int(input("Enter car choice: "))

#Selection and Extraction
if car_choice == 1:
    model = car_list[0]
    model = model[:13]
    price = price_list[0]
    price = price[1:]
elif car_choice == 2:
    model = car_list[1]
    model = model[:13]
    price = price_list[1]
    price = price[1:]
elif car_choice == 3:
    model = car_list[2]
    model = model[:13]
    price = price_list[2]
    price = price[1:]
elif car_choice == 4:
    model = car_list[3]
    model = model[:13]
    price = price_list[3]
    price = price[1:]
else:
    print("Entered car choice is invalid. Please ignore the following messages.")
print("Car has been successfully ordered.")

#Record Order in text file
order = order_no + ".txt"

path = "C:\\1.1\\Text Files\\"
orderfile = open(path + order, "w")
orderfile.write("{} ordered the {} at the price of {}".format(order_name, model, price))
orderfile.close()
