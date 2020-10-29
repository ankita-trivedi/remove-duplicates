import pandas as pd
df = pd.read_csv("file.csv")
print(df)
print(df.duplicated())
print(df.drop_duplicates(keep='first'))