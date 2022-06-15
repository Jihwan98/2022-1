from tkinter import *
from tkinter import messagebox

window = Tk()

def func1():
    if chk1.get() == 0:
        messagebox.showinfo("1","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("1", "체크버튼이 켜졌어요.")
def func2():
    if chk2.get() == 0:
        messagebox.showinfo("2", "2 체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("2", "2 체크버튼이 켜졌어요.")
chk1, chk2 = IntVar(), IntVar()
print(chk2)
cb1 = Checkbutton(window, text='1111', variable=chk1, command=func1)
cb2 = Checkbutton(window, text='2222', variable=chk2, command=func2)
cb1.pack()
cb2.pack()

window.mainloop()