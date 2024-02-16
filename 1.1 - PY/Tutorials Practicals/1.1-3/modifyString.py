#Done by: Chia Wei En Wayne
#Date: 4 May 2023

#Input
#Prompt user to input the original string and substring to delete
original = input("Enter original string: ")
delete = input("Enter substring to delete: ")

#Process
modified = original.replace(delete, "", 1)

#Or

#index_delete = original.find(delete, 1)
#length_delete = len(delete)
#modified = original(:index_delete) + original(index_delete + length_delete:)

#Display
print(modified)
