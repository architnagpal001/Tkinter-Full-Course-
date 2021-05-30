from tkinter import *

def Archit(event):
    print(f"You clicked on the button at {event.x}, {event.y}")


root = Tk()
root.title("Events in Tkinter")
root.geometry("333x666")

widget = Button(root, text="Click me Please")
widget.pack()

widget.bind('<Button-1>', Archit)
widget.bind('<Double-1>', quit)

root.mainloop()