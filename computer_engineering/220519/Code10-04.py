from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:\\Users\\zxwlg\\workspace\\2022-1\\computer_engineering\\220519\\dog.gif")
label1 = Label(window, image = photo)

label1.pack();

window.mainloop()
