from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.geometry("666x333")
root.title("Sublime Text")

def myfunc():
    print("Tera baap aaya")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "Archit will help you")

def rate():
    print("Rate us")
    value=tmsg.askquestion("Was your experience good", "You used this GUI,Was your experience good?")
    print(value)
    if value == "yes":
        msg = "Great,Now rate us"

    else:
        msg = "Tell Your problem"
    tmsg.showinfo("Experience", msg)

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)

# root.config(menu=mymenu)

filemenu = Menu(root)

m1 = Menu(filemenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=filemenu)

filemenu.add_cascade(label="File",menu=m1)

m2 = Menu(filemenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=filemenu)

filemenu.add_cascade(label="Edit",menu=m2)

m4 = Menu(filemenu, tearoff=0)
m4.add_command(label="Help", command=help)
m4.add_command(label="Rate us", command=rate)
root.config(menu=filemenu)
filemenu.add_cascade(label="Help", menu=m4)

m3 =Menu(filemenu, tearoff=0)
m3.add_command(label="Exit Now", command=quit)
root.config(menu=filemenu)

filemenu.add_cascade(label="Exit", menu=m3)


root.mainloop()