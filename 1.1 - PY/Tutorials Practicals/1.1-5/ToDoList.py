#Name: Chia Wei En Wayne
#Student ID: S10257584
#Date: 15 May 2023
#Status: Completed, Checked

path = "C:\\1.1\\Text Files\\"
scriptfile = open(path + "todolist.txt", "r")

line1 = scriptfile.readline()
line2 = scriptfile.readline()
line3 = scriptfile.readline()

print(line1.strip())
print(line2.strip())
print(line3.strip())
