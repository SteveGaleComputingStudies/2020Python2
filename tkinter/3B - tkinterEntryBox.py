# https://datatofish.com/entry-box-tkinter/

import tkinter as tk

root= tk.Tk()                                           # set up tkinter

canvas1 = tk.Canvas(root, width = 400, height = 300)    # canvas to display items
canvas1.pack()

entry1 = tk.Entry (root)                                # text entry box
canvas1.create_window(200, 140, window=entry1)          # display entry box on canvas

def getSquareRoot ():                                   # function called from button press
    x1 = entry1.get()                                   # text entry box value
    
    label1 = tk.Label(root, text= float(x1)**0.5)       #label to display value
    canvas1.create_window(200, 230, window=label1)      # window in canvas for label
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)  # call function on button press event
canvas1.create_window(200, 180, window=button1)         # window in canvas for button

root.mainloop()                                         #tkinter main loop