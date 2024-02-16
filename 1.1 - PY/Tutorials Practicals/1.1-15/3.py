#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 22 July 2023
#Status: Incomplete

from tkinter import *

window = Tk()
window.title("Temperature Converter")
window.geometry("400x300")

celsiusTemp = Label(window, text="Temperature(Celsius)", width=24)
fahrenheitTemp = Label(window, text="Temperature(Fahrenheit)", width=24)
celsiusEntry = Entry(window, width=24)
fahrenheitEntry = Entry(window, width=24)

celsiusTemp.place(x=0, y=20)
fahrenheitTemp.place(x=200, y=20)
celsiusEntry.place(x=0, y=60)
fahrenheitEntry.place(x=200, y=60)
