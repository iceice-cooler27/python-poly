#BMI_BMR_Calculator.py
#this program calculates the body mass index and basal metabolic rate

#Calculate BMI
weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(m): '))

bmi = weight / (height * height)

print('BMI: ', bmi)

#Calculate BMR
age = float(input('Enter age(years): '))

bmr =  10 * weight + 6.25 * height - 5 * age + 5

print('BMR: ', str(bmr))

