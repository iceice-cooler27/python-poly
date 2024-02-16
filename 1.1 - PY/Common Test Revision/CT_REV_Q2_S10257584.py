#Chia Wei En Wayne (S10257584) - P07 (CSF02)

#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 31 May 2023
#Status: Completed

"""
#Blackjack
ace = False

#Input
def cardValue(count):
    card = int(input("Enter card {}: ".format(count)))
    if card > 10:
        card = 10
    return card

count = 1
card1 = cardValue(count)

count = 2
card2 = cardValue(count)

count = 3
card3 = cardValue(count)

if card1 == 1 or card2 == 1 or card3 == 1:
    ace = True

#Calculation
total = card1 + card2 + card3

if ace == True and total <= 11:
    total += 10

#Display
print("Total value is {}".format(total))
"""

#Clearer Method
total = 0
ace = 0

for n in range(3):
    card = int(input("Enter card {}: ".format(n+1)))
    if card > 10:
        card = 10
    if card == 1:
        ace += 1
    else:
        total += card

for i in range(ace):
    if total + 11 <= 21:
        total += 11
    else:
        total += 1

print("Total value is {}".format(total))
