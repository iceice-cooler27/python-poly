#Done By: Chia Wei En Wayne
#Date: 4 May 2023

path = "C:\\1.1\\Text Files\\"
textfile = open(path + "StudentData.txt", "r")

name1 = textfile.readline()
name2 = textfile.readline()

contact1 = name1.split(",")
contact2 = name2.split(",")

print("{:16}{:14}".format("Name", "Mobile Contact"))
print("{:16}{}{:16}{}".format(contact1[0],contact1[1], \
                              contact2[0],contact2[1]))
