from tkinter import *
root = Tk()

root.geometry("333x666")
f1 = Frame(root , bg = "red", borderwidth=7, relief=GROOVE)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root , bg = "grey", borderwidth=9, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter")
l.pack(pady=110)

l = Label(f2, text="Welcome to visual studio code", font= "Comicsansms 18 italic", fg="blue")
l.pack()

root.mainloop()