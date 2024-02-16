#Done by: Chia Wei En Wayne
#Date: 8 May 2023
#Checked

#Input
mark = float(input("Please enter your marks: "))

#Process
if mark >= 85:
    grade = "A+"
    comment = "Excellent!"
elif mark >= 80 and mark < 85:  #80 <= mark <= 85
    grade = "A"
    comment = "Well done."
elif mark >= 75 and mark < 80:
    grade = "B+"
elif mark >= 70 and mark < 75:
    grade = "B"
elif mark >= 65 and mark < 70:
    grade = "C+"
elif mark >= 60 and mark < 65:
    grade = "C"
elif mark >= 55 and mark <60:
    grade = "D+"
elif mark >= 50 and mark < 55:
    grade = "D"
else:
    grade = "F"
    comment = "See me."

#Display
print("Grade: {}".format(grade))

if grade == "A+" or grade == "A" or grade == "F":
    print(comment)
