import pandas as pd 
import numpy as np

excel_file = pd.read_excel('ECC-BaseLine-Survey_Phase2-2024.xlsx')

# Displaying the first five heads(rows)
print(excel_file.head())
# displaying the last 10 rows 
print(excel_file.tail(10))
# to display the first 100 rows 
#print(excel_file.head(100))

# to open file only column name How old are you? in the excel_file 
age_column = excel_file['How old are you?']

print(age_column)
# To descrip the summary of descriptive static
print(age_column.describe())

# I want to create the additional column nagaed age_category drafted/based from the How old are you? cloumn 

def categories_age(age):
    if pd.isna(age) and age == '': # nan is stands for Not a Number 
        return pd.nan
    age = int(age)
    if 0<= age <=5:
        return 'o-5'
    elif 6<= age <=14:
        return '6-14'
    elif 15<= age <=17:
        return '15-17'
    elif 18<= age <=24:
        return '18-24'
    elif 25<= age <=60:
        return '25-60'
    elif age>=61:
        return '>60'
    else:
        return pd.nan 

# Apply the function to the 'How old are you?' column to create 'age_category'

excel_file['age_categories'] = excel_file['How old are you?'].apply(categories_age)

# To rename the existing column in the excel_file 
excel_file.rename(columns={'What is your gender?':'Sex'}, inplace=True)

# to open changed column from What is your gender? to Sex and see its %
colunm_sex = excel_file['Sex'].value_counts(normalize=True)*100

print(colunm_sex)

# Descrip the summary of sex colum

print(colunm_sex.describe())

# open the new created column age_categories 

age_categories = excel_file['age_categories'].value_counts()

y= age_categories.reset_index()

# Convert the Series to a DataFrame and reset the index

y.columns= ['Age_group', 'Frequency']
y.index= ['row1', 'row2', 'row3']
print(y)


# Calculate frequency
frequency = excel_file['age_categories'].value_counts()

# Calculate percentage
percentage = excel_file['age_categories'].value_counts(normalize=True) * 100

# Combine into a DataFrame
y = pd.DataFrame({'Frequency': frequency, 'Percentage': percentage})

# Rename the index to Age_group
y.index.name = 'Age_group'
print(y)

# To display the above y dataframe in html. 

from IPython.display import display

# my dataframe is `y`

print(" ")
display(y)
# to print y DataFrame in html code 
print(" ")
print(" ")
code_html =y.to_html() # output html code 
print(table_html)

#  install tabulate use pip install tabulate 
# create table form out put of above y DataFrame

from tabulate import tabulate

# Create a table format
table = tabulate(y, headers='keys', tablefmt='grid')
print(table)





