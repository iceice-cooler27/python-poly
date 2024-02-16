#Optional
#Name: Chia Wei En Wayne
#Student ID: S10257584
#Date: 15 May 2023
#Status: Completed

#Input
filename = input("Please enter the filename: ")

#Open
path = "C:\\1.1\\Text Files\\"
textfile = open(path + filename, "r")
text = textfile.read()
text = text.split()
no_word = len(text)
textfile.close()

#Write Output
outfile = open(path + "output.txt", "w")
outfile.write("There are {} words in the document.".format(no_word))
outfile.close()

