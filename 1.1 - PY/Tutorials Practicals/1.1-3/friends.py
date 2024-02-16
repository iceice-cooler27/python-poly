#Done By: Chia Wei En Wayne
#Date: 4 May 2023

#Create a list of strings friends and initialise with the following
#string elements "Izzat", "Bryan", "Dalton", "Ethan", "Isaac"
#Initial
friend_list = ["Izzat", "Bryan", "Dalton", "Ethan", "Isaac"]

#Prompt the user to input a new name
#Add this new name to friends and print the new friends' list
#Append this new name and print the new friends' list
new_friend = input("What is the name of your new friend? ")
friend_list.append(new_friend)
print("My friends are: {}".format(friend_list))

#Prompt the user to input an existing name to be removed
#Show the index of this name in the list
#Remove this name from the friends' list
no_friend = input("Who do you want to friendzone? ")
remove_index = friend_list.index(no_friend)
friend_list.remove(no_friend)
print("""{} was in position {}. He will be friendzoned.
My eligible friends are now: {}""".format(no_friend, remove_index, friend_list))
