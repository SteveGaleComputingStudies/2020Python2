#https://datatofish.com/message-box-python/
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()                                               # set up tkinter

canvas1 = tk.Canvas(root, width = 300, height = 300)        # canvas to display items
canvas1.pack()

def ExitApplication():                                      # function called from button press
    # message box 
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':                                     # user response from messagebox tested
       root.destroy()                                       # exit program
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
# call function on button press event
button1 = tk.Button (root, text='Exit Application',command=ExitApplication,bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)             # window in canvas for button
  
root.mainloop()                                             #tkinter main loop