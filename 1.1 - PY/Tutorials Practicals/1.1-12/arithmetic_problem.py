#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 3 July 2023
#Status: Completed, Checked

def menu():
    print("Options Menu: ")
    menu_list = ["Addition", "Subtraction", "Multiplication", "Division", "Random"]
    for n in range(5):
        print("({}) {}".format(n+1, menu_list[n]))
    choice = int(input("Please enter an option of your choice: "))
    return choice

#Message
def print_correct_msg(no):
    msg_list = ["Very Good!", "Excellent!", \
                "Nice Work!", "Keep Up The Good Work!"]
    msg = msg_list[no]
    return msg
def print_incorrect_msg(no):
    msg_list = ["No. Please Try Again.", "Wrong. Try Once More.", \
                "Don't Give Up!", "No. Keep Trying."]
    msg = msg_list[no]
    return msg

#Math Problems
def math_addition(num1, num2):
    corr_ans = num1 + num2
    input_ans = int(input("How much is {} + {}? ".format(num1, num2)))
    return corr_ans, input_ans

def math_subtraction(num1, num2):
    corr_ans = num1 - num2
    input_ans = int(input("How much is {} - {}? ".format(num1, num2)))
    return corr_ans, input_ans

def math_multiplication(num1, num2):
    corr_ans = num1 * num2
    input_ans = int(input("How much is {} * {}? ".format(num1, num2)))
    return corr_ans, input_ans

def math_division(num1, num2):
    corr_ans = num1 / num2
    input_ans = float(input("How much is {} / {}? ".format(num1, num2)))
    return corr_ans, input_ans

#Loop
import random
online = True
while online:
    choice = menu()
    print()
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    if choice == 5:
        choice = random.randint(1,4)
    if choice == 1:
        corr_ans, input_ans = math_addition(num1, num2)
    elif choice == 2:
        corr_ans, input_ans = math_subtraction(num1, num2)
    elif choice == 3:
        corr_ans, input_ans = math_multiplication(num1, num2)
    elif choice == 4:
        corr_ans, input_ans = math_division(num1, num2)
    else:
        online = False
        break

    msg_no = random.randint(0,3)
    if input_ans == corr_ans:
        print(print_correct_msg(msg_no))
        online = False
    else:
        print(print_incorrect_msg(msg_no))
    print()
        
