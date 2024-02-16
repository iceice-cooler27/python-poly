#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 22 May 2023
#Status: Completed

#Display
print("Welcome to Number Guessing Game")
import random
correct_no = random.randint(0,100)
count = 1
print(correct_no)

#Loop Input
input_no = int(input("Try {}: Enter a number between 1 and 100 (or -1 to end): ".format(count)))
while True:
    if input_no > -1:
        if input_no < correct_no:
            print("{} is too low.".format(input_no))
            count += 1
        elif input_no > correct_no:
            print("{} is too high.".format(input_no))
            count += 1
        else:
            print("Bingo, you've got it right!")
            break
    else:
        break
    if count > 5:
            break
    input_no = int(input("Try {}: Guess again, enter a number between 1 and 100 (or -1 to end): ".format(count)))
print("\nBye-bye!")
