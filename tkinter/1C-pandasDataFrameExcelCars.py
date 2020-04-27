# https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/import-csv-file-python-using-pandas/
#from vscode terminal prompt >
#> python -m pip install pandas
#>python -m pip install xlrd
import pandas as pd

#open file and read data 
cars = pd.read_excel(r'C:\Users\sgale\OneDrive\2020-Teaching\Python ADCSE2\code\tkinter\Cars.xlsx')

#specify the columns that match the excel file
df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print (df)