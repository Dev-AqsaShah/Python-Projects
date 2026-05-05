import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')

# print(df.head())  start 5 lines print hongi

# print(df.tail())   end 5 lines

# print(df.info())  

# print(df.describe()) 

# print(df['Age'].mean())

# print(df['city'].unique())

# print(df['col'].unique())  konsi unique hn values

# print(df['Cabin'].nunique()) kitni hnunique values

# missing data 

#df.isnull().sum()  

# true means vlue is missing

# df.duplicated()



#df.isnull()
print(df.info())

