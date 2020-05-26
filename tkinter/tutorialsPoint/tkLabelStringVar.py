# https://www.tutorialspoint.com/python3/tk_label.htm
# !/usr/bin/python3
from tkinter import *

root = Tk()

var = StringVar()
label = Label( root, textvariable = var, relief = RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
