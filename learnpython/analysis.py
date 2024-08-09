import pandas as pd
file_path = '/workspace/mealdata-pythonfullstack/learnpython/mysite/polls/dummy1.xlsx'
df = pd.read_excel(file_path, sheet_name ="Dummy")
#print(df.head())
print(df.describe())