# - https://datatofish.com/scatter-line-bar-charts-using-matplotlib/
#from vscode terminal prompt >
#> python -m pip install pandas
#> python -m pip install matplotlib
from pandas import DataFrame
import matplotlib.pyplot as plt
   
# data to be plotted
Data = {'Country': ['USA','Canada','Germany','UK','France'],
        'GDP_Per_Capita': [45000,42000,52000,49000,47000]
       }
  
#put data into a pandas DataFrame
df = DataFrame(Data,columns=['Country','GDP_Per_Capita'])


#add the data to the x axis
xAxis = [i + 0.5 for i, _ in enumerate(df['Country'])]
  
#plot the data, xaxis / y axis
plt.bar(xAxis, df['GDP_Per_Capita'].astype(float), color='teal')
#add the plot labels
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.xticks([i + 0.5 for i, _ in enumerate(df['Country'])], df['Country'])
plt.show()