#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 26 June 2023
#Status: Completed

#Map
map = [ ["T", " ", " ", " ", "T"], \
        [" ", "P", " ", " ", " "], \
        [" ", " ", " ", "T", " "], \
        [" ", "T", " ", " ", " "] ]

#Display
bar = "+"
for b in range(len(map[0])):
    bar += "---+"
print(bar)

for r in range(len(map)):
    insert = "|"
    for pos in range(len(map[r])):
        insert += " {} |".format(map[r][pos])
    print(insert)
    print(bar)
