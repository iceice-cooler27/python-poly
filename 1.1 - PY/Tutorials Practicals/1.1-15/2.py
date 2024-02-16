#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 22 July 2023
#Status: Incomplete

def displayBMI():
    weight = float(weightEntry.get())
    height = float(heightEntry.get())
    bmiText.delete("1.0", END)
    bmi = weight / (height*height)
    bmi = round(bmi, 2)
    bmiText.insert(END, bmi)

from tkinter import *
window = Tk()
window.title("BMI Calculator")
window.geometry("400x300")

weightLabel = Label(window, text="Weight (kg)", width=12)
weightEntry = Entry(window, width=24)
heightLabel = Label(window, text="Height (m)", width=12)
heightEntry = Entry(window, width=24)
bmiLabel = Label(window, text="BMI", fg="blue", width=12)
bmiText = Text(window, fg="blue", bg="yellow", width=18, height=1)
calculateButton = Button(window, text="Calculate", width=12, command=displayBMI)

weightLabel.place(x=20, y=20)
weightEntry.place(x=120, y=20)
heightLabel.place(x=20, y=60)
heightEntry.place(x=120, y=60)
bmiLabel.place(x=20, y=100)
bmiText.place(x=120, y=100)
calculateButton.place(x=280, y=100)
