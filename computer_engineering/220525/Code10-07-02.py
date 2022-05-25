from tkinter import *
from tkinter import messagebox
window = Tk()

## 함수 선언 부분 ##
def  myFunc1() :
    if chk1.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")
def  myFunc2() :
    if chk2.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")
    
## 메인 코드 부분 ##
chk1 = IntVar()
chk2 = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk1, command = myFunc1)
cb2 = Checkbutton(window, text = "클릭하세요", variable = chk2, command = myFunc2)

cb1.pack()
cb2.pack()

window.mainloop()
