#Name: Chia Wei En Wayne
#ID: S10257584G
#Date: 22 July 2023
#Status: Completed

#Define the function(s) to be used in the application
def displayTable():
    n = int(entryNumber.get())
    textTable.delete("1.0", END)    #Clear content
    for i in range(1, 13):
        row = "{:3} x {:2} = {:3}\n".format(i, n, i*n)
        textTable.insert(END, row)  #Insert new content

#Import tkinter
from tkinter import *

#Create main window
window = Tk()
window.title("Multiplication Table")
window.geometry("400x300")

#Add widgets
labelNumber = Label(window, text="Enter number", width=12)
entryNumber = Entry(window, fg="red", width=24)
buttonNumber = Button(window, text="Display table", width=12, command=displayTable)
textTable = Text(window, fg="blue", width=18, height=12)

#Organise (lay out) the widgets using place() manager
labelNumber.place(x=20, y=20)
buttonNumber.place(x=20, y=60)
entryNumber.place(x=120, y=20)
textTable.place(x=120, y=60)

#Add main event loop (to handle user events)
window.mainloop()
