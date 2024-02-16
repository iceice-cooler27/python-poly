#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 26 June 2023
#Status: Completed

#List
player = ["Hafu", "Toast", "Pokimane", \
          "Pewdiepie", "Ninja", "Markiplier"]

results = [ [98, 107, 87, 121], \
            [88, 111], \
            [79, 130, 99], \
            [86, 100, 121, 66, 98], \
            [108, 79, 92], \
            [77, 126, 93, 100, 73, 89] ]

#Display
print("{:12} {:5} {:4} {:5}".format("Player", "Games", "Wins", "Total"))
for p in player:
    total = 0
    num = 0
    win = 0
    """
    for n in results:
        if player.index(p) == results.index(n):
            for i in n:
                total += i
                num += 1
                if i >= 100:
                    win += 1
    """
    for i in results[player.index(p)]:
        total += i
        num += 1
        if i >= 100:
            win += 1
    print("{:12} {:^5} {:^4} {:^5}".format(p, num, win, total))
