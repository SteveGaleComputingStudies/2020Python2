# https://datatofish.com/create-pandas-dataframe/
#from vscode terminal prompt >
#> python -m pip install pandas
#>python -m pip install xlrd
import pandas as pd

#open file and read data 
roomTemps = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\RoomTemperature.xlsx')

#specify the columns
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature','Humidity','Time'])

print (df)

# filter out unneeded columns
dfRoomTemp = df.filter(["Room", "Temperature"]) 

# filter all rooms except E223
filter = df["Room"] == "E223"
dfE223Temp = df.where(filter, inplace=True)
#filter unnecesary columns
dfE223Temp = df.filter(["Time", "Temperature"])
# order by time ascending
dfE223Temp.sort_values("Time", inplace = True)

print (dfRoomTemp)
print (dfE223Temp)



# importing pandas package 
