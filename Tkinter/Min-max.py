from tkinter import *

root = Tk()

# WidthxHeight
root.geometry("345x456")

# Width, Height
root.minsize(100,200)

# Width, height
root.maxsize(800, 1000)

Archit = Label(text="Archit is a python programmer")
Archit.pack()

root.mainloop()