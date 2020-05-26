from tkinter import *

def onLoginButtonPress():
    pass

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = LEFT)
B1 = Button(top, text="Login",command=onLoginButtonPress)
B1.pack(side=RIGHT)

top.mainloop()