# https://datatofish.com/create-pandas-dataframe/
#>python -m pip install xlrd
import pandas as pd

#open file and read data 
cars = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\Cars.xlsx')

#specify the columns
df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print (df)