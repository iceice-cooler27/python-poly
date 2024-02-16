#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 10 July 2023
#Status: Completed, Checked

prices = {"chicken" : 8.50,\
          "steak" : 13.80,\
          "fish" : 9.80,\
          "pasta" : 9.50,\
          "coffee" : 2.50,\
          "tea" : 1.80,\
          "water" : 0.50}

def showMenu():
    print("{:-<19}".format(""))
    print("1. Add Order")
    print("2. Summarise Orders")
    print("3. Quit")
    print("{:-<19}".format(""))

#Order Menu
orderlist = []
online = True
while online:
    showMenu()
    
    option = int(input("Your Choice? "))
    if option == 1:
        print("{:11}{}".format("Items", "Prices"))
        print("{:11}{}".format("-"*4, "-"*5))
        for key in prices:
            print("{:11}${:.2f}".format(key.capitalize(), prices[key]))
        order = input("Your Order? ")
        order = order.lower()
        if prices.get(order) == None:
            print("{} is not available.".format(order.capitalize()))
        else:
            num = int(input("How many sets? "))
            print("{} sets of {} ordered.".format(num, order))
            repeat = False
            for n in orderlist:
                if order in n[0]:
                    repeat = True
                    count = orderlist.index(n)
                    break
            if repeat == True:
                orderlist[count][1] += num
            else:
                orderlist.append([order, num])
            """
            if order not in orderlist:
                orderlist[order] = num
            else:
                orderlist[order] += num
            """
            
    elif option == 2:
        print("{:11}{}".format("Items", "Quantity"))
        print("{:11}{}".format("-"*4, "-"*8))
        cost = 0
        for i in orderlist:
            print("{:11}{}".format(i[0].capitalize(), i[1]))
            cost += i[1]*prices[i[0]]
        print("Total Cost = ${:.2f}".format(cost))

    else:
        online = False
    print()
