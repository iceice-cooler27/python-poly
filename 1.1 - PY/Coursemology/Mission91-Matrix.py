#Programming I

######################
#     Mission 9.1     #
#   MartrixMultiply   #
#######################

#Background
#==========
#Tom has studied about creating 3D games and wanted
#to write a function to multiply 2 matrices.
#Define a function MaxtrixMulti() function with 2 parameters.
#Both parameters are in a matrix format.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[2,0,0],
     [0,2,0],
     [0,0,2]]

#START CODING FROM HERE
#======================

#Create your function here
def matrixmulti(a, b):
    rowA = len(a[0])
    colB = len(b)
    if rowA == colB:
        ans = []
        for col in range(colB):
            ans.append([])
        print(ans)
        for index in range(rowA):
            for i in a[index]:
                val = 0
                for n in b:
                    val += i * n[index]
                ans[index].append(val)
    return ans
   
#Do not remove the next line
ans = matrixmulti(A, B)

#3) For testing, print out the output
#   - Comment out before submitting
print(ans)




