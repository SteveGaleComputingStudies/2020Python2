# https://datatofish.com/create-pandas-dataframe/
#from vscode terminal prompt >
#> python -m pip install pandas

import pandas as pd

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print (df)