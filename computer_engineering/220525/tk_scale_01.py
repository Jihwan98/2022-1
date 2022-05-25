from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x200")

val = IntVar()
val.set(0)

def func(scl):
    label.config(text='Value = %d'%int(scl))

label = Label(window, text='Value = %d'%val.get())
label.pack()

# s = Scale(window, label='Scale', orient='h', from_=0, to=100, showvalue=False, variable=val, command=func)
s = Scale(window, label='Scale', orient='v', from_=0, to=100, showvalue=False, variable=val, command=func)
s.pack()

window.mainloop()