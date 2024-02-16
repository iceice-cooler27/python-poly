#Name: Chia Wei En Wayne
#Students ID: S10257584G
#Date: 22 May 2023
#Status: Completed

#Find and Open File
path = "C://1.1//Text Files//"
studentfile = open(path + "marks.txt", "r")
rawdata = studentfile.read()
studentdata = rawdata.split("\n")
studentdata.pop(-1)

end = False
count = len(studentdata)
index = 0
total = 0

#Start Display
print("{:<12}{:<}".format("Name", "Mark"))
print("{:<12}{:<}".format("----","----"))

#Loop Extraction
while not(end):
    i_data = studentdata[index]
    data = i_data.split(";")
    print("{:<12}{:<.1f}".format(data[0],float(data[1])))
    total += float(data[1])
    index += 1
    if index == count:
        end = True
average = total / count
print("\nAverage Mark: {:.2f}".format(average))
    
