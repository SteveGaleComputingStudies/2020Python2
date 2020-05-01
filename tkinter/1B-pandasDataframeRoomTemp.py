#ref - https://datatofish.com/create-pandas-dataframe/
#Activity add humidity for each room

#pandas DataFrame containing room temperature of rooms
#from vscode terminal prompt >
#> python -m pip install pandas
import pandas as pd

roomTemps = {'Room': ['E223','E222','E208','E219'],
        'Temperature': [22.1,21.4,23.5,22.6]
        }

df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature'])         # set up pandas DataFrame from dictionary

print (df)