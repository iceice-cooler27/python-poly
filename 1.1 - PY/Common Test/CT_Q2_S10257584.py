#Chia Wei En Wayne (S10257584) - CSF02(P07)
#Status: Completed, Checked

#1st Input
in_word = input("Enter your word: ")
in_word = in_word.lower()

#1st Display
length_word = len(in_word)
print("Your input has {} characters".format(length_word))

#2nd Input
pos_chr = input("Input the positions of the characters to select, separated by ',': ")

#Character Swapping
pos_chr = pos_chr.split(",")
chr1 = in_word[int(pos_chr[0])-1]
chr2 = in_word[int(pos_chr[1])-1]

in_word = in_word.replace(chr1, chr2.capitalize())
in_word = in_word.replace(chr2, chr1.capitalize())

out_scramble = in_word.lower()

#2nd Display
print("Swapping the characters '{}' and '{}'".format(chr1, chr2))
print("Scrambled word: {}".format(out_scramble))
