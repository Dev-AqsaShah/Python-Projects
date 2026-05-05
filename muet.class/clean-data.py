import pandas as pd

df = pd.read_csv("nyc_housing_base.csv")

df = df.dropna(axis=1, how='all')  # empty columns remove
df = df.fillna(0)  # null values ko 0 se fill

print(df.head())