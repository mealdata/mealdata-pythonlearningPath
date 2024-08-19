import pandas as pd
import numpy as np

# Correct method to read an Excel file
excel = pd.read_excel('dummy.xlsx')


# Displaying the first 17 rows
print(excel.head(17))

# Displaying the shape of the dataset
print(excel.shape)

# Displaying the last 10 rows
print(excel.tail(10))

