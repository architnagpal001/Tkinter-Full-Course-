from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# WidthxHeight
root.geometry("345x456")

#pic = PhotoImage(file="profile.jpeg")
image = Image.open("profile.jpeg")
pic = ImageTk.PhotoImage(image)

label = Label(image=pic)
label.pack()

root.mainloop()