import pandas as pd
df = pd.read_csv("ml_training_data.csv")
print(df.head())
print(df['disease_name'].unique())
print(df.dtypes)
