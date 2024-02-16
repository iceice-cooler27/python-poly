#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Date: 22 May 2023
#Status: Completed

#exit_status = False
count = 1
wordlist = []
total_letter = 0

#Loop Input
while count <= 5:
    new_word = input("Enter world (x to exit): ")   #not(exit_status) and
    if new_word == "x":
        break   #exit_status = True
    else:
        if new_word in wordlist:
            print("\"{}\" has already been entered.".format(new_word))
            continue
        else:
            wordlist += [new_word]
            total_letter += len(new_word)
            count += 1

#Display
print("Your words are {}".format(wordlist))
print("The number of letters in these words is {}".format(total_letter))
