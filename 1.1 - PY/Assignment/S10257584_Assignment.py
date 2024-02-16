#Name: Chia Wei En Wayne
#Class: P07
#ID: S10257584
#Date: 28 July 2023
#Status: Basic: Completed, Adavanced: Completed

#Display Menu
def readfile():
    #Open File
    datafile = open("carpark-information.csv", "r")
    mlist = []

    #Read Header, Store Seperate List
    hline = datafile.readline()
    hline = hline.strip("\n")
    hlist = hline.split(",")

    #Read File
    for line in datafile:
        line = line.strip("\n")
        line = line.split(",",3)
        cdict = {}
        for n in range(len(line)):
            cdict[hlist[n]] = line[n] 
        mlist.append(cdict)

    #Close File
    datafile.close()
    return hlist, mlist

def main_menu_option():
    #Prints Options Menu
    print("MENU \n" + "="*4)
    print("[1]  Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2]  Display All Basement Carparks in 'carpark-information.csv'")
    print("[3]  Read Carpark Availability Data File")
    print("[4]  Print Total Number of Carparks in the File Read in [3]")
    print("[5]  Display Carparks Without Available Lots")
    print("[6]  Display Carparks With At Least x% Available Lots")
    print("[7]  Display Addresses of Carparks With At Least x% Available Lots")
    print("[8]  Display All Carparks at Given Location")
    print("[9]  Display Carpark with the Most Parking Lots")
    print("[10] Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
    print("[0]  Exit")
    #Check for correct input. User must input correct value to continue
    while True:
        try:
            option_no = int(input("Enter your option: "))
            assert option_no <= 10 and option_no >= 0
            break
        except ValueError:
            print("Value Error: Please enter an integer from [0] to [10].\n")
        except AssertionError:
            print("Input Error: Please enter a number from [0] to [10].\n")
    print()
    #Return value to find the option that matches
    return option_no

def option_1(dlist):
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
    #Finds Total Carparks in.csv file by counting the number of lines in file
    total = len(dlist)
    print("Total Number of Carparks in 'carpark-information.csv': {}\n".format(total))

def option_2(hlist, dlist):
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    #Format Length + Spacings
    a = len(hlist[0]) + 2
    b = len(dlist[0][hlist[1]]) + 2
    print("{:{a}}{:{b}}{}".format(hlist[0], hlist[1], hlist[3], a=a, b=b))
    count = 0
    #Extract Carparks With Basement
    for i in dlist:
        if "BASEMENT" in i[hlist[1]]:
            print("{:{a}}{:{b}}{}".format(i[hlist[0]], i[hlist[1]], i[hlist[3]], a=a, b=b))
            #Every instance +1
            count += 1
    #Print Count of Basement Carparks
    print("Total Number: {}\n".format(count))

def option_3():
    print("Option 3: Read Carpark Availability Data File")
    #Check for correct input. User must input correct value to continue.
    while True:
        try:
            filename = input("Enter the file name: ")
            datafile = open(filename, "r")
            break
        except FileNotFoundError:
            print("File Not Found: Please enter the file's correct name.\n")
    timestamp = datafile.readline()
    #Print Successful Extraction
    print(timestamp)
    line = datafile.readline()
    line = line.strip("\n")
    ahlist = line.split(",")
    alist = []
    #Extract File by Line
    for line in datafile:
        line = line.strip("\n")
        line = line.split(",")
        c_dict = {}
        for n in range(len(line)):
            c_dict[ahlist[n]] = line[n]
        alist.append(c_dict)
    return ahlist, alist, timestamp

def option_4(alist):
    print("Option 4: Print Total Number of Carparks in the File Read in [3]")
    #Print Total Number of Carparks by counting the number of lines in file
    total = len(alist)
    print("Total Number of Carparks in the File: {}\n".format(total))

def option_5(ahlist, alist):
    print("Option 5: Display Carparks Without Available Lots")
    count = 0
    #Prints Carparks Without Availability
    for i in alist:
        #key = hlist[2]
        #0 == No Availability
        if int(i[ahlist[2]]) == 0:
            print("{}: {}".format(ahlist[0], i[ahlist[0]]))
            count += 1
    print("Total Number: {}\n".format(count))

def option_6(ahlist, alist):
    print("Option 6: Display Carparks With At Least x% Available Lots")
    #Check for correct input. User must input correct value to continue
    while True:
        try:
            a_rpercent = int(input("Enter the percentage required: "))
            #Integer must between 0 and 100
            assert a_rpercent <= 100 and a_rpercent >= 0
            break
        except ValueError:
            print("Value Error: Please enter the percentage as an integer value.\n")
        except AssertionError:
            print("Input Error: Please enter a percentage between 0 and 100.\n")
    #Format Positions
    a = len(ahlist[0]) + 2
    b = len(ahlist[1]) + 2
    c = len(ahlist[2]) + 2
    d = len("Percentage")
    print("{:{a}}{:{b}}{:{c}}{:{d}}".format(ahlist[0], ahlist[1], ahlist[2], "Percentage", \
                                            a=a, b=b, c=c, d=d))
    count = 0
    apdict = {}
    #Calculate Availability Percentage, Store them in Dictionary with Carpark No
    for i in alist:
        #ltotal = int(i[ahlist[1]])
        #lavail = int(i[ahlist[2]])
        try:
            #Calculate Availability Percentage and Round 1dp
            a_percent = (int(i[ahlist[2]])/int(i[ahlist[1]]))*100
            a_percent = round(a_percent, 1)
            #Store in a list
            apdict[i[ahlist[0]]] = a_percent
        #When Availability 0
        except ZeroDivisionError:
            #Assign 0.0%
            apdict[i[ahlist[0]]] = 0.0
        #Print
        if a_percent >= a_rpercent:
            print("{:{a}}{:{b}}{:{c}}{:{d}}".format(i[ahlist[0]], i[ahlist[1]], i[ahlist[2]], a_percent, \
                                                    a=a, b=b, c=c, d=d))
            count += 1
    print("Total Number: {}\n".format(count))
    return apdict

def option_7(hlist, dlist, ahlist, alist):
    print("Option 7: Display Addresses of Carparks With At Least x% Available Lots")
    #Check for correct input. User must input correct value to continue.
    while True:
        try:
            a_rpercent = int(input("Enter the percentage required: "))
            #Integers between 0 and 100
            assert a_rpercent <= 100 and a_rpercent >= 0
            break
        except ValueError:
            print("Value Error: Please enter a percentage in integers.\n")
        except AssertionError:
            print("Input Error: Please enter a percentage between 0 and 100.\n")
    #Format Positions
    a = len(ahlist[0]) + 2
    b = len(ahlist[1]) + 2
    c = len(ahlist[2]) + 2
    d = len("Percentage")
    #Print Header
    print("{:{a}}{:{b}}{:{c}}{:{d}}".format(ahlist[0], ahlist[1], ahlist[2], "Percentage", \
                                            a=a, b=b, c=c, d=d), end="  ")
    print("{}".format(hlist[3]))
    count = 0
    apdict = {}
    #Calculate Availability Percentage, Store them in Dictionary with Carpark No
    for i in alist:
        #lots_total = int(i[ahlist[1]])
        #lots_avail = int(i[ahlist[2]])
        confirm = False
        #Calculate Availability Percentage, Store them in Dictionary with Carpark No
        try:
            a_percent = (int(i[ahlist[2]])/int(i[ahlist[1]]))*100
            a_percent = round(a_percent, 1)
            apdict[i[ahlist[0]]] = a_percent
        #When Availability 0
        except ZeroDivisionError:
            #Assign 0.0%
            apdict[i[ahlist[0]]] = 0.0
        if a_percent >= a_rpercent:
            print("{:{a}}{:{b}}{:{c}}{:{d}}".format(i[ahlist[0]], i[ahlist[1]], i[ahlist[2]], a_percent, \
                                                    a=a, b=b, c=c, d=d), end="  ")
            #Finding Address
            for n in dlist:
                if n[hlist[0]] == i[ahlist[0]]:
                    #Address is Found
                    confirm = True
                    #Print Address matching to Carpark No
                    print("{}".format(n[hlist[3]]))
            #If Carpark No Address Not Found
            if confirm == False:
                #Prints \n
                print()
            count += 1
    print("Total Number: {}\n".format(count))
    return apdict

def option_8(hlist, dlist, ahlist, alist, apdict):
    print("Option 8: Display All Carparks at Given Location")
    #Get Location
    location = input("Enter a location: ")
    #Location made into All Capital Letters
    location = location.upper()
    #Split Location into Individual Words
    lklist = location.split()
    #If No Location Entered, Return and Tells User
    if lklist == []:
        print("There is no such location found.")
        return
    
    #Checks for Each Word of the Location in the Address
    llist = []
    #For Each Address
    for i in dlist:
        #For Each Word in Location
        for k in lklist:
            #Word in Location matches Address
            if k in i[hlist[3]]:
                #Store Carpark Number to Address to Location List
                c_dict = {}
                c_dict[hlist[0]] = i[hlist[0]]
                c_dict[hlist[3]] = i[hlist[3]]
                llist.append(c_dict)
                #Once Again, for each word in location
                for s in lklist:
                    #Checks if every word in location in address
                    if s not in llist[-1][hlist[3]]:
                        #Removes if any word is not found
                        llist.remove(llist[-1])
                        #Breaks out of loop to prevent removing the same address again and avoid error
                        break
                #Breaks out of loop as address no longer exists
                #No need to check for its existence again and move on to the next address
                break
    #Consideration for location not being found or does not exist.
    if len(llist) == 0:
        print("There are no carparks found in this location.")
        return
    else:
        print("There are {} carparks found in {}.".format(len(llist), location))
    #Formatting Position
    a = len(ahlist[0]) + 2
    b = len(ahlist[1]) + 2
    c = len(ahlist[2]) + 2
    d = len("Percentage")
    #Format Header
    print("{:{a}}{:{b}}{:{c}}{:{d}}".format(ahlist[0], ahlist[1], ahlist[2], "Percentage", \
                                            a=a, b=b, c=c, d=d), end="  ")
    print("{}".format(hlist[3]))

    #Match Availability to Location
    count = 0
    #For every Availability in file
    #There might not be a matching Location or Address
    for i in alist:
        #Scans through Address List for each availability
        for k in llist:
            #If Matches, Prints
            if k[hlist[0]] == i[ahlist[0]]:
                print("{:{a}}{:{b}}{:{c}}{:{d}}".format(i[ahlist[0]], i[ahlist[1]], i[ahlist[2]], apdict[i[ahlist[0]]], \
                                                        a=a, b=b, c=c, d=d), end="  ")
                print("{}".format(k[hlist[3]]))
                #Remove location as there would be no repeats
                #Removes so lesser to read through loop
                llist.remove(k)
                count += 1
                #Break out of loop as availability match with address
                break

    #Prints Total Carparks With Addresses
    print("Total Number: {}\n".format(count))
    #Prints Carparks with no Availability found
    if len(llist) != 0:
        print("The following {} carparks' availability could not be found:".format(len(llist)))
        print("{:{a}}{}".format(hlist[0], hlist[3], a=a))
        for k in llist:
            print("{:{a}}{}".format(k[hlist[0]], k[hlist[3]], a=a))
        print()

def option_9(hlist, dlist, ahlist, alist, apdict):
    print("Option 9: Display Carpark with the Most Parking Lots")
    c_t = 0
    c_a = 0
    #Check Highest
    for ia in alist: 
        c_1 = int(ia[ahlist[1]])
        c_2 = int(ia[ahlist[2]])
        if c_1 > c_t:
            c_t = c_1
        if c_2 > c_a:
            c_a = c_2
    #3 Lists for Storing
    tmdlist = []
    tclist = []
    talist = []
    #2 or more carparks may have the same total number of lots or availability.
    for ia in alist:
        t_dict = {}
        #Check if total or availability lots may have more than one and store
        if c_t == int(ia[ahlist[1]]):
            for i in ahlist:
                t_dict[i] = ia[i]
            k = ia[ahlist[0]]
            #1 in total list, 1 in common list
            tclist.append(k)
            tmdlist.append(t_dict)
        if c_a == int(ia[ahlist[2]]):
            for i in ahlist:
                t_dict[i] = ia[i]
            k = ia[ahlist[0]]
            #1 in availability list, 1 in common list
            talist.append(k)
            tmdlist.append(t_dict)
    #In common list, assign all details to each Carpark No
    for k in tmdlist:
        for ib in dlist:
            if ib[hlist[0]] == k[ahlist[0]]:
                #t_dict = {}
                for i in hlist:
                    k[i] = ib[i]
                #k.update(t_dict)
                break
    ctrue = 0
    atrue = 0
    lock = False
    loop = True
    #Looking through the list if there are any not printed
    #Worst Case Scenario:
    #   >1 for total, >1 for availability
    #Best Case Scenario:
    #   1 for total, 1 for availability
    #Therefore, need repeat at least twice
    while loop:
        for i in tmdlist:
            #Filters all location in here until otherwise 
            if lock == False:
                #Check if in which list:
                for k in tclist:
                    #If Match, Print
                    if i[hlist[0]] == k:
                        if ctrue == 0:
                            print("Carpark(s) with the Most Total Parking Lots:")
                        for h in hlist:
                            print("{:<24}:{:<}".format(h, i[h]))
                        for h in ahlist[1:]:
                            print("{:<24}:{:<}".format(h, i[h]))
                        print()
                        #Add 1 to Total Count
                        ctrue += 1
                        #Breaks as Match Found
                        break
                #If Total Count == True Total Count
                if ctrue == len(tclist):
                    #Filter Direction Flips
                    lock = True
                    continue
            elif lock == True:
                #Check if in which list:
                for k in talist:
                    #If Match, Print
                    if i[hlist[0]] == k:
                        if atrue == 0:
                            print("Carpark(s) with the Most Available Parking Lots:")
                        for h in hlist:
                            print("{:<24}:{:<}".format(h, i[h]))
                        for h in ahlist[1:]:
                            print("{:<24}:{:<}".format(h, i[h]))
                        print()
                        #Add 1 to Availability Count
                        atrue += 1
                        #Breaks as Match Found
                        break
                #If Availability Count == True Availability Count
                if atrue == len(talist):
                    #All Done, Escape Loop
                    lock = None
                    loop = False
                    break
            #if ctrue + atrue == len(tclist) + len(talist):
                #loop = False
                #break

def option_10(hlist, dlist, ahlist, alist, timestamp):
    print("Option 10: Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
    #Assigns A Value to Find Lowest Number of Lots 
    low = 1000
    #For every availability
    for i in alist:
        for d in dlist:
            #Match Carpark No
            if i[ahlist[0]] == d[hlist[0]]:
                #Store Address, Edit alist
                i[hlist[3]] = d[hlist[3]]
                #Compare Availability
                if low > int(i[ahlist[2]]):
                    low = int(i[ahlist[2]])
                break
    #Opens File to Write
    csvfile = open("carpark-availability-with-addresses.csv", "w")
    #2 Lines Written - Header and Timestamp
    lock = 2
    line = ""
    for k in ahlist:
        line += "{},".format(k)
    line += hlist[3]
    csvfile.write("{}\n".format(line))
    csvfile.write(timestamp)
    #Need Loop-over-loop as Availability not sorted
    while lock != len(alist)+2:
        #Print All Availability with Addresses
        for i in alist:
            #Current Low Availability matches Carpark No. Details
            if low == int(i[ahlist[2]]):
                line = ""
                #Print Details
                for k in i.keys():
                    line += "{}".format(i[k])
                    if i[k] != ahlist[-1]:
                        line += ","
                csvfile.write("{}\n".format(line))
                #Count +1
                lock += 1
        #Move on to next lowest availability
        low += 1
    #Close File
    csvfile.close()
    #Print File Details
    print("Filename: \"carpark-availability-with-addresses.csv\"")
    print("Number of Lines: {}\n".format(lock))


#Legend
#hlist = Main File (carpark-information.csv) Header List
#dlist = List containing Main File's Dictionary
#ahlist = Availability File (carpark-availability-v1.csv) Header List
#alist = List containing Availability File's Dictionary
#apdict = List containing Dictionaries of Capark No with their respective Availability Percentages

#Start Here
choice = input("Switch to GUI? [Y/N] ")
if " " not in choice and "Y" in choice.capitalize():
    print("Switching User to GUI...")
    print("Displaying Main Interface")
    import S10257584_Assignment_Extra1
else:
    print("Assuming User Not Switching GUI...")

#Main Loop Code
#Call Read File Function
carpark_hlist, carpark_main_list = readfile()
online = True
while online:
    #Calls for Display of Option Menu and Returns Option Choice
    option = main_menu_option()
    #Filter Choice
    if option == 0:
        break
    elif option == 1:
        option_1(carpark_main_list)
        continue
    elif option == 2:
        option_2(carpark_hlist, carpark_main_list)
        continue
    elif option == 3:
        carpark_ahlist, carpark_alist, atime = option_3()
        continue
    else:
        #Check if user has completed Option 3 before continuing
        try:
            assert type(carpark_ahlist) == list
        except NameError:
            print("Name Error: Please select Option [3] first.\n")
            continue
    if option == 4:
        option_4(carpark_alist)
        continue
    elif option == 5:
        option_5(carpark_ahlist, carpark_alist)
        continue
    elif option == 6:
        carpark_apdict = option_6(carpark_ahlist, carpark_alist)
        continue
    elif option == 7:
        carpark_apdict = option_7(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist)
        continue
    elif option == 10:
        option_10(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, atime)
        continue
    else:
        #Check if user has completed Option 6/7 before continuing
        try:
            assert type(carpark_apdict) == dict
        except NameError:
            print("Name Error: Please select Option [6] or [7] first.\n")
            continue
    if option == 8:
        option_8(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, carpark_apdict)
        continue
    else:
    #elif option == 9:
        option_9(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, carpark_apdict)

#Old Edited Codes
#1. Main Loop
#Too repetitive in program validation structure
"""
elif option == 4:
    try:
        option_4(carpark_alist)
    except NameError:
        print("Please select Option [3] first.\n")
            
elif option == 7:
    try:
        carpark_apdict = option_7(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist)
    except NameError:
        print("Please select Option [3] first.\n")
    
elif option == 8:
    try:
        option_8(carpark_hlist, carpark_main_list, carpark_ahlist, carpark_alist, carpark_apdict)
    except NameError:
        try:
            assert type(carpark_apdict) == dict
        except NameError:
            try:
                assert type(carpark_ahlist) == list
            except NameError:
                print("Please select Option [3] first.")
            print("Please select Option [6] or [7] first.\n")
"""
#2. Inconcise phrasing of code
"""
    if ctrue + atrue == len(tclist) + len(talist):
        loop = False
        break
"""
#Unnecessary as it is already determined that when
#atrue == len(talist), ctrue must be == len(tclist)
