#Chia Wei En Wayne (S10257584G) - CSF02 (P07)
#Status: Completed, Checked

#Input
id_input = input("Enter an ID: ")
append = "@abc.edu.sg"

#Find "-" Process
if id_input.find("-") != -1:
    id_split = id_input.split("-")      #Split string using "-"
    append = append.replace("@",".")    #Change append to fit into new email
    email = f"{id_split[1]}@{id_split[0]}{append}" #{id}@{department_code}.abc.edu.sg
else:
    email = f"{id_input}{append}"       #id_input + append = {id}@abc.edu.sg

#Display
print("\nEmail Address: {}".format(email.lower()))    #Display email in lowercase

"""
id_input = input("Enter an ID: ")
append = "@abc.edu.sg"
id_input = id_input.lower()
if id_input.find("-") != -1:
    id_split = id_input.split("-")
    email = "{}@{}{}".format(id_split[1], id_split[0], append.replace("@",".")
else:
    email = f"{id_input}{append}"
print("\nEmail Address: {}".format(email)) 
"""
