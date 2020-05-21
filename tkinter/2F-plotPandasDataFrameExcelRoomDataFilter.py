# https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/import-csv-file-python-using-pandas/
# https://datatofish.com/read_excel/
# https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
# https://www.geeksforgeeks.org/dealing-with-rows-and-columns-in-pandas-dataframe/

# pandas DataFrame data filtering

#from vscode terminal prompt >
#> python -m pip install pandas
#>python -m pip install xlrd
import pandas as pd
import matplotlib.pyplot as plt

#open excel file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns that match the excel file
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])
print(df)


# Filter example: we want only Time and temperature for room E223

#filter unnecesary columns , filter all rooms except E223
# SELECT Room,Temperature WHERE Room == "E223"
#print(df[['Time', 'Temperature']]) 
#
dfE223Temp = df[df["Room"] == "E223"]
print(dfE223Temp)
# ORDER BY Time ACSENDING
dfE223tempSorted = dfE223Temp.sort_values("Time")
print(dfE223tempSorted)

dfE223tempSorted.plot(x ='Time', y='Temperature', kind = 'bar')

#SELECT Time, Temperature FROM roomData WHERE Room == 'E208' ORDER BY Time ASCENDING

dfE208Temp = df[df["Room"] == "E208"]               # SELECT * WHERE  Room == E208
dfE208Temp = dfE208Temp[['Time', 'Temperature']]    # SELECT Time , Temperature
dfE208Temp = dfE208Temp.sort_values("Time")   # ORDER BY Time ASCENDING
print(dfE208Temp)
dfE208Temp.plot(x ='Time', y='Temperature', kind = 'bar')
plt.show()