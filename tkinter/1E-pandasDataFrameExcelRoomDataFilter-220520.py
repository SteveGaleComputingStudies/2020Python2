# https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/import-csv-file-python-using-pandas/
# https://datatofish.com/read_excel/
# https://www.geeksforgeeks.org/dealing-with-rows-and-columns-in-pandas-dataframe/

# pandas DataFrame data filtering

#from vscode terminal prompt >
#> python -m pip install pandas
#>python -m pip install xlrd
import pandas as pd

#open excel file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns that match the excel file
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])
print(df)


# Filter example: we want only Time and temperature for room E223

# filter all rooms except E223
# SELECT * WHERE Room == "E223"
dfE223 = df[df["Room"] == "E223"]
print(dfE223)

#filter unnecesary columns, we want only Time and temperature
dfE223TimeTemp = dfE223[["Time", "Temperature"]]
print(dfE223TimeTemp)
# ORDER BY Time ACSENDING
dfE223TimeTempSorted = dfE223TimeTemp.sort_values("Time")
print(dfE223TimeTempSorted)

#alternative method
#dfE223Temp = df.filter(["Room","Time", "Temperature"]).where(df["Room"] == "E223")


