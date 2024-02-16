#Q1
#Name: Chia Wei En Wayne
#Student ID: S10257584G
#Group: CSF02
#Status: Complete, Checked

#Input
l = int(input("What is your desired loan amount? "))
a = int(input("What is your annual income? "))
c = int(input("What is the total value of your current loans? "))
s = float(input("What is the total of your savings? "))
y = float(input("How many years do you want to pay back this loan? "))

#Calculation Process
def interestrate(l, a, c, s, y):
    i_r = (l + c)/(s + a * y)
    return i_r

#Display
i_r = interestrate(l, a, c, s, y)
print("Your interest rate is {:.1f}%".format(i_r*100))
