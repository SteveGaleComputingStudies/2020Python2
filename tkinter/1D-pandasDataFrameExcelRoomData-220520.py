# https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/import-csv-file-python-using-pandas/
# https://www.geeksforgeeks.org/dealing-with-rows-and-columns-in-pandas-dataframe/


#pandas DataFrame loaded from excel data with data filtering
#from vscode terminal prompt >
#> python -m pip install pandas
#>python -m pip install xlrd
import pandas as pd

#open file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns that match the excel file
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])

print(df)

# filter out unneeded columns, make a new DataFrame with just Room and Temperature values
dfRoomTemp = df[["Room", "Temperature"]]

print(dfRoomTemp)

