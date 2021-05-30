from tkinter import* 
root = Tk()

def hello():
    print("My name is Archit Nagpal")

def hi():
    print("Playing Table Tennis")

def kemcho():
    print("Btech Cse 3rd year")

def kida():
    print("30 june 2001")

root.geometry("333x666")

frame = Frame(root, borderwidth=5, bg="red", relief=GROOVE)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, bg="grey", text="Tell Name", command=hello)
b1.pack(side=LEFT)

b2 = Button(frame, bg="grey", text="your hobby", command=hi)
b2.pack(side=RIGHT)

b3 = Button(frame, bg="grey", text="Your Standard", command=kemcho)
b3.pack(side=TOP)

b4 = Button(frame, bg="grey", text="Your Birthday", command=kida)
b4.pack(side=BOTTOM)

root.mainloop()