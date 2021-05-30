from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0,0,800,200, fill="red")
can_widget.create_line(0,400,800,0, fill="red")

can_widget.create_rectangle(5, 5, 900, 500, fill="blue")

can_widget.create_oval(5, 5, 800, 400, fill="red")
can_widget.create_text(400, 200, text="Archit Nagpal", font="comicsansms 45 bold")

root.mainloop()