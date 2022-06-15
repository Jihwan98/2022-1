from tkinter import *
from tkinter import messagebox

window = Tk()
def func1():
    print('1번 버튼')
    messagebox.showinfo("1번 버튼", "Hi")
def func2():
    print('2번 버튼')
    messagebox.showinfo("2번 버튼", "Hello")

btn1 = Button(window, text='1번 버튼', command=func1)
btn2 = Button(window, text='2번 버튼', command=func2)

btn1.pack(side='left')
btn2.pack(side='left')

window.mainloop()