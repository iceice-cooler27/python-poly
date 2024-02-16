#Programming I

#############################
#     Side Quest 6.1        #
#   Driverless Vehicle 2    #
#############################

#Background
#==========
#Tom would like to enhance the safety of his driverless vehicle by applying braking when
#the vehicle is less than 50 meters from an object. 

#Write a Python program that prompts the user to enter a set of round trip times
#(similar to previous question, each value to be separated by commas, and speed of sound
#at 344 m/s), and returns True if the vehicle is too near an object or False if the
#vehicle is within safe margin of other objects.



#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - roundTrips
#   - tooNear



#START CODING FROM HERE
#======================
#Check closest object
def fail_safety_distance(roundTrips):
    #Perform the parsing of roundTrips input here
    roundTrips = roundTrips.split(",")
    count = 0
    #Check whether vehicle is too near an object, return True if so, False otherwise
    while count <= len(roundTrips)-1:
        time = float(roundTrips[count])
        distance = (time * 344)/2
        if distance < 50:
            tooNear = True
            break
        else:
            tooNear = False
        count += 1
    if len(roundTrips) < 5:
            tooNear = [-1,-1]
    return tooNear#Do not remove this line

#Prompt user to enter a minimum of 5 round trip times separated with commas
roundTrips = input("Enter a minimum of 5 round trips made by the sound waves (in seconds): ")
    
result = fail_safety_distance(roundTrips)

#Modify to display if vehicle is too near an object 
print("Is the vehicle too near an object? {}".format(result))

#input 0.5,2.1,0.3,1.8,2.3  output False
#input 0.1,2.0,1.6,0.5,1     output True
