#Name: Chia Wei En Wayne
#Student ID: S10257584
#Date: 15 May 2023
#Status: Completed

#List
prices = [ ["kopi", 0.40],
           ["teh", 0.40],
           ["milo", 0.50],
           ["soft drinks",1.20] ]

#Assign
def itemlist(index, prices):
    menu = prices.pop(index)
    return menu

index = 0                           #Pop out, means no longer in list.
kopi = itemlist(index, prices)      #Therefore, index should not change,
teh = itemlist(index, prices)       #as 1st item in list changes.
milo = itemlist(index, prices)
soft_drink = itemlist(index, prices)

#Write Text
path = "C:\\1.1\\Text Files\\"
menufile = open(path + "prices.txt", "w")
menufile.write("{}: ${:.2f} \n".format(kopi[0], kopi[1]))
menufile.write("{}: ${:.2f} \n".format(teh[0], teh[1]))
menufile.write("{}: ${:.2f} \n".format(milo[0], milo[1]))
menufile.write("{}: ${:.2f} \n".format(soft_drink[0], soft_drink[1]))
menufile.close()
