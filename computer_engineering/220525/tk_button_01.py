from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x100")

def func():
    print("Pushed")

button = Button(window, text='Push!', command=func)

button.pack()

window.mainloop()