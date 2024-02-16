#Done by: Chia Wei En Wayne
#ID: S10257584
#Date: 8 May 2023
#Checked

#Input
import re
password = input("Enter password: ")

#Conditions
if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif re.search(r"[0-9]", password) == None:
    print("Password must contain at least one digit.")
elif re.search(r"[A-Z]", password) == None:
    print("Password must contain at least one uppercase letter.")
elif re.search(r"[a-z]", password) == None:
    print("Password must contain at least one lowercase letter.")
else:
    print("Password is valid.")

#Or
"""
if len(password) < 8:
    print("Password must be at least 8 characters loong.")
    if password.isalpha() == True:
        print("Password must contain at least one digit.")
    if password == password.lower():
        print("Password must contain at least one uppercase letter.")
    if password == password.upper():
        print("Password must contain at least one lowercase letter.")
    else:
    print("Password is valid.")
"""
#Or
"""
if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not re.search(r"[0-9]", password):
    print("Password must contain at least one digit.")
elif not re.search(r"[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
elif not re.search(r"[a-z]", password):
    print("Password must contain at least one lowercase letter.")
else:
    print("Password is valid.")
"""
