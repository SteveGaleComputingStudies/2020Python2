# BASED on - tkinter\5-tkinterRoomTempDisplay1.py AND tkinter\2F-plotPandasDataFrameExcelRoomDataFilter.py
# https://datatofish.com/matplotlib-charts-tkinter-gui/
#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
import tkinter as tk
import pandas as pd #SG changed
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# added from tkinter\2F-plotPandasDataFrameExcelRoomDataFilter.py
#open excel file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns that match the excel file
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])
print(df)

##Sg added code
dfRoomTemp = df[['Room','Temperature']]
dfE223Temp = df[df["Room"] == "E223"]

root= tk.Tk() 

#plot Room temperatures 
figure1 = plt.Figure(figsize=(6,5), dpi=100)            # Figure to display the plot
ax1 = figure1.add_subplot(111)                          # Axes to use for the plot - subplot(m,n,p) divides the current figure into an m-by-n grid and creates axes in the position specified by p
bar1 = FigureCanvasTkAgg(figure1, root)                 # bar1 widget - backend that combines matplotlib Figure with a tkinter Canvas and returns a Widget
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)   # pack the bar1 widget onto the TkCanvas
dfRoomTemp = dfRoomTemp[['Room','Temperature']] #.groupby('Room').avg()   ## arrange the dataFrame for plotting - required to label axes correctly
dfRoomTemp.plot(kind='bar', legend=True, ax=ax1)        # plot the DataFrame to the Axes on the Figure
ax1.set_title('Room temperature')                       # set the title of the Axis

#plot E223 temperature
figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
dfE223Temp = dfE223Temp[['Time','Temperature']].groupby('Time').sum()   #required to label axes correctly
dfE223Temp.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('E223 hourly room temperature')

root.mainloop()