from tkinter import *
root = Tk()

def click():
    print(uservalue.get())
    print(passvalue.get())

root.geometry("200x400")
user = Label(root, text="username")
password = Label(root, text="Password")
user.grid()
password.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

b1 = Button(text="Submit here", command = click).grid()
root.mainloop()