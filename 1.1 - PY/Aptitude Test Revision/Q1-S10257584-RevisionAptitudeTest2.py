#Chia Wei En Wayne (S10257584G) - CSF02

#Open Sales.txt File
path = "C:\\1.1\\Text Files\\Revision\\"
salefile = open(path + "sales.txt", "r")

#a
salelist = []
for line in salefile:
    line = line.strip()
    line = line.split(",")
    salelist.append(line)
salefile.close()
print(salelist, "\n")

#b
product_list = ["MacBook Air", "MacBook Pro", "iMac"]
total_units_list = [0, 0, 0]
for n in salelist:
    for i in n:
        print("{:15}".format(i), end = "")
    print()
    for pos in range(len(product_list)):
        if product_list[pos] == n[1]:
            total_units_list[pos] += int(n[2])
            break   #Not necessary but is best to use break as to not waste system resources
#c
print("\n{:15}{:15}".format("Product", "Total Units Sold"))
for p in range(len(product_list)):
    print("{:15}{:<15}".format(product_list[p], total_units_list[p]))
