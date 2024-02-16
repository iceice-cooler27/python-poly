#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def obtain_grade(mark):
    if mark < 49.5:
        grade = "F"
    elif mark < 54.5:
        grade = "D"
    elif mark < 59.5:
        grade = "D+"
    elif mark < 64.5:
        grade = "C"
    elif mark < 69.5:
        grade = "C+"
    elif mark < 74.5:
        grade = "B"
    elif mark < 79.5:
        grade = "B+"
    elif mark < 84.5:
        grade = "A"
    else:
        grade = "A+"
    return grade

mark_list = [["Mary", 90.5],["Charles", 60.4],\
             ["John",70.5],["Javier",32.0],\
             ["Luke", 46.7]]

print("{:15}{:10}{}".format("Student Name", "Mark", "Grade"))
for student in mark_list:
    name = student[0]
    mark = float(student[1])
    grade = obtain_grade(mark)
    print("{:15}{:<10}{:^4}".format(name, mark, grade))
