from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\zxwlg\\workspace\\2022-1\\computer_engineering\\220519\\dog.gif")
photo2 = PhotoImage(file = "C:\\Users\\zxwlg\\workspace\\2022-1\\computer_engineering\\220519\\dog2.gif")
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT) # label1.pack(side=TOP)
label2.pack(side=LEFT) # label2.pack(side=TOP)

window.mainloop()
