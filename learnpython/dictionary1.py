import pandas as pd
import numpy as np

# Correcting the spelling in country names
countries = ['Ethiopia', 'Kenya', 'Djibouti', 'South Africa']
population = ['121M', '80M', '50M', '100M']

# Creating dictionary1 with countries and population as keys
dictionary1 = {'countries': countries, 'population': population}

# Creating a zipped dictionary using dict(zip(countries, population))
dictionary2 = dict(zip(countries, population))

# Creating DataFrame from dictionary1
df = pd.DataFrame(dictionary1, index=['row1', 'row2', 'row3', 'row4'])

# Creating DataFrame from dictionary2
df1 = pd.DataFrame(list(dictionary2.items()), columns=['countries', 'population in M'])

# Output the dictionaries and DataFrames
print(dictionary1)
print(" ")
print(dictionary2)
print(" ")
print(df)
print(" ")
print(df1)

