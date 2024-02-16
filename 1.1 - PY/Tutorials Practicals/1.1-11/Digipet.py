#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 26 June 2023
#Status: Completed

#List
menu = ["Feed", "Play", "Rest", "Status"]
status = [3, 3, 3]
title = ["hungry", "happiness", "energy"]
msg = ["Nom nom nom", "XD", "Zzzzz"]

#Constant Loop
online = True
star = "*"
empty = "."

print("Digipet")
while online:
    #Print Menu
    for m in menu:
        print("({}) {}".format(menu.index(m)+1, m))
    #Request Input, Select Option
    select = int(input("Please select an option: "))
    #Sorting Selection
    if select == 4:
        for i in range(len(status)):    #Length = No. of Options = 3
            level = "....."
            s = status[i]
            #Another way to code (as a nested loop)
            #for n in range(s):
                #level = level.replace(empty, star, 1)
            level = level.replace(empty, star, s)
            print("{:11}{}".format(title[i], level))
        """
        elif select > 4:    #Options limited to 4, therefore unnecessary, but allows user to stop program (Break Loop)
            online = False
        """
    else:
        spos = select - 1
        #Print Message Text
        print(msg[spos])
        for i in range(len(status)):
            #Change level values
            if i == spos:
                status[i] += 1
            else:
                status[i] -= 1
            #Check if below minimum or above maximum
            if status[i] < 0:
                status[i] = 0
            elif status[i] > 5:
                status[i] = 5
