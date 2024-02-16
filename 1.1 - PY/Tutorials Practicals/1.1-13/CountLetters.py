#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 10 July 2023
#Status: Completed, Checked

#Input
inp = input("Enter a sentence: ")

#Lists to Dictionary
alpha = []
letters = {}
for abc in inp:  
    if abc.isalpha() == True:
        alpha.append(abc.lower())
for abc in alpha:
    count = alpha.count(abc)
    append = {abc:count}
    letters.update(append)
    #letters[abc] = count

#Display
for key in letters:
    #value = letters[key]
    print("{} : {}".format(key, letters[key]))

"""
sentence = input("Enter a sentence: ").lower()
letters = {}

for char in sentence:
    if char.isalpha():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    else:
        continue
for char in letters:
    print("{} : {}".format(char, letters[char]))
"""
