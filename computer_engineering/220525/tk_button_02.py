from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x100")

def callme():
    print("Hey Dude!!")

def second():
    print("It's My Life")

button1 = Button(window, text='button1', command=callme)
button2 = Button(window, text='button2', command=second)

button1.pack()
button2.pack()

window.mainloop()