#Programming I

####################################
#           Side Quest 3.2         #
#           Caesar Cipher          #
####################################

#Background
#==========
#The encryption of a plaintext by Caesar Cipher is:
#En(Mi) = (Mi + n) mod 26 

#Write a Python program that prompts user to enter a plaintext
#and displays the encrypted result using Caesar Cipher.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - plaintext
#   - n (to represent number of shifts in int)
#   - ciphertext

#START CODING FROM HERE
#======================

#Function to perform the encryption of given plaintext
def caesarEncrypt(plaintext, n):
    #Code to do the conversion
    ciphertext = plaintext.lower()
    #A
    if ciphertext.find("a") != -1:
        ord_pos = (ord("A") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("a", newchr)
    #B
    if ciphertext.find("b") != -1:
        ord_pos = (ord("B") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("b", newchr)
    #C
    if ciphertext.find("c") != -1:
        ord_pos = (ord("C") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("c", newchr)
    #D
    if ciphertext.find("d") != -1:
        ord_pos = (ord("D") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("d", newchr)
    #E
    if ciphertext.find("e") != -1:
        ord_pos = (ord("E") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("e", newchr)
    #F
    if ciphertext.find("f") != -1:
        ord_pos = (ord("F") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("f", newchr)
    #G
    if ciphertext.find("g") != -1:
        ord_pos = (ord("G") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("g", newchr)
    #H
    if ciphertext.find("h") != -1:
        ord_pos = (ord("H") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("h", newchr)
    #I
    if ciphertext.find("i") != -1:
        ord_pos = (ord("I") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("i", newchr)
    #J
    if ciphertext.find("j") != -1:
        ord_pos = (ord("J") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("j", newchr)
    #K
    if ciphertext.find("k") != -1:
        ord_pos = (ord("K") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("k", newchr)
    #L
    if ciphertext.find("l") != -1:
        ord_pos = (ord("L") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("l", newchr)
    #M
    if ciphertext.find("m") != -1:
        ord_pos = (ord("M") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("m", newchr)
    #N
    if ciphertext.find("n") != -1:
        ord_pos = (ord("N") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("n", newchr)
    #O
    if ciphertext.find("o") != -1:
        ord_pos = (ord("O") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("o", newchr)
    #P
    if ciphertext.find("p") != -1:
        ord_pos = (ord("P") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("p", newchr)
    #Q
    if ciphertext.find("q") != -1:
        ord_pos = (ord("Q") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("q", newchr)
    #R
    if ciphertext.find("r") != -1:
        ord_pos = (ord("R") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("r", newchr)
    #S
    if ciphertext.find("s") != -1:
        ord_pos = (ord("S") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("s", newchr)
    #T
    if ciphertext.find("t") != -1:
        ord_pos = (ord("T") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("t", newchr)
    #U
    if ciphertext.find("u") != -1:
        ord_pos = (ord("U") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("u", newchr)
    #V
    if ciphertext.find("v") != -1:
        ord_pos = (ord("V") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("v", newchr)
    #W
    if ciphertext.find("w") != -1:
        ord_pos = (ord("W") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("w", newchr)
    #X
    if ciphertext.find("x") != -1:
        ord_pos = (ord("X") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("x", newchr)
    #Y
    if ciphertext.find("y") != -1:
        ord_pos = (ord("Y") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("y", newchr)
    #Z
    if ciphertext.find("z") != -1:
        ord_pos = (ord("Z") - ord("A") + n)%26 + ord("A")
        newchr = chr(ord_pos)
        ciphertext = ciphertext.replace("z", newchr)
    
    return ciphertext #Do not remove this line


#You need only to copy and paste the function into Coursemology for submission
#The rest of code from here onwards are not needed 

#Display output heading
print("Substitution Cipher - Caesar Cipher")
print("-" * 35)

#Prompt user for input of plaintext and number of shifts
plaintext = input("Enter the plaintext: ")
n = int(input("Enter the number of positions to be shifted: "))
   
#Call the function to get the cipher text
ciphertext = caesarEncrypt(plaintext, n)

#Display the output
print("Ciphertext is \"{}\".".format(ciphertext))

#input 'HELLOWORLDTHESECRETISOUT',5 output 'MJQQTBTWQIYMJXJHWJYNXTZY'

#Falied Attempt No.1
#Reason:
#Did not consider characters after Z becoming A.
