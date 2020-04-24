# https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/import-csv-file-python-using-pandas/
# https://datatofish.com/read_excel/
#from vscode terminal prompt >
#> python -m pip install pandas
#>python -m pip install xlrd
import pandas as pd

#open excel file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])
print (df)


# Filter example: we want only Time and temperature for room E223

#filter unnecesary columns , filter all rooms except E223
# SELECT Room, Time, Temperature WHERE Room == "E223"
dfE223Temp = df.filter(["Room","Time", "Temperature"]).where(df["Room"] == "E223")
print (dfE223Temp)
# ORDER BY Time ACSENDING
dfE223Temp.sort_values("Time", inplace = True)
print (dfE223Temp)
#remove empty records inplace - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
dfE223Temp.dropna(inplace = True)
print (dfE223Temp)



