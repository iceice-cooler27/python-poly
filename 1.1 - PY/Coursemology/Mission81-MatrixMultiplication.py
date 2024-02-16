#Programming I

#########################
#      Mission 8.1      #
# Matrix Multiplication #
#########################

#Background
#==========
#Tom wants to multiply a 3x3 matrix with a 3x1 matrix.
#Write a Python program to multiply matrix A with matrix B
#and store the result in matrix C, which is a 3x1 matrix.


#Important Notes
#===============
#1) You MUST use the variables, A, B, C

#START CODING FROM HERE
#======================

#define the function to multiply matrix A with matrix B, store
#the product in matrix C and return
def matrix_multiplication(A,B):
    C = []
    #Add your code here
    for i in A:
        total = 0
        for n in range(3):  #len(i)
            a = i[n]
            b = B[n]
            total += a*b
        C.append(total)
    return C #do not remove this line
       
#Define matrix A as a nested list and matrix B as a list
#remove these statements when submitting in Coursemology
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [1,2,3]

#Do not remove the next line that calls the function
C = matrix_multiplication(A,B)

#Display the result
print(C)

