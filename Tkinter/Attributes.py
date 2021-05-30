from tkinter import *

root = Tk()

root.geometry("425x255")
root.title("Archit's GUI")

# Important label options
# text - adds the Text      
# bd - background
# fg - foreground
# font - sets the font 
# padx - x padding
# pady - y padding
# relef - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text= '''Abdul Rashid Salim Salman Khan
 (pronounced [səlˈmaːn xaːn] (About this soundlisten); 27 December 1965)[4] is an Indian actor, producer, singer, painter[5] and television personality who works in Hindi films. In a film career spanning over thirty years, Khan has
  received numerous awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting.[6] He is cited in the media as one of the most commercially successful actors of Indian cinema.[7][8] Forbes 
  included him in their 2015 list of Top-Paid 100 Celebrity Entertainers in the world; Khan tied with Amitabh Bachchan for No. 
 71 on the list, both with earnings of $33.5 million.[9][10] According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was the highest-ranked Indian with 82nd rank with earnings of $37.7 million.[11][12]
  He is also known as the host of the reality show, Bigg Boss since 2010''',bg = "red", fg="yellow")

title_label.pack()

root.mainloop()