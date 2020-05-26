import tkinter as tk

top = tk.Tk()

C = tk.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 125, 150
arc = C.create_arc(coord, start=0, extent=90, fill="red")

C.pack()
top.mainloop()