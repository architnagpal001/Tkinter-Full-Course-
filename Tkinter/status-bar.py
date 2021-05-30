from tkinter import * 

def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time 
    time.sleep(7)
    statusvar.set("Ready Now")

root = Tk()
root.geometry("444x222")
root.title("Status Bar tutorial")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=GROOVE, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text = "Upload", command=upload).pack()

root.mainloop()