# https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/import-csv-file-python-using-pandas/
# 
#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

#open file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])

print (df)

# filter out unneeded columns
dfRoomTemp = df.filter(["Room", "Temperature"]) 

print (dfRoomTemp)

# data to be plotted    
#Data = {'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
#        'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
#       }

#put data into a pandas DataFrame   
#df = DataFrame(Data,columns=['Unemployment_Rate','Stock_Index_Price'])

#plot the data, xaxis / y axis  
plt.scatter(df['Room'], df['Temperature'], color='green')

#add the plot labels
plt.title('Room Vs Temperature', fontsize=14)
plt.xlabel('Room', fontsize=14)
plt.ylabel('Temperature', fontsize=14)
plt.grid(True)
plt.show()