#Done by: Chia Wei En Wayne
#ID: S10257584
#Date: 8 May 2023
#Checked

#Input
sees_player = input("Does the guard see the player? (y/n) ")

#Conditions
if sees_player.lower() == "n": #"N" accepted as well
    print("The guard waits.")
else:
#elif sees_player == "y" or "Y":
    dist_player = int(input("How far away is the player? "))
    if dist_player <= 1:
        print("The guard attacks!")
    elif dist_player >= 2 and dist_player <= 4:
        print("The guard advances.")
    else:
    #elif dist_player >= 5:
        print("The guard waits.")
