#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 12 August 2023
#Status: Additional 1: Incomplete

#GUI
#Adds onto Original Code with GUI interface
#Open File
datafile = open("carpark-information.csv", "r")
carpark_main_list = []

#Read Header, Store Seperate List
hline = datafile.readline()
hline = hline.strip("\n")
carpark_hlist = hline.split(",")

#Read File
for line in datafile:
    line = line.strip("\n")
    line = line.split(",",3)
    carpark_dict = {}
    for n in range(len(line)):
        carpark_dict[carpark_hlist[n]] = line[n] 
    carpark_main_list.append(carpark_dict)

#Close File
datafile.close()

from tkinter import *

def main_menu_option_GUI():
    option = optionIn.get()
    mainOut.delete("1.0", END)
    if option != "":
        try:
            error = ""
            option = int(option)
            assert 0 <= option <= 10
        except ValueError:
            error += "Value Error: Please Enter an Integer from [0] to [10]."
            mainOut.insert(END, error)
        except AssertionError:
            error += "Please enter an available option."
            mainOut.insert(END, error)
        #Filter Choice
        if option == 0:
            window.destroy()
        elif option == 1:
            option_1(carpark_main_list)
        elif option == 2:
            option_2(carpark_hlist, carpark_main_list)
        elif option == 3:
            lock = False
            lock = option_3(lock)
            if lock == False:
                carpark_ahlist, carpark_alist, atime = openfile3()
            #Check if user has completed Option 3 before continuing
            try:
                if option == 4:
                    option_4(carpark_alist)
                elif option == 5:
                    option_5(carpark_ahlist, carpark_alist)
                elif option == 6:
                    carpark_apdict = option_6(carpark_ahlist, carpark_alist)
                elif option == 7:
                    carpark_apdict = option_7(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist)
                elif option == 10:
                    option_10(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, atime)
                else:
                    #Check if user has completed Option 6/7 before continuing
                    try:
                        assert type(carpark_apdict) == dict
                        if option == 8:
                            option_8(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, carpark_apdict)
                        elif option == 9:
                            option_9(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, carpark_apdict)
                    except NameError:
                        error = "Name Error: Please select Option [6] or [7] first.\n"
                        mainOut.insert(END, error)
            except NameError:
                error = "Name Error: Please select Option [3] first.\n"
                mainOut.insert(END, error)
    else:
        menu = "MENU\n" + "{}\n".format("="*4)
        menu += "[1]  Display Total Number of Carparks in 'carpark-information.csv'\n"
        menu += "[2]  Display All Basement Carparks in 'carpark-information.csv'\n"
        menu += "[3]  Read Carpark Availability Data File\n"
        menu += "[4]  Print Total Number of Carparks in the File Read in [3]\n"
        menu += "[5]  Display Carparks Without Available Lots\n"
        menu += "[6]  Display Carparks With At Least x% Available Lots\n"
        menu += "[7]  Display Addresses of Carparks With At Least x% Available Lots\n"
        menu += "[8]  Display All Carparks at Given Location\n"
        menu += "[9]  Display Carpark with the Most Parking Lots\n"
        menu += "[10] Create an Output File with Carpark Availability with Addresses and Sort by Lots Available\n"
        menu += "[0]  Exit\n"
        mainOut.insert(END, menu)

def clear():
    mainOut.delete("1.0", END)

def option_1(dlist):
    result = "Option 1: Display Total Number of Carparks in 'carpark-information.csv'\n"
    mainOut.insert(END, result)
    #Finds Total Carparks in.csv file by counting the number of lines in file
    total = len(dlist)
    result = "Total Number of Carparks in 'carpark-information.csv': {}\n".format(total)
    mainOut.insert(END, result)

def option_2(hlist, dlist):
    result = "Option 2: Display All Basement Carparks in 'carpark-information.csv'\n"
    mainOut.insert(END, result)
    #Format Length + Spacings
    a = len(hlist[0]) + 2
    b = len(dlist[0][hlist[1]]) + 2
    result = "{:{a}}{:{b}}{}\n".format(hlist[0], hlist[1], hlist[3], a=a, b=b)
    mainOut.insert(END, result)
    count = 0
    #Extract Carparks With Basement
    for i in dlist:
        if "BASEMENT" in i[hlist[1]]:
            result = "{:{a}}{:{b}}{}\n".format(i[hlist[0]], i[hlist[1]], i[hlist[3]], a=a, b=b)
            mainOut.insert(END, result)
            #Every instance +1
            count += 1
    #Print Count of Basement Carparks
    result = "Total Number: {}\n".format(count)
    mainOut.insert(END, result)

def option_3(lock):
    result = "Option 3: Read Carpark Availability Data File\n"
    mainOut.insert(END, result)
    filename = mainIn.get()
    if filename != "":
        try:
            error = ""
            datafile = open(filename, "r")
        except FileNotFoundError:
            lock = True
            result = "File Not Found: Please enter the file's correct name.\n"
            mainOut.insert(END, result)
        return lock
    else:
        lock = True
        result = "Please enter the filename in the input."
        mainOut.insert(END, result)
        return lock

def openfile3():
    filename = mainIn.get()
    datafile = open(filename, "r")
    timestamp = datafile.readline()
    line = datafile.readline()
    line = line.strip("\n")
    ahlist = line.split(",")
    alist = []
    for line in datafile:
        line = line.strip("\n")
        line = line.split(",")
        c_dict = {}
        for n in range(len(line)):
            c_dict[ahlist[n]] = line[n]
        alist.append(c_dict)
    datafile.close()
    mainOut.insert(END, timestamp)
    return ahlist, alist, timestamp

def option_4(alist):
    result = "Option 4: Print Total Nuumber of Carparks in the File Read in [3]\n"
    total = len(alist)
    result += "Total Number of Carparks in the File: {}".format(total)
    mainOut.insert(END, result)

def option_5(ahlist, alist):
    result = "Option 5: Display Carparks Without Available Lots\n"
    count = 0
    for i in alist:
        if int(i[ahlist[2]]) == 0:
            result += "{}: {}\n".format(ahlist[0], i[ahlist[0]])
            count += 1
    result += "Total Number: {}".format(count)
    mainOut.insert(END, result)


#Create Main Window
window = Tk()
window.title("Main Option Selection Window")
window.geometry("1000x1000")

#Add Widgets
mainOut = Text(window, width=80, height=40)
optionL = Label(window, text="Option")
optionIn = Entry(window, fg="red", width=4)
mainL = Label(window, text="Input")
mainIn = Entry(window, fg="red", width=30)
optionB = Button(window, text="Display", width=10, command=main_menu_option_GUI)

#Placement of Widgets
optionL.place(x=20, y=20)
optionIn.place(x=100, y=20)
mainL.place(x=20, y=40)
mainIn.place(x=100, y=40)
optionB.place(x=20, y=80)
mainOut.place(x=120, y=120)

#Add Main Event Loop (To Handle User Events)
window.mainloop()
