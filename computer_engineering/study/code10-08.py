from tkinter import *

window = Tk()

var = IntVar()

def func():
    if var.get() == 1:
        label1.configure(text='파이썬')
    elif var.get() == 2:
        label1.configure(text='C++')
    else:
        label1.configure(text='JAVA')
rb1 = Radiobutton(window, text="파이썬", variable=var, value=1, command=func)
rb2 = Radiobutton(window, text="C++", variable=var, value=2, command=func)
rb3 = Radiobutton(window, text="JAVA", variable=var, value=3, command=func)
label1 = Label(window, text="선택한 언어 :", fg='red')
rb1.pack(side="left")
rb2.pack(side='left')
rb3.pack(side='left')
label1.pack(side='left')

window.mainloop()