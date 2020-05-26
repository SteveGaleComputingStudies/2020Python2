import tkinter as tk
from tkinter import messagebox


top = tk.Tk()

def helloCallBack():
   tk.messagebox.showinfo('Return','You will now return to the application screen')

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()