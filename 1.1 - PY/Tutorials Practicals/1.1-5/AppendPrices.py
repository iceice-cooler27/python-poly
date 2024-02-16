#Name: Chia Wei En Wayne
#Student ID: S10257584
#Date: 15 May 2023
#Status: Completed

#Things to Append
teh_peng = ["teh peng", 1.20]
milo_peng = ["milo peng", 1.40] 

#Open Append Mode
path = "C:\\1.1\\Text Files\\"
menufile = open(path + "prices.txt", "a")

#Write
menufile.write("{}: ${:.2f}\n".format(teh_peng[0], teh_peng[1]))
menufile.write("{}: ${:.2f}\n".format(milo_peng[0], milo_peng[1]))
menufile.close()
