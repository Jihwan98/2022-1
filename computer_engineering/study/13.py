from tkinter import *
from tkinter import messagebox

window = Tk()

def func1():
    if var.get() == 0:
        messagebox.showinfo('1', '1 선택')
    else:
        messagebox.showinfo('2', '2 선택')

var = IntVar()
rb1 = Radiobutton(window, text="111", variable=var, value=1, command=func1)
rb2 = Radiobutton(window, text='222', variable=var, value=2, command=func1)

rb1.pack()
rb2.pack()

window.mainloop()