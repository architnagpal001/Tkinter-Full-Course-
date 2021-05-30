from tkinter  import *
import tkinter.messagebox as tmsg 

root=Tk()
root.geometry("444x222")
root.title("Radiobutton Tutorial")

def order():
    tmsg.showinfo("Order received!", f"We have received your order for {var.get()}, thanks for ordering")

var = StringVar()
var.set("Radio")

Label(root, text= "What would you like to have ,Sir?", justify=LEFT, pady=14, font="Helvetica 18 italic").pack()

radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Pizza", padx=14, variable=var, value="Pizza").pack(anchor="w")
radio = Radiobutton(root, text="Lassi", padx=14, variable=var, value="Lassi").pack(anchor="w")
radio = Radiobutton(root, text="Paranthe", padx=14, variable=var, value="Paranthe").pack(anchor="w")
radio = Radiobutton(root, text="Cheese Burger", padx=14, variable=var, value="Cheese Burger").pack(anchor="w")

Button(text="Order Now", command=order).pack()

root.mainloop()