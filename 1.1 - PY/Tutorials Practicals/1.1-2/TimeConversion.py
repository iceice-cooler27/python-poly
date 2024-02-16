#Chia Wei En Wayne S10257584

#Input
#Accepts time in seconds
second = int(input("Please enter the time to be converted, in sec: "))

#Process
minute = second // 60
second = second % 60

hour = minute // 60
minute = minute % 60

#Output
print("Time: " + str(hour) + " hr, " + str(minute) + " min " + str(second) + " sec")
