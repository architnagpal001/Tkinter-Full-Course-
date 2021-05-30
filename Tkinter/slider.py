from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("444x222")

root.title("Slider's Tutorial")
def getdollar():
    print(f"We have credited {myslider.get()} to your account")
    tmsg.showinfo("Amount credited!", f"We have credited {myslider.get()} to your account")

Label(root, text="how many dollars do you want ?").pack()
myslider = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10)
myslider.set(21)
myslider.pack()

Button(root, text="Get Dollars!!", command=getdollar).pack()

root.mainloop()