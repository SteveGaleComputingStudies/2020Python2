#ref - https://datatofish.com/create-pandas-dataframe/
# https://datatofish.com/scatter-line-bar-charts-using-matplotlib/

#Activity add humidity for each room


#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
roomTemps = {'Room': ['E223','E222','E208','E219'],
        'Temperature': [22.1,21.4,23.5,22.6]
        }

df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature'])
print (df)

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