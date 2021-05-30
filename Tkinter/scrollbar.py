from tkinter import *

root=Tk()
root.geometry("444x222")
root.title("ScrollBar Tutorial")

# For connecting scrollbar to a widget
#1. Widget(yscrollcommand = scrollbar.set)
#2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT , fill=Y)
lbx = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(344):
    lbx.insert(END, f"Item {i}")

lbx.pack(fill=BOTH, padx=22)
scrollbar.config(command = lbx.yview)

root.mainloop()