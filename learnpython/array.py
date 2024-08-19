import pandas as pd 
import numpy as np 
# creating an array in python
data = [[1,4], [2,5], [3,6], [4,7]]

data1 =np.array(data)
print (data)
print(" ")
print(data1)

print(" ")

# Craeting dataframe
data2=pd.DataFrame(data)
print(data2)
# to replace the name of index(rows) and columns
data2=pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4'], columns=['column1','column2'])
print(data2)
print(" ") # to give black space between data2 and data2.shape
print(data2.shape)