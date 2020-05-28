# https://stackoverflow.com/questions/41168567/how-do-i-get-the-output-of-tkinter-to-print-into-gui-instead-of-cli

import tkinter as tk
import subprocess

def ping():
    cmd = ["ping", entry.get()]  # for linux   #, "-c", "2"]
    output = subprocess.check_output(cmd)   # execueres os command and returns output 
    #output = subprocess.check_output("ping {} -c 2".format(entry.get()), shell=True)

    print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')

my_gui = tk.Tk()
entry = tk.StringVar()

my_gui.geometry('300x300')
my_gui.title("Get output inside GUI") 

tk.Label(my_gui, text="Enter target IP or host as required.").pack() 
tk.Entry(my_gui, textvariable=entry).pack()
tk.Button(my_gui,text="Ping Test", command=ping).pack() 

# label for ping result
result = tk.Label(my_gui)
result.pack()

my_gui.mainloop()