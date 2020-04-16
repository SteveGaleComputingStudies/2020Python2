# - https://datatofish.com/scatter-line-bar-charts-using-matplotlib/
#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
from pandas import DataFrame
import matplotlib.pyplot as plt

# data to be plotted    
Data = {'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
        'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
       }

#put data into a pandas DataFrame   
df = DataFrame(Data,columns=['Unemployment_Rate','Stock_Index_Price'])

#plot the data, xaxis / y axis  
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')

#add the plot labels
plt.title('Unemployment Rate Vs Stock Index Price', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()